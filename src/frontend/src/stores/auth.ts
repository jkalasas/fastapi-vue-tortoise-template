import { defineStore } from "pinia";
import { ref } from "vue";

import authService from "@/services/auth.service";
import router from "@/router";
import type { LoginInfo } from "@/types/user";

export const useAuthStore = defineStore('auth', () => {
    const accessToken = ref(authService.getAccessToken());
    const isAuthenticated = ref(accessToken.value !== '');
    const returnName = ref('');

    if (isAuthenticated.value) {
        authService.me().catch(() => {
            isAuthenticated.value = false;
            router.push({ name: 'Login' });
        });
    }

    const login = async (user: LoginInfo): Promise<boolean> => {
        const returnTo = returnName.value || 'Home';
        try {
            const data = await authService.login(user);
            returnName.value = '';
            isAuthenticated.value = true;
            accessToken.value = data.access_token;

            await router.push({ name: returnTo });
        } catch (e) {
            return false;
        }
        return true;
    };

    const logout = async (): Promise<void> => {
        accessToken.value = '';
        isAuthenticated.value = false;
        authService.logout();

        await router.push({ name: 'Login' });
    };

    return { accessToken, isAuthenticated, returnName, login, logout };
});
