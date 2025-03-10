<template>
  <div class="glass-effect p-8 rounded-xl max-w-2xl mx-auto">
    <div class="flex justify-between items-center mb-6">
      <h3 class="text-2xl font-bold text-white">Whitepaper</h3>
      <button 
        @click="downloadWhitepaper"
        class="flex items-center gap-2 px-4 py-2 bg-orange-500 rounded-lg hover:bg-orange-600 transition"
      >
        <Download class="w-4 h-4" />
        Download PDF
      </button>
    </div>
    
    <!-- Preview Pages -->
    <div class="grid grid-cols-2 gap-4 mb-6">
      <div v-for="i in 4" :key="i" class="aspect-[3/4] bg-white/5 rounded-lg p-4">
        <div class="h-2 bg-white/20 rounded mb-2 w-3/4"></div>
        <div class="h-2 bg-white/20 rounded mb-2"></div>
        <div class="h-2 bg-white/20 rounded mb-2 w-1/2"></div>
        <div class="h-20 bg-white/10 rounded my-4"></div>
        <div class="h-2 bg-white/20 rounded mb-2"></div>
        <div class="h-2 bg-white/20 rounded mb-2 w-2/3"></div>
      </div>
    </div>

    <!-- Quick Stats -->
    <div class="grid grid-cols-3 gap-4 text-center">
      <div>
        <div class="text-orange-500 text-2xl font-bold">45</div>
        <div class="text-gray-400 text-sm">Pages</div>
      </div>
      <div>
        <div class="text-orange-500 text-2xl font-bold">12</div>
        <div class="text-gray-400 text-sm">Diagrams</div>
      </div>
      <div>
        <div class="text-orange-500 text-2xl font-bold">5</div>
        <div class="text-gray-400 text-sm">Chapters</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Download } from '../utils/icons'

const downloadWhitepaper = () => {
  console.log('Downloading whitepaper...')
}
</script>
