/**
 * Created by Jackson on 10/17/16.
 */

(function () {
    function threadListController($scope, $routeParams) {
        $scope.threads = [
            {
                title: 'Hello, world!',
                author: 'Jackson',
                posts: 16,
                views: 10
            },
            {
                title: 'Hambone',
                author: 'Jackson',
                posts: 16,
                views: 10
            },
            {
                title: 'Hambone',
                author: 'Jackson',
                posts: 16,
                views: 10
            }
        ];

        $scope.catID = $routeParams.id;
    }

    threadListController.$inject = ['$scope', '$routeParams'];
    angular.module('devcamp')
        .controller('threadListCtrl', threadListController)
})();


var announcement_permissions = {
    view_forum: {
        admin: 1,
        moderator: 1,
        member: 1
    },
    create_thread: {
        admin: 1,
        moderators: 0,
        members: 0
    },
    reply_to_thread: {
        admin: 1,
        moderator: 1,
        member: 1
    }
};

var display = [
    {
        id: 0,
        title: "First Category",
        forums: [
            {
                id: 0,
                title: "Introductions",
                description: "Introduce yourself to the community",
                last_post: '324985458273', // Unix timestamp
                permissions: {
                    view_forum: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    },
                    create_thread: {
                        admin: 1,
                        moderators: 0,
                        members: 0
                    },
                    reply_to_thread: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    }
                }
            },
            {
                id: 1,
                title: "Another Forum",
                description: "This is another forum",
                last_post: '324985458273', // Unix timestamp
                permissions: {
                    view_forum: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    },
                    create_thread: {
                        admin: 1,
                        moderators: 1,
                        members: 1
                    },
                    reply_to_thread: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    }
                }
            }
        ]
    },
    {
        id: 1,
        title: "Second Category",
        forums: [
            {
                id: 0,
                title: "Introductions",
                description: "Introduce yourself to the community",
                last_post: '324985458273', // Unix timestamp
                permissions: {
                    view_forum: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    },
                    create_thread: {
                        admin: 1,
                        moderators: 0,
                        members: 0
                    },
                    reply_to_thread: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    }
                }
            },
            {
                id: 1,
                title: "Another Forum",
                description: "This is another forum",
                last_post: '324985458273', // Unix timestamp
                permissions: {
                    view_forum: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    },
                    create_thread: {
                        admin: 1,
                        moderators: 1,
                        members: 1
                    },
                    reply_to_thread: {
                        admin: 1,
                        moderator: 1,
                        member: 1
                    }
                }
            }
        ]
    }
];