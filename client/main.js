/**
 * Created by Jackson on 10/13/16.
 */
(function () {
    angular.module('devcamp', ['ngRoute', 'ngSanitize', 'ngAnimate', 'ngCookies', 'ngMessages']);

    function config($routeProvider, $httpProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'home/home.view.html',
                controller: 'homeCtrl'
            })

            .otherwise({
                redirectTo: '/'
            });

        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common["X-Requested-With"];
        $httpProvider.defaults.headers.common["Accept"] = "application/json";
        $httpProvider.defaults.headers.common["Content-Type"] = "application/json";
    }

    function mainController($scope) {
        $scope.loggedIn = false;
        $scope.username = "Jackson";
    }

    angular.module('devcamp')
        .config(['$routeProvider', '$httpProvider', config])
        .controller('mainCtrl', ['$scope', mainController])
})();