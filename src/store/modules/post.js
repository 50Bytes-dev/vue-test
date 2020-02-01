import postService from '@/services/postService'


const state = {
  posts: [],
  post_detail: null,
  loading_post: true,
};

const getters = {
  // posts: function(state) {
  //   return state.posts
  // },
  // post_detail: function(state) {
  //   return state.post_detail
  // }
};

const actions = {
  getPosts ({ commit }) {
    postService.fetchPosts()
    .then(posts => {
      commit('setPosts', posts)
    })
  },
  getPost ({ commit, state }, id) {
    state.loading_post = true;
    postService.fetchPost(id)
    .then(post => {
      state.loading_post = false;
      commit('setPost', post)
    })
  },
};

const mutations = {
  setPosts (state, posts) {
    state.posts = posts
  },
  setPost (state, post) {
    state.post_detail = post
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}