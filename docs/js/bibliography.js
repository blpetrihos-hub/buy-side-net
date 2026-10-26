(() => {
  const nav = document.querySelector(".bib-jump");
  if (!nav) return;
  const links = [...nav.querySelectorAll("a[href^='#layer-']")];
  if (!links.length) return;

  const sections = links
    .map((a) => document.querySelector(a.getAttribute("href")))
    .filter(Boolean);

  function setActive(id) {
    links.forEach((a) => {
      const on = a.getAttribute("href") === "#" + id;
      a.classList.toggle("is-active", on);
      if (on) a.setAttribute("aria-current", "location");
      else a.removeAttribute("aria-current");
    });
  }

  const io = new IntersectionObserver(
    (entries) => {
      const hit = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (hit) setActive(hit.target.id);
    },
    { rootMargin: "-15% 0px -70% 0px", threshold: [0, 0.15, 0.4] }
  );
  sections.forEach((s) => io.observe(s));
})();
