(function() {
    function blogsController($scope, blog) {
        $scope.data = [];
        blog.getDatabaseData()
            .then(function(response){
                for(var i = 0; i < response.data.display.length; i++){
                    $scope.data.push(response.data.display[i]);
                }
            });

       
    }
    angular.module('devcamp')
        .controller('blogsCtrl', ['$scope', '$http', blogsController])

})();
