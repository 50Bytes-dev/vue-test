import postService from '@/services/postService'

const state = {
  posts: []
};

const getters = {
  posts: function(state) {
    return state.posts
  }
};

const actions = {
  getPosts ({ commit }) {
    postService.fetchPosts()
    .then(posts => {
      commit('setPosts', posts)
    })
  },
};

const mutations = {
  setPosts (state, posts) {
    state.posts = posts
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}