import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: true, // Это самое важное! Позволяет Docker пробрасывать порт
    port: 5173,
    watch: {
      usePolling: true // Нужно для Windows/WSL, чтобы файлы обновлялись
    }
  }
})
