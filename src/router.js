import Vue from 'vue'
import Router from 'vue-router'
import Catalog from '@/components/post_catalog/Catalog'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'post_catalog',
      component: Catalog
    },
  ]
})
