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

            .when('/forum', {
                templateUrl: 'forum/forum/forum.view.html',
                controller: 'forumCtrl'
            })

            .when('/forum/:id', {
                templateUrl: 'forum/thread-list/thread-list.view.html',
                controller: 'threadListCtrl'
            })

            .when('/forum/:id/new', {
                templateUrl: 'forum/new-thread/new-thread.html'
            })

            .when('/topic/:id', {
                templateUrl: 'forum/thread/thread.view.html',
                controller: 'threadCtrl'
            })

            .when('/members', {
                templateUrl: 'members/members.view.html',
                controller: 'membersCtrl'
            })
            .when('/blogs', {
                templateUrl: 'blogs/blogs.view.html',
                controller: 'blogsCtrl'
            })

            .otherwise({
                redirectTo: '/'
            });

        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common["X-Requested-With"];
        $httpProvider.defaults.headers.common["Accept"] = "application/json";
        $httpProvider.defaults.headers.common["Content-Type"] = "application/json";
    }

    function mainController($scope, $route) {
        $scope.loggedIn = false;
        $scope.username = "Jackson";

        $scope.isActive = function (path) {
            if ($route.current && $route.current.regexp) {
                return $route.current.regexp.test(path);
            }
            return false;
        };
    }

    angular.module('devcamp')
        .config(['$routeProvider', '$httpProvider', config])
        .controller('mainCtrl', ['$scope', '$route', mainController])
})();