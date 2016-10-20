(function () {
    function registration(){
        return {
            restrict: 'E',
            templateUrl: 'common/directives/registration/registration.template.html',
            controller: 'registerCtrl'
        }
    }

    angular.module('devcamp')
        .directive('register', registration)
})();