# slides/conf.py
project = "半導体の製造工程と関連企業"
author = "eleshis"
release = "2026-07-18"
language = "ja"

extensions = [
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.sass",
    "sphinx_oceanid",
]

myst_enable_extensions = ["colon_fence", "deflist", "attrs_block", "attrs_inline"]

# 部ファイルは index.md に {include} で統合する単一デッキ構成（重要）。
# 部ファイルを単独ドキュメントとしてビルドさせない（＝別々のプレゼンHTMLを作らせない）ため除外する。
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store",
    "00-intro.md", "01-design.md", "02-frontend.md", "03-backend.md", "04-industry.md",
]

revealjs_static_path = ["_static"]
revealjs_style_theme = "solarized"
revealjs_script_conf = {
    "width": 1280,
    "height": 720,
    "slideNumber": "c/t",
    "hash": True,
}
# sphinx_revealjs.ext.sass が _static 配下の .scss を同名 .css にコンパイルする（custom.scss→custom.css）。
# ハイライトテーマCSSは必須（可視化のため）。_static/css/highlight.css に配置して読み込む。
revealjs_css_files = ["custom.css", "css/highlight.css"]
