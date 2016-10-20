(function() {
    function createBlogController($scope, $http) {
    	$('#editor').froalaEditor()
    }
    angular.module('devcamp')
        .controller('createBlogCtrl', ['$scope', '$http', createBlogController])
})();
