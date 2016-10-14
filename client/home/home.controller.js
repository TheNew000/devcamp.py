/**
 * Created by Jackson on 10/13/16.
 */
(function () {
    function homeController($scope, $http) {

    }

    angular.module('devcamp')
        .controller('homeCtrl', ['$scope', '$http', homeController]);
})();