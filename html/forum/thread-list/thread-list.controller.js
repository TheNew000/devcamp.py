/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    function threadListController($scope, $routeParams, forum) {
        $scope.catID = $routeParams.id;
        $scope.forum = {};

        forum.getThreads($scope.catID)
            .then(function(response){
                $scope.forum = response.data.thread_object;
                console.log($scope.forum.threads[0].post_time);
            })
    }

    threadListController.$inject = ['$scope', '$routeParams', 'forum'];
    angular.module('devcamp')
        .controller('threadListCtrl', threadListController)
})();