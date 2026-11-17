additional_css = '''
/* High-Contrast Typography & Sizing Fixes for Transformation Section */
.trans-card-modern .trans-card-title,
.trans-card-modern h3,
body.theme-light .trans-card-modern .trans-card-title,
body.theme-light .trans-card-modern h3 {
  color: #ffffff !important;
  font-size: 1.55rem !important;
  font-weight: 800 !important;
  line-height: 1.3 !important;
  margin: 0 0 8px !important;
}

.trans-card-modern .trans-card-desc,
.trans-card-modern p,
body.theme-light .trans-card-modern .trans-card-desc,
body.theme-light .trans-card-modern p {
  color: #94a3b8 !important;
  font-size: 0.94rem !important;
  line-height: 1.6 !important;
  margin: 0 0 16px !important;
}

.trans-card-legacy .trans-card-title,
.trans-card-legacy h3,
body.theme-light .trans-card-legacy .trans-card-title,
body.theme-light .trans-card-legacy h3 {
  color: #0f172a !important;
  font-size: 1.55rem !important;
  font-weight: 800 !important;
  line-height: 1.3 !important;
  margin: 0 0 8px !important;
}

.trans-card-legacy .trans-card-desc,
.trans-card-legacy p,
body.theme-light .trans-card-legacy .trans-card-desc,
body.theme-light .trans-card-legacy p {
  color: #475569 !important;
  font-size: 0.94rem !important;
  line-height: 1.6 !important;
  margin: 0 0 16px !important;
}

.trans-card-inner-split {
  grid-template-columns: 210px 1fr !important;
  gap: 22px !important;
}

.trans-isometric-svg {
  max-height: 230px !important;
}

/* Enhanced 3D Podium Disc Platform */
.trans-stage-pedestal {
  position: absolute;
  bottom: -24px;
  left: 50%;
  transform: translateX(-50%);
  width: 98%;
  max-width: 1180px;
  height: 52px;
  pointer-events: none;
  z-index: 1;
}
.pedestal-disc-surface {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: linear-gradient(180deg, #fbeee7 0%, #f4d5ca 70%, #edd0c4 100%);
  border: 2px solid rgba(255, 140, 100, 0.4);
  box-shadow: 0 35px 70px rgba(235, 120, 80, 0.22), 0 12px 30px rgba(15, 23, 42, 0.1);
}
.pedestal-disc-bevel {
  position: absolute;
  bottom: -6px;
  left: 3%;
  right: 3%;
  height: 14px;
  border-radius: 999px;
  background: linear-gradient(180deg, #dfb4a4 0%, #cd9c8b 100%);
  opacity: 0.6;
  filter: blur(2px);
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(additional_css)

print("Successfully appended refined styles to styles.css!")
