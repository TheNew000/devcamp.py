/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    function auth($http, $window, $route){
        var login = function(user){
            return $http.post('http://localhost:5000/api/login')
                .then(function(response){

                })
        }
    }
})();