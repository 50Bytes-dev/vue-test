import Vue from 'vue'
import Router from 'vue-router'
import Catalog from '@/components/post_catalog/Catalog'
import PostDetail from '@/components/post_catalog/PostDetail'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'post_catalog',
      component: Catalog,
    },
    {
      path: '/post_catalog/detail/:id',
      name: 'post_detail',
      component: PostDetail,
      props: true,
    },
  ]
})
