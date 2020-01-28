import api from '@/services/api'

export default {
    fetchPosts() {
        return api.get(`post/`)
            .then(response => response.data)
    },
}