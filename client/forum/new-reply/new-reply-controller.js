/**
 * Created by Jackson on 10/18/16.
 */

(function () {
    createThread.$inject = ['$scope', 'forum', '$routeParams', '$location'];
    function createThread($scope, forum, $routeParams, $location) {
        $scope.thread = {
            author_id: 1
        };

        $scope.submit = function () {
            forum.createReply($routeParams.id, $scope.thread)
                .then(function (err, response) {
                    if (err) {
                        console.log(err);
                    }

                    $location.path('/topic/' + $routeParams.id);
                })
        }
    }

    angular.module('devcamp')
        .controller('newReplyCtrl', createThread)
})();