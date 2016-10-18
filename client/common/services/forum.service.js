/**
 * Created by Jackson on 10/18/16.
 */

(function(){
    function forumService($http){
        function getMainDisplay(){
            return $http.get('http://localhost:5000/api/forum_main')
        }

        function getThreads(id){
            return $http.get('http://localhost:5000/api/get_forum/' + id)
        }

        return {
            getMainDisplay: getMainDisplay,
            getThreads: getThreads
        }
    }

    angular.module('devcamp')
        .service('forum', ['$http', forumService])
})();