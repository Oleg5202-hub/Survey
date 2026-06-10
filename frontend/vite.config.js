import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      "/get_questions": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true
      },
      "/add_questions": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true
      },
      "/save_answers": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true
      },
      "/get_results": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true
      }
    }
  }
});
