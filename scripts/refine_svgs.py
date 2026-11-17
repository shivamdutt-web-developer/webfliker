# Update the SVG illustrations and styles in scripts/new_trans_section.html and styles.css

refined_legacy_svg = '''<svg class="trans-isometric-svg" viewBox="0 0 220 230" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="srvTopG" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#edf2f7"/>
                    </linearGradient>
                    <linearGradient id="srvFrontG" x1="0%" y1="0%" x2="0%" y2="100%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#e2e8f0"/>
                    </linearGradient>
                    <linearGradient id="srvSideG" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#cbd5e1"/>
                      <stop offset="100%" stop-color="#94a3b8"/>
                    </linearGradient>
                    <filter id="srvShadowRef" x="-20%" y="-10%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="10" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.14"/>
                    </filter>
                    <linearGradient id="warnTriGradRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#ff733b"/>
                      <stop offset="100%" stop-color="#ea3b16"/>
                    </linearGradient>
                    <filter id="warnGlowRef" x="-30%" y="-30%" width="160%" height="160%">
                      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#ea3b16" flood-opacity="0.55"/>
                    </filter>
                    <radialGradient id="wpSphereGradRef" cx="35%" cy="35%" r="65%">
                      <stop offset="0%" stop-color="#38a5df"/>
                      <stop offset="55%" stop-color="#21759b"/>
                      <stop offset="100%" stop-color="#11435d"/>
                    </radialGradient>
                    <filter id="wpShadowRef" x="-20%" y="-20%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#11435d" flood-opacity="0.4"/>
                    </filter>
                  </defs>

                  <!-- Server Blade 3 (Top) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,75 170,100 105,124 40,100" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,100 105,124 105,142 40,118" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,124 170,100 170,118 105,142" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <!-- Server LED Status Dots -->
                    <circle cx="62" cy="112" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="116" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="120" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Server Blade 2 (Middle) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,118 170,143 105,167 40,143" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,143 105,167 105,185 40,161" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,167 170,143 170,161 105,185" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <circle cx="62" cy="155" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="159" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="163" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Server Blade 1 (Bottom) -->
                  <g filter="url(#srvShadowRef)">
                    <polygon points="105,161 170,186 105,210 40,186" fill="url(#srvTopG)" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="40,186 105,210 105,226 40,202" fill="url(#srvFrontG)" stroke="#cbd5e1" stroke-width="1"/>
                    <polygon points="105,210 170,186 170,202 105,226" fill="url(#srvSideG)" stroke="#94a3b8" stroke-width="1"/>
                    <circle cx="62" cy="197" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="72" cy="201" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                    <circle cx="82" cy="205" r="2.5" fill="#ef4444" filter="drop-shadow(0 0 3px #ef4444)"/>
                  </g>

                  <!-- Floating 3D WordPress Logo Sphere on Top -->
                  <g class="floating-3d-node wp-node" filter="url(#wpShadowRef)">
                    <circle cx="105" cy="40" r="26" fill="url(#wpSphereGradRef)"/>
                    <ellipse cx="98" cy="27" rx="10" ry="5" fill="#ffffff" opacity="0.45" transform="rotate(-20 98 27)"/>
                    <!-- WordPress W Emblem -->
                    <circle cx="105" cy="40" r="19" stroke="#ffffff" stroke-width="2.2" fill="none" opacity="0.9"/>
                    <path d="M 94 33 L 100 50 L 105 38 L 110 50 L 116 33" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>

                  <!-- 3D Red Warning Triangle Badge in Front -->
                  <g class="floating-3d-node warn-node" filter="url(#warnGlowRef)">
                    <polygon points="152,156 190,218 114,218" fill="url(#warnTriGradRef)" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
                    <text x="152" y="210" font-size="24" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="system-ui, sans-serif">!</text>
                  </g>
                </svg>'''

refined_modern_svg = '''<svg class="trans-isometric-svg" viewBox="0 0 220 230" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <!-- Ambient Base Glow -->
                    <radialGradient id="baseOrangeGlowRef" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#ff7a18" stop-opacity="0.95"/>
                      <stop offset="50%" stop-color="#ff5e1e" stop-opacity="0.35"/>
                      <stop offset="100%" stop-color="#ff5e1e" stop-opacity="0"/>
                    </radialGradient>
                    <!-- LLM Glass Slab Gradient -->
                    <linearGradient id="llmTopGRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#361f1a"/>
                      <stop offset="100%" stop-color="#170d10"/>
                    </linearGradient>
                    <!-- WebGL 3D Glass Slab Gradient -->
                    <linearGradient id="webglTopGRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#132c4d"/>
                      <stop offset="100%" stop-color="#0a152e"/>
                    </linearGradient>
                    <!-- Next.js Dark Glass Slab Gradient -->
                    <linearGradient id="nextTopGRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#2d2d32"/>
                      <stop offset="100%" stop-color="#0d0d10"/>
                    </linearGradient>
                    <!-- Shopify Green Bag Gradient -->
                    <linearGradient id="shopifyBagGradRef" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#9dd345"/>
                      <stop offset="50%" stop-color="#72aa29"/>
                      <stop offset="100%" stop-color="#4e7d17"/>
                    </linearGradient>
                    <filter id="shopifyShadowRef" x="-25%" y="-20%" width="150%" height="150%">
                      <feDropShadow dx="0" dy="10" stdDeviation="8" flood-color="#84cc16" flood-opacity="0.55"/>
                    </filter>
                  </defs>

                  <!-- Base Radiant Ground Glow Ring -->
                  <ellipse cx="110" cy="195" rx="80" ry="24" fill="url(#baseOrangeGlowRef)"/>

                  <!-- Layer 1: LLM Graph (Bottom Slab) -->
                  <g class="tech-slab slab-llm">
                    <polygon points="110,158 178,181 110,204 42,181" fill="url(#llmTopGRef)" stroke="#ff7a18" stroke-width="1.8"/>
                    <polygon points="42,181 110,204 110,217 42,194" fill="#24130f" stroke="#ea580c" stroke-width="1.2"/>
                    <polygon points="110,204 178,181 178,194 110,217" fill="#140a08" stroke="#c2410c" stroke-width="1.2"/>
                    <!-- Icon & Label -->
                    <g transform="translate(74, 188)">
                      <circle cx="6" cy="3" r="2.2" fill="#ff7a18"/>
                      <circle cx="13" cy="8" r="1.8" fill="#ff7a18"/>
                      <circle cx="18" cy="2" r="2" fill="#ff7a18"/>
                      <line x1="6" y1="3" x2="13" y2="8" stroke="#ff7a18" stroke-width="1.2"/>
                      <line x1="13" y1="8" x2="18" y2="2" stroke="#ff7a18" stroke-width="1.2"/>
                      <text x="26" y="6" font-size="10" font-weight="700" fill="#ffedd5" font-family="system-ui, sans-serif">LLM Graph</text>
                    </g>
                  </g>

                  <!-- Layer 2: WebGL 3D (Middle Slab) -->
                  <g class="tech-slab slab-webgl">
                    <polygon points="110,116 178,139 110,162 42,139" fill="url(#webglTopGRef)" stroke="#38bdf8" stroke-width="1.8"/>
                    <polygon points="42,139 110,162 110,175 42,152" fill="#0c223c" stroke="#0284c7" stroke-width="1.2"/>
                    <polygon points="110,162 178,139 178,152 110,175" fill="#071526" stroke="#0369a1" stroke-width="1.2"/>
                    <!-- Cube Icon & Label -->
                    <g transform="translate(72, 146)">
                      <polygon points="11,0 18,3.5 11,7 4,3.5" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <polygon points="4,3.5 11,7 11,13 4,9.5" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <polygon points="11,7 18,3.5 18,9.5 11,13" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
                      <text x="26" y="9" font-size="10" font-weight="700" fill="#e0f2fe" font-family="system-ui, sans-serif">WebGL 3D</text>
                    </g>
                  </g>

                  <!-- Layer 3: Next.js (Upper Slab) -->
                  <g class="tech-slab slab-nextjs">
                    <polygon points="110,74 178,97 110,120 42,97" fill="url(#nextTopGRef)" stroke="#ffffff" stroke-width="1.8"/>
                    <polygon points="42,97 110,120 110,133 42,110" fill="#1c1c20" stroke="#a1a1aa" stroke-width="1.2"/>
                    <polygon points="110,120 178,97 178,110 110,133" fill="#0b0b0e" stroke="#71717a" stroke-width="1.2"/>
                    <!-- Next.js N Logo Badge & Label -->
                    <g transform="translate(74, 103)">
                      <circle cx="8" cy="5" r="7" fill="#000000" stroke="#ffffff" stroke-width="1"/>
                      <text x="5" y="8.5" font-size="8.5" font-weight="900" fill="#ffffff" font-family="system-ui, sans-serif">N</text>
                      <text x="23" y="9" font-size="10.5" font-weight="800" fill="#ffffff" font-family="system-ui, sans-serif">Next.js</text>
                    </g>
                  </g>

                  <!-- Floating 3D Shopify Plus Shopping Bag on Top -->
                  <g class="floating-3d-node shopify-bag-node" filter="url(#shopifyShadowRef)">
                    <!-- Bag Curved Handles -->
                    <path d="M 103 26 C 103 16, 117 16, 117 26" stroke="#f1f5f9" stroke-width="3" fill="none" stroke-linecap="round"/>
                    <!-- Bag Body Polygon with 3D Depth -->
                    <polygon points="94,26 126,26 131,58 89,58" fill="url(#shopifyBagGradRef)" stroke="#bbf7d0" stroke-width="1.2"/>
                    <polygon points="89,58 131,58 127,63 93,63" fill="#3b5e11"/>
                    <!-- Shopify S Leaf Monogram -->
                    <path d="M 107 35 C 107 33, 113 33, 114 36 C 115 40, 107 41, 107 46 C 107 49, 114 49, 114 47" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>
                  </g>
                </svg>'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Replace the legacy visual pane SVG
html = re.sub(
    r'<div class="trans-3d-visual-pane legacy-visual-pane">\s*<svg class="trans-isometric-svg"[\s\S]*?</svg>\s*</div>',
    f'<div class="trans-3d-visual-pane legacy-visual-pane">\n                {refined_legacy_svg}\n              </div>',
    html
)

# Replace the modern visual pane SVG
html = re.sub(
    r'<div class="trans-3d-visual-pane modern-visual-pane">\s*<svg class="trans-isometric-svg"[\s\S]*?</svg>\s*</div>',
    f'<div class="trans-3d-visual-pane modern-visual-pane">\n                {refined_modern_svg}\n              </div>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated SVGs in index.html!")
