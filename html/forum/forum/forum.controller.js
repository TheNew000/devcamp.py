/**
 * Created by Jackson on 10/14/16.
 */

(function () {
    function forumController($scope, forum) {
        $scope.categories = [];

        forum.getMainDisplay()
            .then(function(response){
                for(var i = 0; i < response.data.display.length; i++){
                    $scope.categories.push(response.data.display[i]);
                }
            });

    }

    angular.module('devcamp')
        .controller('forumCtrl', ['$scope', 'forum', forumController]);
})();