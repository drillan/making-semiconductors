# 半導体の製造工程と関連企業スライド 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** solarized テーマの sphinx-revealjs で半導体バリューチェーンを企業・シェア付きで解説する約43枚のスライド（`slides/`）と、その深掘り・出典・用語集を収めた Furo の補助ドキュメント（`docs/`）を作る。

**Architecture:** **2つのSphinxプロジェクト**に分離する。`slides/` はプレゼン本体（sphinx-revealjs, solarized, MyST を部ごと5ファイル分割）。`docs/` は通常のHTMLドキュメント（Furo）で、各部の詳細ページ・データ出典/確度一覧・用語集を置き、スライドが深掘りを委譲する。既存 `docs/superpowers/**`（spec/plan）は docs ビルドの `exclude_patterns` で除外。

**Tech Stack:** Python (uv), Sphinx, sphinx-revealjs, sphinx-revealjs.ext.sass, sphinx-oceanid (Mermaid), Furo, MyST。

**Content source of truth:** すべてのスライド／詳細ページの内容・企業・数値・出典方針は
`docs/superpowers/specs/2026-07-18-semiconductor-slides-design.md`（特に §3 構成、§5 確度区分、§6 2プロジェクト構成、付録A 企業/数値リスト）、および `research/2026-07-18-semiconductor-gaps-research.md` に定義済み。本計画はそれを重複させず参照する。

## Global Constraints

- **2プロジェクト**：スライド本体＝`slides/`、補助ドキュメント＝`docs/`（spec §6）
- スライドテーマ＝**solarized**（`revealjs_style_theme = "solarized"`）。docs テーマ＝**Furo**
- スライド構造は見出し階層：`#`=タイトル / `##`=部区切り / `###`=個別スライド（spec §6.1）
- **単一デッキ**：sphinx-revealjs はソース文書1つにつきプレゼンHTMLを1つ生成する。よって
  `slides/index.md` に各部を `{include}` で統合し、部ファイルは `exclude_patterns` で単独ビルドを
  抑止して**1つの43枚デッキ**にする。`#` は index.md のタイトルスライド専用（部ファイルは `##` 始まり）
- MyST ディレクティブは**コロンフェンス `:::`**（revealjs-authoring 規約）。span属性は `[語]{.class}`
- **list-table は最大3列厳守**。4項目以上は属性統合か2枚分割（spec §4）
- 図は Mermaid（sphinx-oceanid のサポート型：flowchart / sequence / class / state / er / xychart-beta 等）
- **出典はMyST脚注を使わない**。各スライド末尾に小文字の出典行＋CSSクラス `.source`、数値の隣に取得年。
  **完全な出典URL一覧は docs の `sources` ページに集約**し、スライド出典行は要約＋docs導線に留める（spec §4/§5）
- 工程色は **solarized アクセント**：設計=青`#268bd2` / 前工程=緑`#859900` / 後工程=橙`#cb4b16` / 素材=菫`#6c71c4`。
  日本企業はバッジ強調（CSSクラスで実装、spec §4/§6.1）
- 数値の**確度区分を厳守**（spec §5）：確度高＝断定可 / 概況＝「約」「〜年時点」で丸め。
  再確認対象（AMATイオン注入%、KLA指標、京セラEMC買収、Heraeus%）は数値を断定しない
- 断定禁止：熱処理・ALDの企業別シェア序列（spec §7）。荏原CMP2位・KOKUSAI単独序列は「概況」扱い
- 各コンテンツタスクは該当プロジェクトのビルドが**警告・エラーなく**通ることを完了条件に含める
  （slides: `uv run make -C slides revealjs` / docs: `uv run make -C docs html`）
- コミットはタスク単位。メッセージ末尾に `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`

---

### Task 1: `slides/` 雛形（sphinx-revealjs + solarized ビルドが通る最小構成）

**Files:**
- Create: `pyproject.toml`（uv 管理、リポジトリ共通）
- Create: `slides/conf.py`, `slides/index.md`, `slides/Makefile`
- Create: `.gitignore`

**Interfaces:**
- Produces: ビルド `uv run make -C slides revealjs` → `slides/_build/revealjs/index.html`、
  ソースルート `slides/`、toctree ルート `slides/index.md`

> 注：`revealjs-init` スキルは既定で `docs/` に雛形を作るが、本構成では `docs/` を補助ドキュメントに充てる
> ため使わず手動スキャフォールドする。sass拡張・ハイライトCSS・プラグインの設定キー名で迷ったら
> `revealjs-config` スキルで補正（目標状態は下記）。

- [ ] **Step 1: uv プロジェクト初期化と依存追加**

```bash
cd /home/driller/repo/making-semiconductors
uv init --no-workspace --name making-semiconductors --python 3.12
rm -f main.py hello.py            # uv init が生成するサンプルファイルを削除
uv add sphinx myst-parser sphinx-revealjs sphinx-oceanid libsass furo
uv add --dev sphinx-autobuild     # 両 Makefile の livehtml ターゲット用
```

Expected: `pyproject.toml` と `uv.lock` が生成される。`myst-parser` は両 conf.py が
`extensions` に指定するため必須（欠けると Step 7 のビルドが即失敗）。furo は Task 10 の docs、
sphinx-autobuild は livehtml で使用。

- [ ] **Step 2: `slides/conf.py` を作成**

```python
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
```

> 単一デッキの要：sphinx-revealjs は**ソース文書1つにつきプレゼンHTMLを1つ**生成する。よって
> toctree で5文書を並べると5つの別デッキになる。`index.md` に各部を `{include}` で取り込み、
> 部ファイルは上記 `exclude_patterns` で単独ビルドを抑止して、**1つの43枚デッキ**にする。

- [ ] **Step 3: `slides/index.md`（単一デッキのルート、include統合）を作成**

`#` がタイトルスライドになり、各部ファイルを `{include}`（コロンフェンス＋`:parser: myst`）で
取り込んで**1つのデッキ**にする。toctree は使わない。

````markdown
# 半導体の製造工程と関連企業

設計から製造（前工程・後工程）、装置・素材、業界俯瞰までを体系的に解説する。

:::{include} 00-intro.md
:parser: myst
:::
:::{include} 01-design.md
:parser: myst
:::
:::{include} 02-frontend.md
:parser: myst
:::
:::{include} 03-backend.md
:parser: myst
:::
:::{include} 04-industry.md
:parser: myst
:::
````

- [ ] **Step 4: `slides/Makefile` を作成**

```makefile
# slides/Makefile
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build

revealjs:
	@$(SPHINXBUILD) -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" $(SPHINXOPTS)

livehtml:
	@sphinx-autobuild -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
```

- [ ] **Step 5: 各部の最小ファイルを作成（足場：`##` 部区切りのみ、後続タスクで `###` 追記）**

`slides/00-intro.md`…`slides/04-industry.md` を作り、各先頭に **`##` の部区切り見出しのみ**を置く。
**`#` は置かない**（h1 は index.md のタイトルスライド専用。1デッキに複数 h1 があると構造が壊れる）：
`## 導入` / `## 設計` / `## 前工程` / `## 後工程` / `## 業界俯瞰`。

- [ ] **Step 6: `.gitignore` を作成**

```gitignore
_build/
.venv/
__pycache__/
```

- [ ] **Step 7: ビルドしてスモーク確認**

Run: `uv run make -C slides revealjs`
Expected: エラーなく完了、`slides/_build/revealjs/index.html` 生成。
Run: `test -f slides/_build/revealjs/index.html && echo OK`
Expected: `OK`

- [ ] **Step 8: コミット**

```bash
git add pyproject.toml uv.lock slides/ .gitignore
git commit -m "chore: scaffold slides/ sphinx-revealjs project (solarized)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: `slides/` カスタムSCSS（solarized調の工程色・日本企業バッジ・出典行）と Mermaid スモーク

**Files:**
- Create: `slides/_static/custom.scss`（sass拡張が `custom.css` にコンパイル）
- Create: `slides/_static/css/highlight.css`（ハイライトCSS）

（conf.py の sass/CSS 設定は Task 1 で確定済み。本タスクでの conf.py 変更は不要）

**Interfaces:**
- Produces: CSSクラス `.design/.frontend/.backend/.material`（工程色）、`.jp`（日本企業バッジ）、
  `.source`（出典行）。後続の全スライドタスクが使用。

- [ ] **Step 1: ハイライトCSSを配置（sass/CSS 設定は Task 1 の conf.py で確定済み）**

`sphinx_revealjs.ext.sass` は `_static` 配下の `.scss` を同名 `.css` に自動コンパイルする
（Step 2 の `_static/custom.scss` → `_static/custom.css`）。本デッキはコード片をほぼ含まないが、
revealjs-config スキルの指針に従いハイライトCSSを用意する。外部依存を避け、最小テーマを直接作成：

`slides/_static/css/highlight.css`:

```css
/* minimal solarized-ish highlight theme (deck にコードは少ないため最小限) */
.hljs { color: #657b83; background: #fdf6e3; }
.hljs-keyword, .hljs-selector-tag { color: #859900; }
.hljs-string, .hljs-attr { color: #2aa198; }
.hljs-number, .hljs-literal { color: #d33682; }
.hljs-comment { color: #93a1a1; font-style: italic; }
```

（この2ファイルは Task 1 の `revealjs_css_files = ["custom.css", "css/highlight.css"]` が読み込む）

- [ ] **Step 2: `slides/_static/custom.scss` を作成（solarized アクセント）**

```scss
// 工程種別の色（spec §6.1、solarized アクセント）
.design   { color: #268bd2; }   // 設計=青
.frontend { color: #859900; }   // 前工程=緑
.backend  { color: #cb4b16; }   // 後工程=橙
.material { color: #6c71c4; }   // 素材=菫

.badge-design   { background:#268bd2; color:#fdf6e3; }
.badge-frontend { background:#859900; color:#fdf6e3; }
.badge-backend  { background:#cb4b16; color:#fdf6e3; }
.badge-material { background:#6c71c4; color:#fdf6e3; }

// 日本企業バッジ（spec §2/§4「日本の強み」テーマ）
.jp::after {
  content: "🇯🇵";
  font-size: 0.7em;
  margin-left: 0.2em;
  vertical-align: super;
}

// 出典行（MyST脚注は使わない — spec §4）
.source {
  font-size: 0.5em;
  color: #93a1a1;   // solarized base1
  margin-top: 0.6em;
  display: block;
}
```

- [ ] **Step 3: `slides/00-intro.md` に Mermaid スモークと `.source` を仮置き（`##` 始まり・コロンフェンス）**

````markdown
## 導入
### スモークテスト

:::{mermaid}
flowchart LR
  A[設計] --> B[前工程] --> C[後工程]
:::

[出典: スモーク, 2026]{.source}
````

- [ ] **Step 4: ビルドして Mermaid とCSSクラスの反映を確認**

Run: `uv run make -C slides revealjs`
Expected: 警告・エラーなし。
Run: `ls slides/_build/revealjs/*.html`
Expected: **`index.html` のみ**（部ごとの別HTMLが無い＝単一デッキに統合されている）。
Run: `grep -o 'class="source"' slides/_build/revealjs/index.html | head -1`
Expected: `.source` クラスがHTMLに出力（1行以上）。
Run: `grep -o 'mermaid' slides/_build/revealjs/index.html | head -1`
Expected: Mermaid 描画要素が出力。

- [ ] **Step 5: ブラウザ目視（推奨）**

`run` スキルまたは手動で `slides/_build/revealjs/index.html` を開き、solarized配色・Mermaid描画・
`.source` 行が小さく出ることを確認。

- [ ] **Step 6: コミット**

```bash
git add slides/_static slides/conf.py slides/00-intro.md
git commit -m "feat: add slides SCSS (solarized process colors, JP badge, source line) + mermaid smoke

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### コンテンツ実装の共通ルール（Task 3〜9 のスライド用 MyST テンプレート）

各スライドタスクは spec §3 のスライド定義と 付録A のデータを、以下に落とす。**新しい事実を発明しない**。

**ディレクティブはすべてコロンフェンス `:::` で書く**（revealjs-authoring 規約）。バッククォート
フェンス ` ```{...} ` は使わない。

**A. 工程スライドの定型3ブロック**（①何をする→②図→③企業＋シェア）

Mermaid の工程色は**外部CSSクラスがSVG内部に効かない**ため、`classDef` に solarized の hex を
直書きする（設計#268bd2 / 前工程#859900 / 後工程#cb4b16 / 素材#6c71c4）。

````markdown
### ③リソグラフィ / 露光

パターンを転写する工程。ArF/EUV の光でレジストに回路を焼き付ける。

:::{mermaid}
flowchart LR
  R[レジスト塗布] --> E[露光] --> D[現像]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75;
  class R,E,D fe;
:::

:::{list-table}
:header-rows: 1

* - 企業
  - 役割
  - 位置づけ
* - ASML
  - EUV露光装置
  - EUVは唯一の供給元（代替なし）
* - Nikon・Canon
  - DUV露光装置
  - 成熟ノードで競合（各約5%、EUV非供給）
:::

[出典: 装置シェアは概況/2024。詳細は docs「前工程」ページ]{.source}
````

**B. 3列に収まらない比較（例：スライド2）** → 属性を「用途・特徴」に統合し3列に：

````markdown
:::{list-table}
:header-rows: 1

* - 種類
  - 用途・特徴
  - 代表企業
* - ロジック
  - 演算。微細化の主戦場
  - TSMC / NVIDIA / Intel
:::
````

**C. 日本企業の強調** → attrs_inline の**span記法 `[扶桑化学]{.jp}`** で `.jp` を付す
（出典行 `[出典: …]{.source}` と同じ形式。崩れる場合は行末に `🇯🇵` フォールバック）。

**D. 出典行＋docs導線** → 各 `###` スライド末尾に `[出典: …, 取得年。詳細は docs「<部>」ページ]{.source}`。
確度高は断定、概況は「約」。再確認対象（AMAT注入%・KLA指標・京セラ買収・Heraeus%）は数値を書かず定性表現。

**各スライドタスクの完了条件（共通）:**
- `uv run make -C slides revealjs` が警告・エラーなく通る
- そのファイルの `###` 見出し数が spec §3 の該当枚数と一致（`grep -c '^### ' slides/<file>.md`）
- 各 `###` ブロックに `.source` 行が1つ以上ある

---

### Task 3: 第0部 導入（スライド1〜3）

**Files:** Modify `slides/00-intro.md`
**Interfaces:** Consumes Task 2 のCSS。Produces バリューチェーン鳥瞰図。

- [ ] **Step 1:** spec §3 第0部に従い実装。**スライド1「タイトル」は index.md の `#`（Task 1 で作成済み）**なので 00-intro.md には作らない。00-intro.md（`## 導入` は作成済み）に `###` を2枚追加：2.半導体の種類（テンプレB 3列：ロジック/DRAM/NAND/パワー、「本編は先端ロジック/メモリ軸」明示）/ 3.全体像アジェンダ（テンプレA Mermaid 鳥瞰図、工程色 classDef）。Task 2 のスモーク `### スモークテスト` は削除。
- [ ] **Step 2:** `uv run make -C slides revealjs`（警告なし）／ `grep -c '^### ' slides/00-intro.md` → `2`（タイトルは index.md 側）／ `ls slides/_build/revealjs/*.html` → `index.html` のみ
- [ ] **Step 3:** コミット `feat: add part 0 intro slides`

---

### Task 4: 第1部 設計（スライド4〜7）

**Files:** Modify `slides/01-design.md`
**Interfaces:** Produces 分業構造の語彙。

- [ ] **Step 1:** spec §3 第1部 / 付録A 設計エコシステムに従い実装。4.分業構造（Mermaid IDM/ファブレス/ファウンドリ/OSAT）/ 5.設計フロー（仕様→論理→回路→レイアウト→検証）/ 6.EDA・IP・ISA（3列：Synopsys/Cadence/Siemens EDA、Arm、RISC-V〔Tenstorrent〕）/ 7.主要ファブレス（NVIDIA/Qualcomm/AMD/Apple/Broadcom）
- [ ] **Step 2:** ビルド（警告なし）／ `grep -c '^### ' slides/01-design.md` → `4`
- [ ] **Step 3:** コミット `feat: add part 1 design slides`

---

### Task 5: 第2部 前工程① フロー〜マスク（スライド8〜14）

**Files:** Modify `slides/02-frontend.md`（前半）
**Interfaces:** Produces 前工程フロー図。

- [ ] **Step 1:** spec §3 第2部前半 / 付録A に従い実装。8.前工程全体フロー（Mermaid、前工程色）/ 9.①ウェハー製造＋素材（信越化学・SUMCO `.jp`）/ 10.②成膜CVD/PVD/ALD＋装置（AMAT/TEL/Lam/ASM International）＋熱処理（縦型炉 **TEL/KOKUSAI/ASM 3社で73%超**、序列断定しない）/ 11.成膜材料（前駆体・特殊ガス：関東電化/大陽日酸/レゾナック/Air Liquide/Merck、スパッタターゲット：JX金属 約60%）/ 12-13.③リソグラフィ/露光（テンプレAの例：ASML=EUV独占、Nikon/Canon=DUV競合、コータ/デベロッパ=TEL、レジスト=JSR/東京応化/信越）/ 14.マスク製造エコシステム（NuFlare描画 / レーザーテック=**アクチニック（EUV光源）検査でほぼ100%** / **AGC約59%＞HOYA約34%** / 三井化学ペリクル。★日本の強み、`.jp`多用）
- [ ] **Step 2:** ビルド（警告なし）／ `grep -c '^### ' slides/02-frontend.md` → `7`
- [ ] **Step 3（ガード）:** `grep -n "アクチニック" slides/02-frontend.md` → スライド14に1件
- [ ] **Step 4:** コミット `feat: add front-end slides 8-14`

---

### Task 6: 第2部 前工程② エッチング〜まとめ（スライド15〜22）

**Files:** Modify `slides/02-frontend.md`（後半）
**Interfaces:** Produces 装置マップ／材料マップ。

- [ ] **Step 1:** spec §3 第2部後半 / 付録A に従い実装。15.④エッチング（Lam/TEL）＋ガス / 16.⑤イオン注入（AMAT〔首位、**%を書かない=再確認**〕/Axcelis/住友重機械）/ 17.⑥CMP（装置：AMAT/荏原〔世界2位=概況〕、スラリー：Entegris/DuPont/フジミ、**砥粒コロイダルシリカ：扶桑化学 世界90%超** `.jp`、パッド：DuPont約80%=日本の弱点）/ 18.⑦洗浄（SCREEN=**枚葉式**31%首位/TEL、薬液：ステラケミファ/森田化学/三菱ガス化学）/ 19.⑧計測・検査（KLA=プロセス制御首位〔**"17%超"を書かない=再確認**〕/日立ハイテク/Onto/Nova/Bruker、市場はWFEの約14%、NIST計測ギャップ）/ 20.微細化と配線革新（FinFET→GAA、BSPDN、High-NA、**W→モリブデンALD**〔Lam ALTUS Halo 2025〕）/ 21-22.前工程まとめ（装置マップ／材料マップ 2枚）
- [ ] **Step 2:** ビルド（警告なし）／ `grep -c '^### ' slides/02-frontend.md` → `15`
- [ ] **Step 3（ガード）:** `grep -n "単葉式" slides/02-frontend.md || echo OK-no-typo` → `OK-no-typo`；`grep -n "枚葉式" slides/02-frontend.md` → スライド18に1件
- [ ] **Step 4:** コミット `feat: add front-end slides 15-22`

---

### Task 7: 第3部 後工程（スライド23〜31）

**Files:** Modify `slides/03-backend.md`
**Interfaces:** Produces HBM/OSAT/先端パッケージの語彙。

- [ ] **Step 1:** spec §3 第3部 / 付録A に従い実装。23.後工程全体（Mermaid、後工程色）/ 24.バックグラインド・ダイシング（ディスコ/東京精密 `.jp`）/ 25.ボンディング・封止＋装置（ASMPT/Kulicke & Soffa/Besi/新川）/ 26.後工程材料（封止材：**住友ベークライト世界1位** `.jp` / アンダーフィル：ナミックス〔独立系〕 / ボンディングワイヤ：田中電子・日鉄マイクロメタル〔**全体首位は Heraeus、%を書かない**〕 / リードフレーム：**三井ハイテック世界1位** `.jp`）/ 27.パッケージ基板（FC-BGA、**ABF=味の素**〔PC向けほぼ100%〕 `.jp`、ガラスコア=Intel、Ibiden/新光/Unimicron/AT&S）/ 28.先端パッケージング（CoWoS/InFO/SoIC・Foveros/EMIB・I-Cube/X-Cube＋**UCIe**創設メンバー）/ 29.積層化・3D実装（ハイブリッドボンディング/WoW/TSV、HBM積層を Mermaid）/ 30.テスト（Advantest/Teradyne）＋OSAT順位（ASE/Amkor/JCET）/ 31.後工程まとめ
- [ ] **Step 2:** ビルド（警告なし）／ `grep -c '^### ' slides/03-backend.md` → `9`
- [ ] **Step 3:** コミット `feat: add part 3 back-end slides`

---

### Task 8: 第4部 業界俯瞰（スライド32〜41）

**Files:** Modify `slides/04-industry.md`（32〜41）
**Interfaces:** Produces 全体企業マップ・日本の強み総まとめ。

- [ ] **Step 1:** spec §3 第4部 / 付録A に従い実装。32.全体×企業マップ（Mermaid＋工程色）/ 33.装置業界シェア（**ASML>AMAT>Lam>TEL>KLA**、トップ5でトップ10の約85%、xychart-beta 可）/ 34.素材業界と日本（材料世界の約48%）/ 35.**日本の強み総まとめ**（確度高：レーザーテック/扶桑化学/信越化学/JX金属/三井化学/三井ハイテック・住友ベークライト `.jp`。弱点：CMPパッド=DuPont約80%。※荏原・KOKUSAIは概況注記で「確度高断定」枠外）/ 36.ファウンドリ勢力図（TSMC/Samsung/Intel、2〜3nm、Rapidus。**Rapidus×Tenstorrent は2nm IP共同開発提携〔2023-11〕で製造委託ではない**）/ 37.メモリ（DRAM：Samsung/SK hynix/Micron、NAND：層数競争/Kioxia）＋HBM順位（SK hynix首位/Samsung/Micron）/ 38.パワー半導体の別チェーン（Infineon/STMicro/onsemi/ローム/三菱、SiC：Wolfspeed/Coherent/ローム、製造フロー詳細に踏み込まない）/ 39.地政学・供給リスク / 40.トレンド / 41.まとめ
- [ ] **Step 2:** ビルド（警告なし）／ `grep -c '^### ' slides/04-industry.md` → `10`
- [ ] **Step 3（ガード）:** `grep -n "IP共同開発\|製造委託ではない" slides/04-industry.md` → スライド36にヒット
- [ ] **Step 4:** コミット `feat: add part 4 industry slides`

---

### Task 9: 用語集・出典（要約）＋ slides 全体ビルド・はみ出し・出典監査

**Files:** Modify `slides/04-industry.md`（42〜43）
**Interfaces:** Produces 用語集・出典の要約スライド（詳細は docs へ）。

- [ ] **Step 1:** 42.用語集（要点、deflist：EUV/GAA/BSPDN/HBM/OSAT/FC-BGA/ABF/UCIe/RISC-V 等）/ 43.参考文献・データ出典（要点＋「完全な出典URL・詳細は **docs「出典一覧」ページ** 参照」の導線、「シェアは変動／取得年明記」の注意書き）。※完全版は Task 12 の docs `sources`/`glossary` に置く
- [ ] **Step 2:** 全体ビルド `uv run make -C slides revealjs`（警告なし）。`###` 総数 `grep -c '^### ' slides/0[0-4]-*.md | awk -F: '{s+=$2} END{print s}'` → `42`（＋ index.md の `#` タイトルスライドで**計43枚**。スライド20分割時は 43＝計44、バッファ内で可）
- [ ] **Step 3（出典監査）:** `for f in slides/0[0-4]-*.md; do echo "$f: ###=$(grep -c '^### ' $f) source=$(grep -c '{.source}' $f)"; done` → 各ファイルで source ≥ ###（用語集等の数枚を除き原則一致）。不足は補う
- [ ] **Step 4（はみ出しレビュー）:** ブラウザで `slides/_build/revealjs/index.html` を通し、枠はみ出しを確認。**スライド20がはみ出す場合は2枚に分割**（「微細化（FinFET→GAA→BSPDN）」「配線革新（High-NA/モリブデンALD）」、総枚数44〜45はバッファ内）。分割時は Step 2 期待値を更新
- [ ] **Step 5:** コミット `feat: add glossary/source summary slides; full deck builds`

---

### Task 10: `docs/` 雛形（Furo HTML、superpanel を除外）

**Files:**
- Create: `docs/conf.py`, `docs/index.md`, `docs/Makefile`

**Interfaces:**
- Produces: ビルド `uv run make -C docs html` → `docs/_build/html/index.html`、
  ページ `overview/design/frontend/backend/industry/sources/glossary`（Task 11-12 で作成）

> 注：`docs/` は既に `superpowers/**` を含むため、`sphinx-init` スキルの「新規docs」前提と衝突しうる。
> 手動スキャフォールドし、`exclude_patterns` で `superpowers/**` を確実に除外する。

- [ ] **Step 1: `docs/conf.py` を作成**

```python
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
```

- [ ] **Step 2: `docs/index.md`（toctree ルート）を作成**

````markdown
# 半導体の製造工程と関連企業 — 補助ドキュメント

スライド（`slides/`）の深掘り・データ出典・用語集。

```{toctree}
:maxdepth: 2

overview
design
frontend
backend
industry
sources
glossary
```
````

- [ ] **Step 3: `docs/Makefile` を作成**

```makefile
# docs/Makefile
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

livehtml:
	@sphinx-autobuild -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
```

- [ ] **Step 4: 各ページの最小ファイルを作成（足場：H1のみ）**

`docs/overview.md` `docs/design.md` `docs/frontend.md` `docs/backend.md` `docs/industry.md`
`docs/sources.md` `docs/glossary.md` を作り、各先頭に H1（例 `# 前工程 詳細`）だけ置く。

- [ ] **Step 5: ビルドしてスモーク確認（superpowers が混ざらないこと）**

Run: `uv run make -C docs html`
Expected: エラーなく完了、`docs/_build/html/index.html` 生成。
Run: `grep -R "superpowers" docs/_build/html/index.html || echo "OK-excluded"`
Expected: `OK-excluded`（spec/plan がビルドに混入していない）。

- [ ] **Step 6: コミット**

```bash
git add docs/conf.py docs/index.md docs/Makefile docs/overview.md docs/design.md docs/frontend.md docs/backend.md docs/industry.md docs/sources.md docs/glossary.md
git commit -m "chore: scaffold docs/ companion site (furo, superpowers excluded)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 11: `docs/` 詳細ページ（overview + 各部4ページ）

**Files:** Modify `docs/overview.md` `docs/design.md` `docs/frontend.md` `docs/backend.md` `docs/industry.md`
**Interfaces:** Consumes spec §3/付録A。Produces スライドがリンクする詳細ページ。

各ページは対応するスライド群を**散文と表で補足**し、確度区分の根拠を明記する。数値は spec §5 の確度区分を厳守（概況は「約」、再確認対象は非断定）。Mermaid も使用可。

- [ ] **Step 1: `docs/overview.md`** — バリューチェーン全体像、分業構造、本ドキュメントの読み方、「日本の強み」通底テーマの要約
- [ ] **Step 2: `docs/design.md`** — 設計（第1部）の詳細：EDA/IP/ISA（RISC-V/UCIeの位置づけ）、ファブレスとファウンドリの関係
- [ ] **Step 3: `docs/frontend.md`** — 前工程（第2部）の詳細：各工程の目的、装置・材料の主要企業表（付録A 前工程装置/材料を丁寧に）、マスク製造エコシステムと日本の強み、微細化・配線革新（GAA/BSPDN/モリブデンALD）。**熱処理は3社寡占まで、序列断定しない**旨を明記
- [ ] **Step 4: `docs/backend.md`** — 後工程（第3部）の詳細：封止/基板/ABF、先端パッケージ各社ブランド、HBM/積層、後工程材料表（Heraeus首位も明記、%は非断定）
- [ ] **Step 5: `docs/industry.md`** — 業界俯瞰（第4部）の詳細：装置/素材/ファウンドリ/メモリ/HBM/OSAT/パワー半導体、Rapidus（IP提携≠製造委託を明記）、地政学
- [ ] **Step 6:** ビルド `uv run make -C docs html`（警告なし）／ 各ページに H2 以上の実内容があること：`for f in overview design frontend backend industry; do echo "$f: $(grep -c '^## ' docs/$f.md)"; done` → 各 ≥ 1
- [ ] **Step 7:** コミット `feat: add docs detail pages (overview + 4 parts)`

---

### Task 12: `docs/` 出典一覧・用語集 ＋ スライド相互リンク ＋ 両プロジェクト最終ビルド

**Files:** Modify `docs/sources.md` `docs/glossary.md`、`slides/*.md`（相互リンク調整）

**Interfaces:** Consumes 全スライド・全詳細ページの出典。Produces データ出典/確度の集約、用語集。

- [ ] **Step 1: `docs/sources.md`** — spec §5 の確度区分（確度高／概況／再確認対象）と、付録A・調査レポートの主要出典URLを**カテゴリ別に集約**（装置トップ5、レーザーテック、扶桑化学、JX金属、ABF、Nikon/Canon、HBM、OSAT 等）。各数値に取得年。再確認対象（AMAT注入%・KLA指標・京セラEMC買収・Heraeus%）は「未確定」と明記
- [ ] **Step 2: `docs/glossary.md`** — 用語集の完全版（deflist）。スライド42の要約より網羅的に
- [ ] **Step 3: スライドの `.source` 行から docs への導線を確認・統一**

テンプレDの通り各スライド末尾の `.source` 行に「詳細は docs『<部>』ページ」を含める。docs公開を
`slides/` と `docs/` を並置（例 `slides/` と `docs/` を同一ルート下で配信）する前提で、リンクは
相対URL（例 `../docs/frontend.html`）を用いる。ホスティング形態が未定なら、まずテキスト導線
（「docs『前工程』ページ参照」）で実装し、ハイパーリンク化は公開時に確定する。

Run: `grep -c "docs" slides/02-frontend.md`
Expected: ≥ 1（前工程スライドが docs 前工程ページへ言及）。

- [ ] **Step 4: 両プロジェクトの最終ビルド**

Run: `uv run make -C slides revealjs && uv run make -C docs html`
Expected: 両方とも警告・エラーなし。
Run: `test -f slides/_build/revealjs/index.html && test -f docs/_build/html/index.html && echo BOTH-OK`
Expected: `BOTH-OK`

- [ ] **Step 5: コミット**

```bash
git add docs/sources.md docs/glossary.md slides/
git commit -m "feat: add docs sources/glossary pages and slide cross-links; both projects build

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Self-Review（計画者によるチェック結果）

**1. Spec coverage:** spec §3 の全43スライド→Task 3〜9。§6.1 slides（solarized・SCSS・Mermaid・部分割）→Task 1〜2。
§6.2 docs（Furo・5詳細ページ・sources・glossary・superpowers除外・相互リンク）→Task 10〜12。§4 表現ルール
（3列/Mermaid/出典行/色/バッジ）→共通ルール節＋Task 2。§5 確度区分・再確認対象→各タスク注記＋ガードgrep。
§7 スコープ外（TDK不在・熱処理序列断定禁止・パワー詳細なし）→該当タスク注記。

**2. Placeholder scan:** 足場ファイル（Task 1 Step 5 / Task 10 Step 4）は後続タスクが差し替える旨を明記。
コンテンツは spec/付録A を参照元にテンプレA〜Dで具体化。曖昧表現は不使用。相互リンクのURL形態のみ
「ホスティング未定時はテキスト導線→公開時にハイパーリンク化」と判断基準を明示（曖昧放置ではない）。

**3. Type/命名 consistency:** CSSクラス `.design/.frontend/.backend/.material/.jp/.source` を全タスク統一。
ビルドコマンドは slides=`uv run make -C slides revealjs`、docs=`uv run make -C docs html` で統一。
docsページ名 `overview/design/frontend/backend/industry/sources/glossary` を Task 10-12 で一貫使用。
確度区分・再確認対象・断定禁止事項は spec §5/§7 と一致。

**設計判断（レビュー反映済み）:**
- **単一デッキ**を include 統合で実現（Task 1 Step 3/5・conf.py exclude_patterns）。部ごと独立デッキにはしない
- 依存に `myst-parser`（必須）・`sphinx-autobuild`（dev）を追加済み（Task 1 Step 1）
- sass/ハイライトCSSは conf.py に具体値を確定（`custom.scss→custom.css`、`css/highlight.css`）
- コミットトレーラーは実行モデルに一致させ **Claude Opus 4.8**（本セッションの exact model は claude-opus-4-8）

**既知のリスク/確認事項（実行時に解決）:**
- `{include}` の `:parser: myst` 指定で部ファイルがMySTとして統合されることを Task 1 Step 7 のビルドで確認
  （h1重複回避のため部ファイルは `##` 始まり厳守）
- `sphinx_revealjs.ext.sass` の scss→css 出力パスが想定と異なる場合は `revealjs_css_files` の参照を調整
- スライド↔docs のハイパーリンクはホスティング形態に依存。未定ならテキスト導線で実装（Task 12 Step 3）
- 再確認対象の数値は、実装中に一次情報が取れたスライド/ページのみ数値化してよい（取れなければ定性表現のまま）
