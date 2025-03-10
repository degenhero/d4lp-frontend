<template>
  <form @submit.prevent="handleSubmit" class="glass-effect p-8 rounded-xl">
    <div class="space-y-6">
      <!-- Name Input -->
      <div>
        <label class="block text-gray-300 mb-2">Name</label>
        <input 
          v-model="formData.name"
          type="text"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          placeholder="Enter your name"
        />
      </div>

      <!-- Email Input -->
      <div>
        <label class="block text-gray-300 mb-2">Email</label>
        <input 
          v-model="formData.email"
          type="email"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          placeholder="Enter your email"
        />
      </div>

      <!-- Interest Selection -->
      <div>
        <label class="block text-gray-300 mb-2">I'm interested in</label>
        <select 
          v-model="formData.interest"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
        >
          <option value="trading">Trading</option>
          <option value="liquidity">Providing Liquidity</option>
          <option value="development">Development</option>
          <option value="partnership">Partnership</option>
        </select>
      </div>

      <!-- Message Input -->
      <div>
        <label class="block text-gray-300 mb-2">Message</label>
        <textarea 
          v-model="formData.message"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          rows="4"
          placeholder="Your message here..."
        ></textarea>
      </div>

      <!-- Submit Button -->
      <button 
        type="submit"
        class="w-full bg-gradient-to-r from-purple-500 to-orange-500 text-white py-3 rounded-lg font-semibold hover:opacity-90 transition flex items-center justify-center gap-2"
      >
        <Send class="w-4 h-4" />
        Send Message
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { Send } from '../utils/icons'

const formData = ref({
  name: '',
  email: '',
  interest: 'trading',
  message: ''
})

const handleSubmit = () => {
  console.log('Form submitted:', formData.value)
}
</script>
