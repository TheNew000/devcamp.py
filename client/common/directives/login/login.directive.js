/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    function login(){
        return {
            restrict: 'EA',
            templateUrl: 'common/directives/login/login.template.html',
            controller: 'loginCtrl'
        }
    }

    angular.module('devcamp')
        .directive('login', login)
})();