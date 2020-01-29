<template>
    <div class="card" style="width: 18rem;">
        <img :src="photo_url" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title"><a target="_blank" :href="post_url">Открыть пост</a></h5>
            <p class="card-text">{{post.text}}</p>
        </div>

        <ul class="list-group list-group-flush">
            <li class="list-group-item">Дата поста: <span class="text-muted">{{post.date_post}}</span></li>
            <li class="list-group-item">Дата создания: <span class="text-muted">{{post.date_created}}</span></li>
        </ul>
        <div class="card-body">
            <button>Открыть</button>
            <button>Подробно</button>
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
    }
</style>