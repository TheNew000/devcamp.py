/**
 * Created by Jackson on 10/13/16.
 */
(function () {
    function homeController($scope, $http) {
        $scope.helloWorld = "";

        $http.get('http://localhost:5000/api/hello')
            .then(function(response){
                console.log(response);
                $scope.helloWorld = response.data.hello
            })
    }

    angular.module('devcamp')
        .controller('homeCtrl', ['$scope', '$http', homeController]);
})();