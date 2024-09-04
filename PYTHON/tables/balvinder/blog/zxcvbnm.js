gsap.from(".vector-line", {
  duration: 10,
  opacity: 0,
  stagger: 0.2,
  ease: "elastic",
  yoyo: true,
  repeat: -1
});

gsap.from(".vector-line", {
  stagger: 0.2,
  duration: 5,
  rotate: 300,
  transformOrigin: "center",
  yoyo: true,
  repeat: -5
});
