// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  modules: [
    '@nuxtjs/tailwindcss',
    '@hypernym/nuxt-gsap',
    '@pinia/nuxt',
    '@vueuse/nuxt'
  ],
  css: ['assets/css/main.css'],
  gsap: {
    extraPlugins: {
      scrollTrigger: true
    }
  }
})