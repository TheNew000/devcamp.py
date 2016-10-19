/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    threadController.$inject = ['$scope', 'forum', '$routeParams'];
    function threadController($scope, forum, $routeParams) {
        $scope.forumID = $routeParams.id;
        $scope.thread = {};

        forum.getThread($scope.forumID)
            .then(function (response) {
                console.log(response.data.thread_object);
                $scope.thread = response.data.thread_object;
            })
    }

    angular.module('devcamp')
        .controller('threadCtrl', threadController)
})();