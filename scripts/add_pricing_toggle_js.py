with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pricing_toggle_js = '''
// Interactive Pricing Billing Switcher (Monthly vs Quarterly Retainer)
function initPricingBillingToggle() {
  const toggleBtn = document.getElementById('pricingToggleBtn');
  const labelMonthly = document.getElementById('labelMonthly');
  const labelQuarterly = document.getElementById('labelQuarterly');
  const priceElements = document.querySelectorAll('.price-amount');
  if (!toggleBtn || !priceElements.length) return;

  let isQuarterly = false;

  function updatePrices(quarterly) {
    isQuarterly = quarterly;
    toggleBtn.classList.toggle('active', isQuarterly);
    if (labelMonthly) labelMonthly.classList.toggle('active', !isQuarterly);
    if (labelQuarterly) labelQuarterly.classList.toggle('active', isQuarterly);

    priceElements.forEach(el => {
      const val = isQuarterly ? el.getAttribute('data-quarterly') : el.getAttribute('data-monthly');
      if (val) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(-4px)';
        setTimeout(() => {
          el.textContent = val;
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, 150);
      }
    });
  }

  toggleBtn.addEventListener('click', () => updatePrices(!isQuarterly));
  if (labelMonthly) labelMonthly.addEventListener('click', () => updatePrices(false));
  if (labelQuarterly) labelQuarterly.addEventListener('click', () => updatePrices(true));
}

// Call on DOMContentLoaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPricingBillingToggle);
} else {
  initPricingBillingToggle();
}
'''

if 'initPricingBillingToggle' not in js:
    js += pricing_toggle_js
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('Appended initPricingBillingToggle to app.js!')
else:
    print('Already present in app.js')
