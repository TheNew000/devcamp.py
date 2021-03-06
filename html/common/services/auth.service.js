/**
 * Created by Jackson on 10/13/16.
 */

(function () {
    auth.$inject = ['$http', '$window'];
    function auth($http, $window) {
        var setToken = function (token) {
            $window.localStorage['devtoken'] = token;
        };

        var getToken = function () {
            return $window.localStorage['devtoken'];
        };

        var logout = function () {
            $window.localStorage.removeItem('devtoken');
        };

        var getProfile = function (id) {
            return http.get('http://dannyarango.com:7070/api/profile/' + id);
        };

        var isLoggedIn = function () {
            var token = getToken();
            var payload;

            if (token) {
                payload = token.split('.')[1];
                payload = $window.atob(payload);
                payload = JSON.parse(payload);

                return payload.exp > Date.now() / 1000;
            } else {
                return false;
            }
        };

        var login = function (user) {
            return $http.post('http://dannyarango.com:7070/api/login', user)
        };

        var register = function (user) {
            return $http.post('http://dannyarango.com:7070/api/register', user)
        };

        return {
            setToken: setToken,
            getToken: getToken,
            logout: logout,
            isLoggedIn: isLoggedIn,
            login: login,
            register: register,
            getProfile: getProfile
        }
    }

    angular.module('devcamp')
        .service('auth', auth);
})();
