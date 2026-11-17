js_snippet = '''
/* ========================================================================= */
/* TRANSFORMATION SHOWCASE INTERACTIVE SWITCHER                              */
/* ========================================================================= */
function initTransformationSwitcher() {
  const btnSplit = document.getElementById('btnViewSplit');
  const btnLegacy = document.getElementById('btnViewLegacy');
  const btnModern = document.getElementById('btnViewModern');
  const cardLegacy = document.getElementById('cardLegacy');
  const cardModern = document.getElementById('cardModern');
  const grid = document.getElementById('transCardsGrid');

  if (!btnSplit || !btnLegacy || !btnModern || !cardLegacy || !cardModern || !grid) return;

  function setActiveTab(activeBtn) {
    [btnSplit, btnLegacy, btnModern].forEach(b => b.classList.remove('active'));
    activeBtn.classList.add('active');
  }

  btnSplit.addEventListener('click', () => {
    setActiveTab(btnSplit);
    cardLegacy.style.display = 'flex';
    cardModern.style.display = 'flex';
    grid.style.gridTemplateColumns = 'repeat(2, minmax(0, 1fr))';
  });

  btnLegacy.addEventListener('click', () => {
    setActiveTab(btnLegacy);
    cardLegacy.style.display = 'flex';
    cardModern.style.display = 'none';
    grid.style.gridTemplateColumns = '1fr';
  });

  btnModern.addEventListener('click', () => {
    setActiveTab(btnModern);
    cardLegacy.style.display = 'none';
    cardModern.style.display = 'flex';
    grid.style.gridTemplateColumns = '1fr';
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initTransformationSwitcher();
});
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initTransformationSwitcher();
}
'''

with open('app.js', 'a', encoding='utf-8') as f:
    f.write(js_snippet)

print("Appended switcher JS to app.js")
