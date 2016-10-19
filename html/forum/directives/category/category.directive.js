/**
 * Created by Jackson on 10/14/16.
 */

(function () {
    // Haha philosophy joke
    function categoricalDirective() {
        return {
            restrict: 'E',
            transclude: true,
            scope: {
                title: '@'
            },
            templateUrl: 'forum/directives/category/category.template.html'
        }
    }

    angular.module('devcamp')
        .directive('category', categoricalDirective);
})();