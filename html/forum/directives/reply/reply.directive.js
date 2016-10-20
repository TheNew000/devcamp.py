/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    function threadDirective() {
        return {
            restrict: 'E',
            templateUrl: 'forum/directives/reply/reply.template.html',
            transclude: true,
            scope: {
                author: '@'
            }
        }
    }

    angular.module('devcamp')
        .directive('reply', threadDirective)
})();