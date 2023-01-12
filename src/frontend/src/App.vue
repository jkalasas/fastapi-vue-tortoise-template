<template>
  <header>
    <RouterLink :to="{ name: 'Home' }" v-if="isAuthenticated">Home</RouterLink>
    <a href="#" v-if="isAuthenticated" @click="logout">Logout</a>
    <RouterLink :to="{ name: 'Login' }" v-if="!isAuthenticated">Login</RouterLink>
    <RouterLink :to="{ name: 'Register' }" v-if="!isAuthenticated">Register</RouterLink>
  </header>
  <RouterView />
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { RouterLink, RouterView } from 'vue-router';

import { useAuthStore } from '@/stores/auth';

const { isAuthenticated } = storeToRefs(useAuthStore());
const { logout } = useAuthStore();
</script>
