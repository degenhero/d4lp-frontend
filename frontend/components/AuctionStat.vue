<template>
  <div class="glass-effect p-6 rounded-xl text-center">
    <div class="text-gray-400 text-sm mb-2">{{ label }}</div>
    <div :class="['text-2xl font-bold', highlight ? 'text-orange-500' : 'text-white']">
      {{ value }}
    </div>
    <div v-if="trend" :class="[
      'text-sm mt-2',
      trend.startsWith('+') ? 'text-green-500' : 'text-red-500'
    ]">
      {{ trend }}
    </div>
  </div>
</template>

<script setup>
defineProps({
  label: String,
  value: String,
  trend: String,
  highlight: Boolean
})
</script>