(function() {
    function blogsController($scope, $http) {
        $scope.openModal = function() {
            tinymce.init({
                selector: 'textarea',
                height: 200,
                plugins: [
                    'advlist autolink lists link image charmap print preview anchor',
                    'searchreplace visualblocks code fullscreen',
                    'insertdatetime media table contextmenu paste code'
                ],
                toolbar: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
                content_css: '//www.tinymce.com/css/codepen.min.css'
            });
        }
        $http({
            method: 'get',
            url: 'http://127.0.0.1:5000/api/blogs'
        }).then(function successCallback(response){
            console.log(response.data);
        })

    }
    angular.module('devcamp')
        .controller('blogsCtrl', ['$scope', '$http', blogsController])

})();
