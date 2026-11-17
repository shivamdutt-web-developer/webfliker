with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

missing_funcs = '''
/* ========================================================================= */
/* MULTI-STEP PROPOSAL MODAL, PRICING TOGGLE, & PORTFOLIO FILTER HANDLERS    */
/* ========================================================================= */
function initProposalModal() {
  const modal = document.getElementById('proposalModal');
  const triggers = document.querySelectorAll('[data-open-proposal], .open-proposal-btn, a[href="#proposalModal"]');
  const closeBtns = document.querySelectorAll('.close-modal-btn, [data-close-modal]');

  if (!modal) return;

  triggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    });
  });

  closeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    });
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  });
}

function initPricingToggle() {
  const toggle = document.getElementById('billingToggle') || document.querySelector('.pricing-billing-toggle');
  const priceElements = document.querySelectorAll('[data-monthly-price][data-annual-price]');
  if (!toggle) return;

  toggle.addEventListener('change', () => {
    const isAnnual = toggle.checked;
    priceElements.forEach(el => {
      const price = isAnnual ? el.getAttribute('data-annual-price') : el.getAttribute('data-monthly-price');
      if (price) el.textContent = price;
    });
  });
}

function initPortfolioFilters() {
  const filterBtns = document.querySelectorAll('.portfolio-filter-btn, .work-filter-btn');
  const projectCards = document.querySelectorAll('.project-card, .case-study-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter') || 'all';
      projectCards.forEach(card => {
        const cat = card.getAttribute('data-category') || '';
        if (filter === 'all' || cat.includes(filter)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
'''

# Append at the bottom of app.js
if 'function initProposalModal()' not in js:
    js += '\n' + missing_funcs
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Successfully added missing modal, pricing, and filter functions to app.js")
else:
    print("Functions already present")
