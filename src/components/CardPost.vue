<template>
    <div>
        <div class="card" style="width: 18rem;">
            <img src="" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Название карточки</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            </div>

            <ul class="list-group list-group-flush">
                <li></li>
                <li class="list-group-item">Ид: 220р </li>
                <li class="list-group-item"></li>
                <li class="list-group-item"></li>
            </ul>
            <div class="card-body">
                <a href="#" class="card-link">Card link</a>
                <a href="#" class="card-link">Another link</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CardPost",
        data(){
            return{
                photosObj:{},
            }
        },
        props:['post'],
        mounted:function () {
            let textSizes = this.post.photos[0].sizes;
            this.photosObg = JSON.parse(textSizes.replace(/'/g, '"'))
        }
    }
</script>

<style scoped>

</style>