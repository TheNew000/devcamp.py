/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    function loginController($scope, auth) {
        $scope.register = function () {
            auth.register({
                username: $scope.username,
                password: $scope.password
            }).then(function (response) {
                console.log(response.statusText);
            })
        }
    }

    angular.module('devcamp')
        .controller('loginCtrl', ['$scope', 'auth', loginController]);
})();