css_rules = '''
/* ========================================================================= */
/* SEAMLESS 3D FLAGSHIP PHONE (ZERO RECTANGULAR BOX EDGES - MOBIKASA GRADE)  */
/* ========================================================================= */
.phone-3d-chassis-seamless {
  position: relative !important;
  width: 330px !important;
  max-width: 100% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
  transform-style: preserve-3d !important;
  will-change: transform !important;
  z-index: 2 !important;
}

.mobikasa-flagship-phone-img {
  width: 100% !important;
  height: auto !important;
  max-height: 560px !important;
  object-fit: contain !important;
  display: block !important;
  background: transparent !important;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  filter: drop-shadow(0 35px 55px rgba(0, 0, 0, 0.45)) 
          drop-shadow(0 15px 30px rgba(255, 94, 30, 0.22)) !important;
  pointer-events: none !important;
  user-select: none !important;
  transform-style: preserve-3d !important;
}

/* Mobikasa Signature Frosted Card (Bottom-Left Overlapping Phone) */
.mobikasa-signature-card {
  bottom: 25px !important;
  left: -35px !important;
  width: 260px !important;
  padding: 20px 22px !important;
  background: rgba(13, 18, 30, 0.88) !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  border: 1px solid rgba(255, 255, 255, 0.18) !important;
  border-radius: 22px !important;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45), 0 0 35px rgba(255, 94, 30, 0.16) !important;
  z-index: 8 !important;
  text-align: left !important;
}

.mobi-card-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 12px !important;
}

.mobi-icon-box {
  width: 36px !important;
  height: 36px !important;
  border-radius: 10px !important;
  background: rgba(255, 94, 30, 0.18) !important;
  border: 1px solid rgba(255, 94, 30, 0.35) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.mobi-arrow-btn {
  width: 28px !important;
  height: 28px !important;
  border-radius: 50% !important;
  background: rgba(255, 255, 255, 0.08) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all 0.2s ease !important;
}
.mobikasa-signature-card:hover .mobi-arrow-btn {
  background: #ff5e1e !important;
  transform: translate(2px, -2px) !important;
}

.mobi-card-title,
body.theme-light .mobi-card-title {
  font-size: 1.05rem !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  margin: 0 0 6px !important;
  line-height: 1.25 !important;
}

.mobi-card-desc,
body.theme-light .mobi-card-desc {
  font-size: 0.78rem !important;
  color: #94a3b8 !important;
  line-height: 1.45 !important;
  margin: 0 0 12px !important;
}

.mobi-card-tags {
  display: flex !important;
  gap: 8px !important;
}

.mobi-tag {
  font-size: 0.68rem !important;
  font-weight: 700 !important;
  padding: 4px 10px !important;
  border-radius: 999px !important;
  letter-spacing: 0.02em !important;
}
.tag-cyan {
  background: rgba(56, 189, 248, 0.15) !important;
  color: #38bdf8 !important;
  border: 1px solid rgba(56, 189, 248, 0.3) !important;
}
.tag-emerald {
  background: rgba(16, 185, 129, 0.15) !important;
  color: #10b981 !important;
  border: 1px solid rgba(16, 185, 129, 0.3) !important;
}

@media (max-width: 768px) {
  .mobikasa-signature-card {
    position: relative !important;
    bottom: auto !important;
    left: auto !important;
    width: 100% !important;
    margin-top: 18px !important;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_rules)

print("Appended seamless phone CSS to styles.css")
