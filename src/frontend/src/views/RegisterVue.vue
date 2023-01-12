<template>
    <main>
        <h1>Register</h1>
        <form @submit.prevent="register">
            <p style="color: red" v-if="isFailed">Invalid credentials</p>
            <label for="username">Username</label>
            <input type="text" name="username" id="username" v-model.trim="loginInfo.username">
            <label for="password">Password</label>
            <input type="password" name="password" id="password" v-model.trim="loginInfo.password">
            <button type="submit">Register</button>
        </form>
    </main>
</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue';

import authService from '@/services/auth.service';
import { useAuthStore } from '@/stores/auth';
import type { LoginInfo } from '@/types/user';

const isFailed = ref(false);
const loginInfo: Ref<LoginInfo> = ref({
    username: '',
    password: '',
});

const { login } = useAuthStore();

async function register() {
    console.log(loginInfo.value);
    try {
        await authService.register(loginInfo.value);
        await login(loginInfo.value);
    } catch (e) {
        isFailed.value = true;
    }
}
</script>
