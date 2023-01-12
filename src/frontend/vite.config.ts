import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

const apiURI = process.env.API_URI || 'http://localhost:8000';

export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: apiURI,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api /, ''),
      },
    },
  },
});
