(function () {
    function registerController($scope) {
        $scope.register = function () {
            if ($scope.password != $scope.confirm) {
                alert('Your passwords do not match!');
            } else {
                $http.post(apiPath + '/register', {
                    fullName: $scope.fullname,
                    userName: $scope.username,
                    email: $scope.email,
                    password: $scope.password,
                    title: $scope.title,
                    avatar: $scope.avatar
                }).then(function success(response) {
                    if (response.status == 200) {
                        $cookies.put('token', response.token);
                        $cookies.put('username', $scope.username);
                        $location.path('/main');
                    } else {
                        alert(response.message);
                    }
                }, function error(response) {
                    console.log(response.data.message);
                });
            }
        };
    }

    angular.module('devcamp')
        .controller('registerCtrl', ['$scope', registerController])

})();
