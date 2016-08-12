import json

from authentication.models import AdviserInvitations, AdviserUser

from django.views.generic import View

from forms import UserForm, UserInvitationForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from utils.EmailService import EmailSender

from models import User

from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib import auth

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def validate_verification_code(func):
    """
    Decorator that check is verification code valid, existing and open
    :param func: function, that be wrapped
    :return: nothing
    """
    def wrapper(self, request, *args, **kwargs):
        """
        Wrapper, that checks verification code
        :param self:
        :param request:
        :param args:
        :param kwargs:
        :return: BadRequest when verification code is incorrect or function in other case
        """
        verification_code = request.GET.get("code", "")

        if verification_code:
            if AdviserInvitations.objects.filter(verification_code=verification_code).exists():
                invitation = AdviserInvitations.objects.get(verification_code=verification_code)

                if not invitation.is_active:
                    return HttpResponseBadRequest("Invitation is already used")
            else:
                return HttpResponseBadRequest("No open invitation")
        else:
            return HttpResponseBadRequest("Invalid code")
        return func(self, request, *args, **kwargs)
    return wrapper


class RegistrationView(View):
    """
    View used for handling registration
    """

    @validate_verification_code
    def get(self, request):
        """
        Handling GET method
        :param request: Request to View
        :return: rendered registration page
        """
        return render(request, "register.html")


    @validate_verification_code
    def post(self, request):
        """
        Handling GET method
        :param request: Request to View
        :return: HttpResponse with code 201 if user is created or
        HttpResponseBadRequest if request contain incorrect data
        """
        verification_code = request.GET.get("code", "")

        invitation = AdviserInvitations.get_invitation(verification_code)

        data = json.loads(request.body)
        base_form = UserForm(data)

        if not base_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")

        new_base_user = base_form.save(commit=False)
        new_base_user.username = invitation.email
        new_base_user.email = invitation.email
        new_base_user.set_password(data['password'])
        new_base_user.save()

        new_extended_user = AdviserUser()
        new_extended_user.setup_user(new_base_user, invitation)
        new_extended_user.save()

        invitation.close_invitation()

        return HttpResponse(status=201)


class InviteView(View):
    """View that handles user invitation"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InviteView, self).dispatch(*args, **kwargs)

    def post(self, request):
        """Handling GET method
            :param request: Request to View
            :return: HttpResponse with code 201 if user is invited or
                     HttpResponseBadRequest if request contain incorrect data
        """

        invite_form = UserInvitationForm(request.POST)

        if not invite_form.is_valid():
            return HttpResponseBadRequest("Invalid input data. Please edit and try again.")

        if User.objects.filter(email=invite_form.data[u'email']).exists():
            return HttpResponseBadRequest("User with this e-mail is registered")

        if AdviserInvitations.objects.filter(email=invite_form.data[u'email']).exists():
            return HttpResponseBadRequest("User with this e-mail is already invited")

        sender = EmailSender(invite_form.data[u'email'])
        print sender.send_invite(invite_form.data[u'id_company'])
        return HttpResponse(status=201)

    def get(self, request):
        """
        Handling GET method
            :param request: Request to View
            :return: rendered inviting page
        """
        invite_form = UserInvitationForm()
        return render(request, "invite.html", {
            'inviteForm': invite_form
        })


class LoginView(View):

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(LoginView, self).dispatch(*args, **kwargs)


    def post(self, request):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse(status=200)

        else:
            return HttpResponse("incorect username or password", status=401)

        #else:
        return HttpResponse(status=400)


    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')




