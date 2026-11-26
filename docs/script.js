// Highlight the current section in the navigation bar
const links = [...document.querySelectorAll('nav a')];
const secs = links.map(a => document.querySelector(a.getAttribute('href')));
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) links.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
}), {rootMargin: '-40% 0px -55% 0px'});
secs.forEach(s => s && io.observe(s));

// Show / hide the data table
const btn = document.getElementById('toggle-data'), box = document.getElementById('data-box');
btn.addEventListener('click', () => {
  const hidden = box.hasAttribute('hidden');
  hidden ? box.removeAttribute('hidden') : box.setAttribute('hidden', '');
  btn.textContent = hidden ? 'Hide the data table' : 'Show the data table (2010–2025)';
});
