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

        function getThread(id) {
            return $http.get('http://localhost:5000/api/get_thread/' + id)
        }

        function createThread(id, thread) {
            return $http.post('http://localhost:5000/api/create_thread/' + id, thread)
        }

        function createReply(id, reply) {
            return $http.post('http://localhost:5000/api/create_reply/' + id, reply)
        }

        return {
            getMainDisplay: getMainDisplay,
            getThreads: getThreads,
            getThread: getThread,
            createThread: createThread,
            createReply: createReply
        }
    }

    angular.module('devcamp')
        .service('forum', ['$http', forumService])
})();