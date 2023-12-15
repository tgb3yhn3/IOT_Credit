// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/Home.vue'),
      },
    ],
  },
  {
    path: '/credit',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'credit',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/creditView.vue'),
      },
    ],
  },
  {
    path: '/advise',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'advise',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/adviseView.vue'),
      },
    ],
  },
  {
    path: '/report',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'report',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/reportView.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
