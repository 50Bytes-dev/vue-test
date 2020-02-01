import api from '@/services/api'

export default {
    fetchPosts() {
        return api.get(`post/`)
            .then(function (response) {
                return response.data
            })
    },
    fetchPost(id) {
        return api.get(`post/${id}`)
            .then(response => response.data)
    },
}