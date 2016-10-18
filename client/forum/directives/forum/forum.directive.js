/**
 * Created by Jackson on 10/14/16.
 */

(function () {
    function forumDirective() {
        return {
            restrict: 'E',
            transclude: true,
            scope: {
                title: '@',
                description: '@'
            },
            templateUrl: 'forum/directives/forum/forum.template.html'
        }
    }

    angular.module('devcamp')
        .directive('forum', forumDirective);
})();