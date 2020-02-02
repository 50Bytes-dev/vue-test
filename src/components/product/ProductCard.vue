<template>
    <div class="card bg-light mb-3 border-dark">
        <figure class="figure" style="max-height: 260px">
            <img :src="photo_url" class="card-img-top img-fluid">
        </figure>
        <div class="card-body">
            <ul class="list-group  list-group-flush">
                <li class="list-group-item bg-light" style="text-overflow: clip">
                    Цена: <span class="text-muted">{{product.price}}</span>
                </li>
                <li class="list-group-item bg-light" style="text-overflow: clip">
                    Размер: <span class="text-muted"></span>
                </li>
                <li class="list-group-item bg-light" style="text-overflow: clip">
                    <router-link :to="{name: `product_detail`, params: {id: product.id}}" class="btn-block btn btn-primary" tag="button">Подробно</router-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ProductCard",
        props: ['product'],
        computed: {
            photo_url: function() {
                return  this.product.post.photos[0].sizes[2].url
            }
        },
    }
</script>

<style scoped>
    .list-group-item {
        font-size: 0.85em;
    }
    .card {
        margin-bottom: 1%;
        width: 18rem;
        height: 98%;
    }
    .card-body{
        padding: 0px;
    }
</style>