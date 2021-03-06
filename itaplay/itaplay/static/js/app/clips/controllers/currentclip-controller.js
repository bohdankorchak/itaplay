function CurrentClipController($scope, $sce, $http, $routeParams, $location, Upload, $timeout) {

    var id = $routeParams.clip_id;
    $scope.init = function() {
        $http.get("clips/" + id).then(function(response) {
            $scope.data = response.data;
            $scope.myAmazonUrl = response.data[0].fields.url

            $scope.trustSrc = function(src) {
                return $sce.trustAsResourceUrl(src);
            }

            $scope.clipUrl = { src: $scope.myAmazonUrl };

            console.log(response);


        }, function(response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
    };

};
