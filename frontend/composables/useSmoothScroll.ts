

export function useSmoothScroll() {
  useEventListener("click", (event: { target: HTMLElement; preventDefault: () => void; }) => {
    const target = event.target as HTMLElement;
    if (target.tagName === "A" && target.getAttribute("href")?.startsWith("#")) {
      event.preventDefault();
      const id = target.getAttribute("href")?.substring(1);
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }
  });
}
