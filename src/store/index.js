import Vue from 'vue'
import Vuex from 'vuex'
import post from './modules/post'
import product from './modules/product'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    post,
    product,
  }
})