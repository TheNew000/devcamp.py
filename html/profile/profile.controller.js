(function () {
    function profileController($scope, $http) {
    	$scope.message  = "Profile View"
    }

    angular.module('devcamp')
        .controller('profileCtrl', ['$scope', '$http', profileController]);
})();