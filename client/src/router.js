import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import HedgeHogs from '@/components/pages/HedgeHogs'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HedgeHogs',
      component: HedgeHogs
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
