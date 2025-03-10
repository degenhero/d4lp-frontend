<template>
  <div class="glass-effect rounded-xl overflow-hidden">
    <!-- Terminal Header -->
    <div class="bg-black/50 p-4 flex items-center">
      <div class="flex space-x-2">
        <div class="w-3 h-3 rounded-full bg-red-500"></div>
        <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
        <div class="w-3 h-3 rounded-full bg-green-500"></div>
      </div>
      <div class="text-gray-400 text-sm ml-4">HydraCurve™ Demo</div>
    </div>

    <!-- Terminal Content -->
    <div class="p-6 font-mono text-sm">
      <div v-for="(line, index) in terminalLines" :key="index" class="mb-2">
        <div class="flex items-start">
          <span class="text-orange-500 mr-2">$</span>
          <div>
            <div class="text-gray-300">{{ line.command }}</div>
            <div 
              v-if="line.response" 
              class="text-gray-400 mt-1"
              v-html="line.response"
            ></div>
          </div>
        </div>
      </div>

      <!-- Typing Effect -->
      <div class="flex items-center">
        <span class="text-orange-500 mr-2">$</span>
        <div class="flex items-center">
          <span class="text-gray-300">{{ currentCommand }}</span>
          <span class="w-2 h-5 bg-orange-500 ml-1 animate-pulse"></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const terminalLines = ref([
  {
    command: 'connect wallet',
    response: '✓ Wallet connected successfully'
  },
  {
    command: 'check balance',
    response: 'ETH: 1.5234<br>USDC: 5000.00'
  },
  {
    command: 'hydra swap 1000 USDC to ETH',
    response: '⚡ Calculating optimal route...<br>✓ Best price: 0.4123 ETH<br>✓ Slippage: 0.05%'
  }
])

const commands = [
  'view pool stats',
  'check rewards',
  'claim yield',
  'optimize position'
]

const currentCommand = ref('')
let currentIndex = 0
let charIndex = 0

const typeCommand = () => {
  if (charIndex < commands[currentIndex].length) {
    currentCommand.value = commands[currentIndex].substring(0, charIndex + 1)
    charIndex++
    setTimeout(typeCommand, 100)
  } else {
    setTimeout(() => {
      currentCommand.value = ''
      charIndex = 0
      currentIndex = (currentIndex + 1) % commands.length
      typeCommand()
    }, 2000)
  }
}

onMounted(() => {
  typeCommand()
})
</script>