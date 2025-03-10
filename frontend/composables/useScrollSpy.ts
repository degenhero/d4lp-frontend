import { ref, onMounted, onUnmounted } from "vue";

export function useScrollSpy(sectionIds: string[]) {
  const activeSection = ref("");

  const onScroll = () => {
    const scrollPosition = window.scrollY + 200; // Offset for better activation
    for (const id of sectionIds) {
      const section = document.getElementById(id);
      if (section && section.offsetTop <= scrollPosition) {
        activeSection.value = id;
      }
    }
  };

  onMounted(() => window.addEventListener("scroll", onScroll));
  onUnmounted(() => window.removeEventListener("scroll", onScroll));

  return { activeSection };
}
