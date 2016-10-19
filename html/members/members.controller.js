(function(){
    function membersController($scope, $http){
    	$scope.memberRequest = function(user_id){
    		$http({
      			url: 'api/follow/'+user_id,
      			method: "GET",
      			headers: { 'Content-Type': 'application/json' }
    	}).success(function(response) {
      		console.log(response)
    });
 };

   		$scope.username = "Freddy Fingas";
   		$scope.title = "Bootcamp Student";
   		$scope.rank = "Rank: " + 3

    }
    angular.module('devcamp')
        .controller('membersCtrl', ['$scope','$http', membersController])
})();