<template>
    <div>
        <div v-if="loading" class="d-flex justify-content-center" style="height: 100vh">
            <div class="spinner-border spinner-center" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>


        <div v-if="product">
            <div v-if="editMod === false" class="container border-dark">
                <div class="card mb-3 bg-light" style="padding: 2%">
                    <div class="row no-gutters">
                        <div class="col-md-4 " style="text-align: center">
                            <img class="img-fluid" v-show="activePhoto" :src="activePhoto">
                            <div class="" style="overflow-x: auto; text-align: center;">
                                <div class="div-img-min" v-for="(photo, index) in product.post.photos">
                                    <img @mouseover="changeActivePhoto(index)" :src="photo.sizes[3].url" style="width: 50px; height: 50px">
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <ul class="list-inline" style="padding: 0px">

                                    <li class="list-group-item" style="text-align: center">
                                        <h3>{{product.title}}</h3>
                                    </li>

                                    <li class="list-group-item">
                                        <h5>Цена: <span class="comic">{{product.price_trade}}</span><i class="fas fa-ruble-sign"></i>
                                        / Оптовая: <span class="comic"> {{product.price}} </span><i class="fas fa-ruble-sign"></i></h5>
                                    </li>

                                    <li class="list-group-item">
                                        <span class="comic">Места: </span><span style="font-size: 1.02em" class="badge badge-secondary" v-for="place in product.places">{{place}}  </span>
                                    </li>

                                     <li class="list-group-item">
                                         <span class="comic">Категории: </span><span style="font-size: 1.02em" class="badge badge-secondary" v-for="categori in product.categories">{{categori}} </span>
                                    </li>

                                    <li class="list-group-item">
                                        <span style="font-size: 0.9em">{{product.description}}</span>
                                    </li>

                                     <li class="list-group-item" style="text-align: right">
                                         <button class="btn btn-secondary" @click="editMod = true">Редактировать</button>
                                        <button class="btn btn-primary">В корзину</button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>




            <div v-else class="container border-dark">
                <div class="card mb-3 bg-light" style="padding: 2%">
                    <div class="row no-gutters">
                        <div class="col-md-4 " style="text-align: center">
                            <img class="img-fluid" v-show="activePhoto" :src="activePhoto">
                            <div class="" style="overflow-x: auto; text-align: center;">
                                <div class="div-img-min" v-for="(photo, index) in product.post.photos">
                                    <img @mouseover="changeActivePhoto(index)" :src="photo.sizes[3].url" style="width: 50px; height: 50px">
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <ul class="list-inline" style="padding: 0px">

                                    <li class="list-group-item">
                                        <input type="text" v-model="product.title" placeholder="Название продукта">
                                    </li>

                                    <li class="list-group-item">
                                        <textarea rows="4" style="width: 100%" type="text" v-model="product.description"></textarea>
                                    </li>

                                    <li class="list-group-item">
                                        <div class="input-group" style="max-width: 250px;">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text">Опт(Руб.)</span>
                                            </div>
                                            <input type="number" placeholder="цена" class="form-control" v-model="product.price_trade">
                                        </div>
                                    </li>

                                    <li class="list-group-item">
                                        <div class="input-group" style="max-width: 250px;">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text">Роз(Руб.)</span>
                                            </div>
                                            <input type="number" placeholder="цена" class="form-control" v-model="product.price">
                                        </div>

                                        <div class="input-group" style="max-width: 250px;">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text">%</span>
                                            </div>
                                            <input type="number" placeholder="цена" class="form-control" v-model="product.percent">
                                        </div>

                                    </li>

                                    <li class="list-group-item">
                                        <span v-for="(place, index) in product.places" class="badge badge-secondary" @click="removeArrayElement(product.places, index)">{{place}} <i class="fas fa-times"></i></span>
                                        <div class="input-group ">
                                            <input type="text" placeholder="Место" v-model="inputPlace">
                                            <div class="input-group-append">
                                                <button class="btn btn-sm btn-outline-secondary" @click="addArrayElement(product.places, inputPlace); inputPlace = ''">Добавить</button>
                                            </div>
                                        </div>
                                    </li>

                                    <li class="list-group-item">
                                        <span v-for="(size, index) in product.sizes" class="badge badge-secondary" @click="removeArrayElement(product.sizes, index)">{{size}} <i class="fas fa-times"></i></span>
                                        <div class="input-group">
                                            <input type="text" placeholder="Размер" v-model="inputSize">
                                            <div class="input-group-append">
                                                <button class="btn btn-sm btn-outline-secondary"  @click="addArrayElement(product.sizes, inputSize); inputSize = ''">Добавить</button>
                                            </div>
                                        </div>
                                    </li>

                                    <li class="list-group-item">
                                        <span v-for="(categorie, index) in product.categories" class="badge badge-secondary" @click="removeArrayElement(product.categories, index)">{{categorie}} <i class="fas fa-times"></i></span>
                                        <div class="input-group">
                                            <input type="text" placeholder="Категория" v-model="inputCategorie">
                                            <div class="input-group-append">
                                                <button class="btn btn-sm btn-outline-secondary"  @click="addArrayElement(product.categories, inputCategorie); inputCategorie = ''">Добавить</button>
                                            </div>
                                        </div>
                                    </li>

                                    <li class="list-group-item" style="text-align: right">
                                        <button class="btn btn-secondary" @click="editMod=false">Отмена</button>
                                        <button class="btn btn-primary" @click="editProduct; editMod = false" style="margin-left: 1%">Отправить в каталог</button>
                                    </li>
                                </ul>
                            </div>
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
        name: "ProductDetail",
        data(){
            return{
                activePhotoId: 0,
                editMod: false,
                inputPlace:'',
                inputSize: '',
                inputCategorie: '',
            }
        },
        props: ['id'],
        computed:{
            ...mapState({
                product: state => state.product.product_detail,
                loading: state => state.product.loading_product
            }),
            activePhoto: function () {
                return this.product.post.photos[this.activePhotoId].sizes[3].url
            }
        },
        methods:{
            changeActivePhoto(id){
                this.activePhotoId = id
            },
            addArrayElement(array, element,){
                element=`${element}`
                if(!array.includes(element) && element.length > 0) {
                    let array_element = element.split(',')
                    for(let index in array_element) {
                        array.push(array_element[index].trim(' '))
                    }
                }

            },
            editProduct(){
                let product = {
                    id: this.product.id,
                    post: this.product.post.id,
                    title: this.product.title,
                    price_trade: this.product.price_trade,
                    price: this.product.price,
                    percent: this.product.percent,
                    description: this.product.description,
                    sizes: this.product.sizes,
                    places: this.product.places,
                    categories: this.product.categories,
                }
                this.$store.dispatch('product/editProduct', product)
            },
            removeArrayElement(array, index){
                array.splice(index, 1)
            },
        },
        created: function() {
            this.$store.dispatch('product/getProduct', this.id)
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
    .comic{
        font-family: Comic Sans MS;
    }
</style>