/*FONDO DE ESTRELLAS*/

tsParticles.load("tsparticles", {
  background: {
    color: {
      value: "transparent" // ← fondo transparente
    }
  },
  backgroundMode: {
    enable: true,
    zIndex: 0
  },
  particles: {
    number: {
      value: 355,
      density: {
        enable: true,
        value_area: 789.1476416322727
      }
    },
    color: {
      value: "#ffffff"
    },
    shape: {
      type: "circle"
    },
    opacity: {
      value: 0.48,
      anim: {
        enable: true,
        speed: 0.2,
        opacity_min: 0
      }
    },
    size: {
      value: 2,
      random: true,
      anim: {
        enable: true,
        speed: 2,
        size_min: 0
      }
    },
    line_linked: {
      enable: false
    },
    move: {
      enable: true,
      speed: 0.2,
      random: true,
      out_mode: "out"
    }
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: {
        enable: true,
        mode: "bubble"
      },
      onclick: {
        enable: true,
        mode: "push"
      },
      resize: true
    },
    modes: {
      bubble: {
        distance: 80,
        size: 1,
        duration: 3,
        opacity: 1,
        speed: 3
      },
      push: {
        particles_nb: 4
      }
    }
  },
  retina_detect: true
});
