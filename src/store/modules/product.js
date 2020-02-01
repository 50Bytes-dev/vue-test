import productService from "../../services/productService";

const state = {
  products: [],
};

const actions = {
  addProduct ({commit}, product) {
    productService.addProduct(product)
    .then(product => {
      commit('addProduct', product)
    })
  },
  getProducts ({ commit }) {
    productService.fetchProducts()
    .then(products => {
      commit('setProducts', products)
    })
  },
};

const mutations = {
  addProduct (state, product) {
    state.products.push(product)
  },
  setProducts (state, products) {
    state.products = products
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
}