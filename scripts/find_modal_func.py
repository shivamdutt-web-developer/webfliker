with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'function\s+initProposalModal', text)
print("Function definitions for initProposalModal:", len(m))
