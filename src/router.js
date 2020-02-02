import Vue from 'vue'
import Router from 'vue-router'
import Catalog from '@/components/post_catalog/Catalog'
import PostDetail from '@/components/post_catalog/PostDetail'
import ProductCatalog from "@/components/product/ProductCatalog";
import ProductDetail from "@/components/product/ProductDetail";


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/post_catalog',
      name: 'post_catalog',
      component: Catalog,
    },
    {
      path: '/post_catalog/detail/:id',
      name: 'post_detail',
      component: PostDetail,
      props: true,
    },
    {
      path: '/',
      name: 'product_catalog',
      component: ProductCatalog,
    },
     {
       path: '/product_catalog/detail/:id',
       name: 'product_detail',
       component: ProductDetail,
       props: true,
     }
  ]
})
