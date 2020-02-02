import productService from "../../services/productService";

const state = {
  products: [],
  product_detail: null,
  loading_product: true,
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
   getProduct ({ commit, state }, id) {
     state.loading_product = true;
     productService.fetchProduct(id)
         .then(product => {
           state.loading_product = false;
           commit('setProduct', product)
         })
   }
};

const mutations = {
  addProduct (state, product) {
    state.products.push(product)
  },
  setProducts (state, products) {
    state.products = products
  },
    setProduct (state, product) {
    state.product_detail = product
  },
};


export default {
  namespaced: true,
  state,
  actions,
  mutations,
}