<template>
  <div class="glass-effect p-6 rounded-xl hover:scale-105 transition-transform">
    <div class="flex items-center mb-4">
      <img 
        :src="avatar" 
        :alt="name"
        class="w-12 h-12 rounded-full border-2 border-orange-500"
      />
      <div class="ml-4">
        <h4 class="text-white font-semibold">{{ name }}</h4>
        <p class="text-gray-400 text-sm">{{ role }}</p>
      </div>
    </div>
    <blockquote class="relative">
      <span class="text-orange-500 text-4xl absolute -top-4 -left-2">"</span>
      <p class="text-gray-300 italic pl-6">{{ quote }}</p>
    </blockquote>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  role: String,
  quote: String,
  avatar: String
})
</script>