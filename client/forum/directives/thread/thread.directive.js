/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    function threadDirective() {
        return {
            restrict: 'E',
            templateUrl: 'forum/directives/thread/thread.template.html',
            transclude: true,
            scope: {
                author: '@',
                title: '@',
                id: '@'
            }
        }
    }

    angular.module('devcamp')
        .directive('thread', threadDirective)
})();