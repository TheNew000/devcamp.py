(function () {
    function createBlog(){
        return {
            restrict: 'EA',
            templateUrl: 'common/directives/create_blog/create_blog.template.html',
            controller: 'createBlogCtrl'
        }
    }

    angular.module('devcamp')
        .directive('createblog', createBlog)
})();