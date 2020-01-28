<template>
    <div>
        <div v-for="post in posts">
            <CardPost :post = "post"></CardPost>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import CardPost from "./CardPost";

    export default {
        name: "Catalog",
        components: {
            CardPost
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
