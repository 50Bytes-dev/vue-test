<template>
    <div class="container">
        <div class="row">
            <div v-for="post in posts" class="col col-auto">
                <PostCard :post = "post"></PostCard>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import PostCard from "./PostCard";

    export default {
        name: "Catalog",
        components: {
            PostCard
        },
        computed:{
            ...mapState({
                posts: state => state.post.posts
            })
        },
        created() {
            this.$store.dispatch('post/getPosts')
        }
    };
</script>

<style scoped>
</style>
