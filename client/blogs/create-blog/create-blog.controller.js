(function() {
    function createBlogController($scope, $http) {
        // $('#createBlogModal').on('shown.bs.modal', function() {
        //     $('textarea').focus();
        // });


    }
    angular.module('devcamp')
        .controller('createBlogCtrl', ['$scope', '$http', createBlogController])
})();
