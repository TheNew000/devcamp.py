/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    function loginController($scope, auth) {
        $scope.register = function () {
            auth.register({
                username: "jackson",
                password: "password"
            }).then(function (response) {
                console.log(response.statusText);
            })
        }
    }

    angular.module('devcamp')
        .controller('loginCtrl', ['$scope', 'auth', loginController]);
})();