import os, re

for fname in os.listdir('.'):
    if fname.endswith('.js') or fname.endswith('.py'):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'initProposalModal' in content and fname != 'app.js':
                    print(f"Found initProposalModal in {fname}")
                if 'initPricingToggle' in content and fname != 'app.js':
                    print(f"Found initPricingToggle in {fname}")
                if 'initPortfolioFilters' in content and fname != 'app.js':
                    print(f"Found initPortfolioFilters in {fname}")
        except Exception:
            pass
