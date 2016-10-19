
(function(){
    function blogsService($http){
        function getDatabaseData(){
            return $http.get('http://162.243.19.103:5000/api/blog_post')
        }

        // function getThreads(id){
        //     return $http.get('http://162.243.19.103:5000/api/get_forum/' + id)
        // }

        // function getThread(id) {
        //     return $http.get('http://162.243.19.103:5000/api/get_thread/' + id)
        // }

        // function createThread(id, thread) {
        //     return $http.post('http://162.243.19.103:5000/api/create_thread/' + id, thread)
        // }

        // function createReply(id, reply) {
        //     return $http.post('http://162.243.19.103:5000/api/create_reply/' + id, reply)
        // }

        return {
            getDatabaseData: getDatabaseData
            // getThreads: getThreads,
            // getThread: getThread,
            // createThread: createThread,
            // createReply: createReply
        }
    }

    angular.module('devcamp')
        .service('blog', ['$http', blogService])
})();
