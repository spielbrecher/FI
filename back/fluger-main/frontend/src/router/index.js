import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/company',
    name: 'Company',
    component: () => import('../views/Company.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/risk',
    name: 'RiskProfile',
    component: () => import('../views/RiskProfile.vue')
  },
  {
    path: '*',
    name: 'Error',
    component: () => import('../views/Error.vue')
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
