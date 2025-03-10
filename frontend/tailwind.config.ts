import type { Config } from 'tailwindcss'

export default {
  content: [
    "./components/**/*.{vue,js,ts}",
    "./layouts/**/*.{vue,js,ts}",
    "./pages/**/*.{vue,js,ts}",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./assets/css/**/*.css"
  ],
  theme: {
    extend: {
      colors: {
        'background': '#0f172a',
        'primary': '#6d28d9',
        'secondary': '#10b981',
        'text': '#e2e8f0',  // Changed from textColor to text
        'accent': '#f59e0b'
      },
      animation: {
        'pulse-slow': 'pulse 4s infinite'
      },
      container: {
        center: true,
        padding: {
          DEFAULT: '1rem',
          sm: '2rem',
          lg: '4rem',
          xl: '5rem',
          '2xl': '6rem',
        },
        screens: {
          sm: '640px',
          md: '768px',
          lg: '1024px',
          xl: '1280px',
          '2xl': '1536px',
        },
      }
    }
  },
  plugins: []
} as Config
