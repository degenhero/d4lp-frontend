<script setup>
import { computed } from "vue";
import { useWindowScroll } from "@vueuse/core";
import { ArrowUp } from "lucide-vue-next"; // ✅ Import Lucide Icon

const { y } = useWindowScroll();
const isVisible = computed(() => y.value > 300);

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
};
</script>

<template>
  <button
    v-if="isVisible"
    @click="scrollToTop"
    class="fixed bottom-6 right-6 backdrop-blur-lg bg-white/10 border border-white/20
           text-white p-4 rounded-full shadow-xl transition-all transform hover:scale-110 
           hover:bg-white/20 backdrop-saturate-150 z-50 flex items-center justify-center"
  >
    <ArrowUp class="w-6 h-6 text-white" />
  </button>
</template>

<style scoped>
button {
  box-shadow: 0 4px 30px rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}
</style>
