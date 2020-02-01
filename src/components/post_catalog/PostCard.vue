<template>
    <div class="card bg-light mb-3 border-dark">
        <figure class="figure" style="max-height: 260px">
            <img :src="photo_url" class="card-img-top img-fluid">
        </figure>
        <div class="card-body">
            <ul class="list-group  list-group-flush">
                <li class="list-group-item bg-light">
                    <h5 class="card-title"><a target="_blank" :href="post_url">Открыть пост</a></h5> </li>
                <li class="list-group-item bg-light" style="text-overflow: clip">Дата поста: <span class="text-muted">{{post.date_post}}</span></li>
                <li class="list-group-item bg-light"> <router-link :to="{name: `post_detail`, params: {id: post.id}}" class="btn-block btn btn-primary" tag="button">Подробно</router-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PostCard",
        data() {
            return {}
        },
        props: ['post'],
        computed: {
            post_url: function () {
                return `https://vk.com/id${this.post.owner_id}?w=wall${this.post.from_id}_${this.post.post_id}`
            },
            photo_url: function() {
                return  this.post.photos[0].sizes[3].url
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