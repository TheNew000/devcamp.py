/**
 * Created by Jackson on 10/13/16.
 */
(function(){
    angular.module('devcamp', ['ngRoute', 'ngSanitize', 'ngAnimate', 'ngCookies', 'ngMessages']);

    function config($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl: 'home/home.view.html',
                controller: 'homeCtrl'
            })

            .otherwise({
                redirectTo: '/'
            })
    }

    function mainController($scope) {
        $scope.loggedIn = false;
        $scope.username = "Jackson";
    }

    angular.module('devcamp')
        .config(['$routeProvider', config])
        .controller('mainCtrl', ['$scope', mainController])
})();