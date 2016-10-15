(function(){
    function blogsController($scope, $http){
      $scope.message = "Blogs Template"

    }
    angular.module('devcamp')
        .controller('blogsCtrl', ['$scope','$http', blogsController])
})();