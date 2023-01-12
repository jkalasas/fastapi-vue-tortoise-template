import { createApp } from 'vue';
import { createPinia, storeToRefs } from 'pinia';
import type { RouteLocationNormalized } from 'vue-router';

import App from '@/App.vue';
import router from '@/router';
import { useAuthStore } from './stores/auth';

const app = createApp(App);

app.use(createPinia());
app.use(router);

router.beforeEach(
    (
        to: RouteLocationNormalized,
        from: RouteLocationNormalized,
        next: Function
    ) => {
        const { isAuthenticated, returnName } = storeToRefs(useAuthStore());

        if (to.meta.public) next();
        else if (to.meta.notAuthenticated && isAuthenticated.value)
            next({ name: from.name?.toString() || 'Home' });
        else if (!to.meta.notAuthenticated && !isAuthenticated.value && to.name?.toString() !== 'Login') {
            returnName.value = to.name?.toString() || '';
            next({ name: 'Login' });
        } else next();
    }
);

app.mount('#app');
