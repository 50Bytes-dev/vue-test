<template>
    <div>
        <div v-if="loading" class="d-flex justify-content-center" style="height: 100vh">
            <div class="spinner-border spinner-center" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <div v-if="post" class="container border-dark">
            <div class="card mb-3 bg-light" style="padding: 2%">
                <div class="row no-gutters">
                    <div class="col-md-4 " style="text-align: center">
                            <img class="img-fluid" v-show="activePhoto" :src="activePhoto">
                        <div class="" style="overflow-x: auto; text-align: center;">
                            <div class="div-img-min" v-for="(photo, index) in post.photos">
                                <img @mouseover="changeActivePhoto(index)" :src="photo.sizes[3].url" style="width: 50px; height: 50px">
                            </div>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <ul class="list-inline" style="padding: 0px">
                                <li class="list-group-item"><textarea rows="4" style="width: 100%" type="text" v-model="post.text"></textarea></li>

                                <li class="list-group-item" style="">
                                    <div class="input-group" style="max-width: 250px;">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">Опт(Руб.)</span>
                                        </div>
                                        <input type="number" placeholder="цена" class="form-control" v-model="priceOpt">
                                    </div>
                                </li>

                                <li class="list-group-item">
                                    <div class="input-group" style="max-width: 250px;">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">Роз(Руб.)</span>
                                        </div>
                                        <input type="number" placeholder="цена" class="form-control" v-model="priceRoz">
                                    </div>
                                </li>

                                <li class="list-group-item">
                                    <span v-for="(place, index) in places" class="badge badge-secondary" @click="removeArrayElement(places, index)">{{place}} <i class="fas fa-times"></i></span>
                                    <div class="input-group ">
                                        <input type="text" placeholder="Место" v-model="inputPlace">
                                        <div class="input-group-append">
                                            <button class="btn btn-sm btn-outline-secondary" @click="addArrayElement(places, inputPlace); inputPlace = ''">Добавить</button>
                                        </div>
                                    </div>
                                </li>

                                <li class="list-group-item">
                                    <span v-for="(size, index) in sizes" class="badge badge-secondary" @click="removeArrayElement(sizes, index)">{{size}} <i class="fas fa-times"></i></span>
                                    <div class="input-group">
                                        <input type="text" placeholder="Размер" v-model="inputSize">
                                        <div class="input-group-append">
                                            <button class="btn btn-sm btn-outline-secondary"  @click="addArrayElement(sizes, inputSize); inputSize = ''">Добавить</button>
                                        </div>
                                    </div>
                                </li>

                                <li class="list-group-item" style="text-align: right">
                                    <button class="btn btn-secondary">Отмена</button>
                                    <button class="btn btn-primary" style="margin-left: 1%">Отправить в каталог</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import {mapState} from 'vuex'

    export default {
        name: "PostDetail",
        data(){
            return{
                activePhotoId: 0,
                priceOpt: 0,
                priceRoz: 0,
                sizes:[],
                inputSize: '',
                places:[],
                inputPlace:'',
            }
        },
        props: ['id'],
        computed:{
            ...mapState({
                post: state => state.post.post_detail,
                loading: state => state.post.loading_post
            }),
            activePhoto: function () {
                return this.post.photos[this.activePhotoId].sizes[3].url
            }
        },
        methods:{
            changeActivePhoto(id){
                this.activePhotoId = id
            },
            addArrayElement(array, element, array_element){
                if(!array.includes(element) && element.length > 2) {
                    array_element = element.split(',')
                    for(let index in array_element) {
                        array.push(array_element[index].trim(' '))
                    }
                }

            },
            removeArrayElement(array, index){
                array.splice(index, 1)
            },
        },
        created: function() {
            this.$store.dispatch('post/getPost', this.id)
        }

    }
</script>

<style scoped>
    .spinner-center{
        margin-top: auto;
        margin-bottom: auto;
    }
    img{
        border: 1px solid silver;
    }
    .div-img-min{
        display: inline-block;
        margin-left: 2%;
        padding-top: 1%
    }
</style>