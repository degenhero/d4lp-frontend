<template>
  <div class="glass-effect p-6 rounded-xl hover:scale-105 transition-transform">
    <component :is="icon" class="w-8 h-8 text-orange-500 mb-4" />
    <h3 class="text-xl font-semibold text-white mb-2">{{ title }}</h3>
    <p class="text-gray-400">{{ description }}</p>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  description: String,
  icon: Object
})
</script>