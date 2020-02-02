import api from '@/services/api'

export default {
    addProduct(product){
        return api.post('product/', product)
            .then(response => response.data)
    },
     fetchProducts() {
        return api.get(`product/`)
            .then(function (response) {
                return response.data
            })
    },
     fetchProduct(id) {
        return api.get(`product/${id}`)
            .then(response => response.data)
    },

}