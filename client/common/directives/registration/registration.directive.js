(function () {
    function registration(){
        return {
            restrict: 'EA',
            templateUrl: 'common/directives/registration/registration.template.html',
            controller: 'registrationCtrl'
        }
    }

    angular.module('devcamp')
        .directive('registration', registration)
})();