# docs/conf.py
project = "半導体の製造工程と関連企業 — 補助ドキュメント"
author = "eleshis"
release = "2026-07-18"
language = "ja"

extensions = ["myst_parser", "sphinx_oceanid"]
myst_enable_extensions = ["colon_fence", "deflist", "attrs_block", "attrs_inline"]

# spec/plan（メタ資料）はドキュメントビルド対象外
exclude_patterns = ["_build", "superpowers/**", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "半導体 補助ドキュメント"
