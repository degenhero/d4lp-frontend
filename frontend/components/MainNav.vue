<script setup>
import { ref } from "vue";
import { Home, Rocket, Layers, FileText, Users, LogIn } from "lucide-vue-next"; // ✅ Import Lucide Icons

const menuOpen = ref(false);
const toggleMenu = () => (menuOpen.value = !menuOpen.value);
</script>

<template>
  <nav class="fixed top-0 w-full z-50 bg-white/10 backdrop-blur-md border-b border-white/20 shadow-lg">
    <div class="container mx-auto px-6 py-4 flex justify-between items-center">
      <!-- LOGO -->
      <NuxtLink to="#top" class="text-white text-xl font-bold flex items-center space-x-2">
        <Rocket class="w-6 h-6 text-orange-400" />
        <span>D4L</span>
      </NuxtLink>

      <!-- NAVIGATION MENU -->
      <div class="hidden md:flex items-center space-x-6 text-white">
        <NuxtLink to="#home" class="flex items-center space-x-1 hover:text-orange-400 transition">
          <Home class="w-5 h-5" />
          <span>Home</span>
        </NuxtLink>

        <NuxtLink to="#auction" class="flex items-center space-x-1 hover:text-orange-400 transition">
          <Rocket class="w-5 h-5" />
          <span>Auction</span>
        </NuxtLink>

        <NuxtLink to="#features" class="flex items-center space-x-1 hover:text-orange-400 transition">
          <Layers class="w-5 h-5" />
          <span>Features</span>
        </NuxtLink>

        <NuxtLink to="#whitepaper" class="flex items-center space-x-1 hover:text-orange-400 transition">
          <FileText class="w-5 h-5" />
          <span>Whitepaper</span>
        </NuxtLink>

        <NuxtLink to="#community" class="flex items-center space-x-1 hover:text-orange-400 transition">
          <Users class="w-5 h-5" />
          <span>Community</span>
        </NuxtLink>
      </div>

      <!-- LOGIN BUTTON -->
      <NuxtLink
        to="#login"
        class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 shadow-lg transition"
      >
        <LogIn class="w-5 h-5" />
        <span>Login</span>
      </NuxtLink>

      <!-- MOBILE MENU BUTTON -->
      <button @click="toggleMenu" class="md:hidden text-white focus:outline-none">
        <Layers class="w-6 h-6" />
      </button>
    </div>

    <!-- MOBILE MENU -->
    <div v-if="menuOpen" class="absolute top-full left-0 w-full bg-black/80 backdrop-blur-md text-white flex flex-col py-4">
      <NuxtLink to="#" class="py-2 px-6 flex items-center space-x-2 hover:bg-orange-500/20 transition">
        <Home class="w-5 h-5" />
        <span>Home</span>
      </NuxtLink>

      <NuxtLink to="#auction" class="py-2 px-6 flex items-center space-x-2 hover:bg-orange-500/20 transition">
        <Rocket class="w-5 h-5" />
        <span>Auction</span>
      </NuxtLink>

      <NuxtLink to="#features" class="py-2 px-6 flex items-center space-x-2 hover:bg-orange-500/20 transition">
        <Layers class="w-5 h-5" />
        <span>Features</span>
      </NuxtLink>

      <NuxtLink to="#whitepaper" class="py-2 px-6 flex items-center space-x-2 hover:bg-orange-500/20 transition">
        <FileText class="w-5 h-5" />
        <span>Whitepaper</span>
      </NuxtLink>

      <NuxtLink to="#community" class="py-2 px-6 flex items-center space-x-2 hover:bg-orange-500/20 transition">
        <Users class="w-5 h-5" />
        <span>Community</span>
      </NuxtLink>
    </div>
  </nav>
</template>

