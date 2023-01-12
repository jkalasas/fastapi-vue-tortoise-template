import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/login',
      name: 'Login',
      meta: {
        notAuthenticated: true,
      },
      component: () => import('@/views/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'Register',
      meta: {
        notAuthenticated: true,
      },
      component: () => import('@/views/RegisterVue.vue'),
    },
  ],
});

export default router;
