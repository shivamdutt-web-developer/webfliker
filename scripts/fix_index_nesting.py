with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the messy boundary
target = '''            </div>

          </div>
        </div>
    </div>
  </footer>

  <script src="app.js?v=1794771344"></script>
</body>'''

replacement = '''            </div>

          </div>
        </div>
      </div>
    </div>
  </section>'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed hero section nesting and removed rogue footer/body tags!")
else:
    # Try more flexible whitespace replacement
    import re
    pattern = r'</div>\s*</div>\s*</div>\s*</div>\s*</footer>\s*<script[^>]*></script>\s*</body>'
    m = re.search(pattern, text)
    if m:
        text = text[:m.start()] + '</div>\n        </div>\n      </div>\n    </div>\n  </section>' + text[m.end():]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Fixed hero section nesting via regex!")
    else:
        print("Could not match target boundary!")
