<template>
    <main>
        <h1>Login</h1>
        <form @submit.prevent="onSubmitLogin">
            <p style="color: red" v-if="isFailed">Invalid username or password</p>
            <label for="username">Username</label>
            <input type="text" name="username" id="username" v-model.trim="loginInfo.username">
            <label for="password">Password</label>
            <input type="password" name="password" id="password" v-model.trim="loginInfo.password">
            <button type="submit">Login</button>
        </form>
    </main>
</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue';

import { useAuthStore } from '@/stores/auth';
import type { LoginInfo } from '@/types/user';

const isFailed: Ref<boolean> = ref(false);
const loginInfo: Ref<LoginInfo> = ref({
    username: '',
    password: '',
});

const { login } = useAuthStore();

async function onSubmitLogin() {
    isFailed.value = await login(loginInfo.value);
}
</script>