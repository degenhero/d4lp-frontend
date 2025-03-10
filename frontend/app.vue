
 <template>
  <div>
    <NuxtLayout>
      <NuxtPage />
      <ScrollToTop />
    </NuxtLayout>
  </div>
</template>


<script setup>
import { useSmoothScroll } from "~/composables/useSmoothScroll";

useSmoothScroll();
</script>
