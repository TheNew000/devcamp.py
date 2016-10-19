/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    function threadsDirective() {
        return {
            restrict: 'E',
            templateUrl: 'forum/directives/thread-summary/thread-summary.template.html',
            scope: {
                title: '@',
                author: '@',
                posts: '@',
                views: '@',
                posted: '@',
                id: '@'
            }
        }
    }

    angular.module('devcamp')
        .directive('threadSummary', threadsDirective)
})();