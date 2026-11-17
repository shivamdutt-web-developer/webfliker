css_rules = '''
/* ========================================================================= */
/* PHOTOREAL 3D ARCHITECTURE VISUAL COMPONENT STYLES                         */
/* ========================================================================= */
.photoreal-3d-wrap {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: transform 0.4s cubic-bezier(0.2, 0, 0.2, 1);
}
.photoreal-3d-img {
  width: 100%;
  max-width: 240px;
  height: auto;
  display: block;
  object-fit: contain;
  filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.1));
  transition: transform 0.4s ease, filter 0.4s ease;
}
.legacy-3d-img {
  max-width: 250px;
}
.modern-3d-img {
  max-width: 195px;
  filter: drop-shadow(0 15px 35px rgba(255, 122, 24, 0.25)) drop-shadow(0 10px 20px rgba(16, 185, 129, 0.2));
}

.trans-card-legacy:hover .legacy-3d-img {
  transform: scale(1.04) translateY(-4px);
  filter: drop-shadow(0 20px 35px rgba(239, 68, 68, 0.2));
}

.trans-card-modern:hover .modern-3d-img {
  transform: scale(1.05) translateY(-4px);
  filter: drop-shadow(0 20px 45px rgba(255, 122, 24, 0.4)) drop-shadow(0 15px 25px rgba(16, 185, 129, 0.3));
}

/* Floating micro-animations */
.floating-3d-legacy {
  animation: floatLegacyServer 5s ease-in-out infinite;
}
@keyframes floatLegacyServer {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-7px) rotate(-0.5deg); }
}

.floating-3d-modern {
  animation: floatModernTech 4.5s ease-in-out infinite;
}
@keyframes floatModernTech {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-7px) rotate(0.8deg); }
}

/* Photoreal 3D Toruses */
.bg-torus-img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  filter: drop-shadow(0 20px 30px rgba(234, 88, 12, 0.3));
}
.torus-img-left {
  width: 130px;
}
.torus-img-right {
  width: 140px;
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_rules)

print("Appended photoreal 3D CSS to styles.css successfully!")
