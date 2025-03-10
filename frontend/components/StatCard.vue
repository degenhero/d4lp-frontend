<template>
  <div class="glass-effect p-6 rounded-xl">
    <component :is="icon" class="w-8 h-8 text-orange-500 mx-auto mb-4" />
    <div class="text-3xl font-bold text-white">{{ number }}</div>
    <div class="text-gray-400 text-sm mt-2">{{ label }}</div>
  </div>
</template>

<script setup>
defineProps({
  number: String,
  label: String,
  icon: Object
})
</script>