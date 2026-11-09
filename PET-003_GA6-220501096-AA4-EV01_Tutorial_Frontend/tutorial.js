/**
 * TUTORIAL DIDÁCTICO DE FUNDAMENTOS FRONTEND (HTML, CSS Y JS)
 * Evidencia: GA6-220501096-AA4-EV01
 * Aprendiz: Karen Yuliana Campo | Ficha: 228118
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initScrollProgress();
  initSearch();
  initBackToTop();
  initTocHighlight();
  initSmoothScroll();
});

/* 1. MODO OSCURO / MODO CLARO (DARK / LIGHT THEME) */
function initTheme() {
  const toggleBtn = document.getElementById('themeToggleBtn');
  const themeIcon = document.getElementById('themeIcon');
  const themeText = document.getElementById('themeText');
  const body = document.body;

  // Cargar preferencia guardada
  const savedTheme = localStorage.getItem('tutorial-theme') || 'light';
  if (savedTheme === 'dark') {
    body.classList.remove('light-theme');
    body.classList.add('dark-theme');
    if (themeIcon) themeIcon.textContent = '☀️';
    if (themeText) themeText.textContent = 'Modo Claro';
    if (toggleBtn) toggleBtn.title = 'Cambiar a Modo Claro';
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const isDark = body.classList.contains('dark-theme');
      if (isDark) {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
        themeIcon.textContent = '🌙';
        themeText.textContent = 'Modo Oscuro';
        toggleBtn.title = 'Cambiar a Modo Oscuro';
        localStorage.setItem('tutorial-theme', 'light');
      } else {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
        themeIcon.textContent = '☀️';
        themeText.textContent = 'Modo Claro';
        toggleBtn.title = 'Cambiar a Modo Claro';
        localStorage.setItem('tutorial-theme', 'dark');
      }
    });
  }
}

/* 2. BARRA DE PROGRESO DE LECTURA (SCROLL PROGRESS) */
function initScrollProgress() {
  const progressBar = document.getElementById('scrollProgressBar');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = `${progress}%`;
    progressBar.setAttribute('aria-valuenow', Math.round(progress));
  }, { passive: true });
}

/* 3. BÚSQUEDA Y FILTRADO EN TIEMPO REAL DE TEMAS */
function initSearch() {
  const searchInput = document.getElementById('topicSearch');
  const countLabel = document.getElementById('searchResultsCount');
  const cards = document.querySelectorAll('.tema-card');

  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase().trim();
    let visibleCount = 0;

    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      const match = text.includes(term);
      if (match) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (term.length > 0) {
      countLabel.textContent = `${visibleCount} de ${cards.length} temas coincidentes`;
    } else {
      countLabel.textContent = '';
    }
  });
}

/* 4. RESALTADO DEL ÍNDICE ACTIVO AL HACER SCROLL */
function initTocHighlight() {
  const links = document.querySelectorAll('.toc-link');
  const sections = document.querySelectorAll('.tema-card');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 120;

    sections.forEach(sec => {
      if (sec.offsetTop <= scrollPos && sec.offsetTop + sec.offsetHeight > scrollPos) {
        current = sec.getAttribute('id');
      }
    });

    links.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }, { passive: true });
}

/* 5. NAVEGACIÓN SUAVE CON COMPENSACIÓN DE ENCABEZADO */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* 6. BOTÓN FLOTANTE "VOLVER ARRIBA" */
function initBackToTop() {
  const btn = document.getElementById('backToTopBtn');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.style.display = 'flex';
    } else {
      btn.style.display = 'none';
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* 7. COPIAR CÓDIGO AL PORTAPAPELES */
window.copiarSnippet = function(button) {
  const wrapper = button.closest('.code-snippet-wrapper');
  if (!wrapper) return;
  const code = wrapper.querySelector('code');
  if (!code) return;

  const textToCopy = code.innerText;
  navigator.clipboard.writeText(textToCopy).then(() => {
    const originalText = button.textContent;
    button.textContent = '✔ ¡Copiado!';
    button.classList.add('copied');
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove('copied');
    }, 2000);
  }).catch(() => {
    button.textContent = 'Error al copiar';
  });
};
