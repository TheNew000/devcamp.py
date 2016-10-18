/**
 * Created by Jackson on 10/14/16.
 */

(function () {
    function forumController($scope) {
        $scope.forums = [
            {
                title: "Introductions",
                description: "Introduce yourself to the community"
            },
            {
                title: "Another Forum",
                description: "This is another forum. What's up bro?"
            },
            {
                title: "Hambone",
                description: "The bone of ham"
            }
        ];

        $scope.categories = [
            {
                title: "First Category",
                forums: $scope.forums
            },
            {
                title: "Second Category",
                forums: $scope.forums
            },
            {
                title: "Third Category",
                forums: $scope.forums
            }
        ];
    }

    angular.module('devcamp')
        .controller('forumCtrl', ['$scope', forumController]);
})();