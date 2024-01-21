import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/Home/HomeView.vue')
    },
    {
      path: '/plan',
      name: 'Plan',
      component: () => import('../views/PlanView.vue')
    }
  ]
})

export default router
