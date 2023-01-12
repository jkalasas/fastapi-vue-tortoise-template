export { }

import 'vue-router';

declare module 'vue-router' {
    interface RouteMeta {
        public?: boolean;
        notAuthenticated: boolean;
    }
}
