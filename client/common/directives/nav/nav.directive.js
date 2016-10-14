/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    function navigation(){
        return {
            restrict: 'EA',
            templateUrl: 'common/directives/nav/nav.template.html',
            controller: 'navCtrl'
        }
    }

    angular.module('devcamp')
        .directive('navigation', navigation)
})();