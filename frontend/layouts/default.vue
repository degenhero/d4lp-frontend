<template>
  <div class="min-h-screen bg-background text-white flex flex-col">
    <!-- Top Navigation -->
    <MainNav />
    
    <!-- Main Content with smooth page transitions -->
    <main class="flex-grow mt-[72px]"> <!-- Fixed height of nav -->
      <transition name="page" mode="out-in">
        <slot />
      </transition>
    </main>

    <!-- Floating UI for Auction Info -->
    <FloatingUI v-if="showFloatingUI" />
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { LucideMenu, LucideLogIn } from 'lucide-vue-next'
import { useScrollSpy } from "~/composables/useScrollSpy"

const route = useRoute()
const showFloatingUI = ref(false)
const { activeSection } = useScrollSpy(["about", "auction", "features", "community", "contact"])

onMounted(() => {
  // Show floating UI only on home page
  showFloatingUI.value = route.path === '/'
})
</script>

<style scoped>
/* Page Transitions */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.3s ease;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
}

/* Navbar Link Styling */
.nav-link {
  @apply text-white hover:text-accent transition px-3 py-2;
}
</style>
