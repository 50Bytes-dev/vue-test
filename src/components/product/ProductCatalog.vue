<template>
    <div class="container">
        <div class="row">
            <div v-for="product in products" class="col col-auto">
                <ProductCard :product = "product"></ProductCard>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import ProductCard from "./ProductCard";
    export default {
        name: "ProductCatalog",
        components: {
            ProductCard
        },
        computed:{
            ...mapState({
                products: state => state.product.products
            })
        },
        created() {
            this.$store.dispatch('product/getProducts')
        }
    }
</script>

<style scoped>

</style>