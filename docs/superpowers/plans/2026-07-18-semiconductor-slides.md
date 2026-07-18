# 半導体の製造工程と関連企業スライド 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** sphinx-revealjs で、半導体のバリューチェーン（設計→前工程→後工程→業界俯瞰）を企業・シェア付きで解説する約43枚のHTMLスライドを作る。

**Architecture:** `docs/` を Sphinx ソースルートとし、MyST Markdown を部ごとに5ファイル分割（`00-intro.md`〜`04-industry.md`）して `index.md` の toctree で束ねる。図解は sphinx-oceanid の Mermaid、色分け・日本企業バッジ・出典行はカスタムSCSSクラスで実装。既存の `docs/superpowers/**`（spec/plan）は `exclude_patterns` でビルド対象外にする。

**Tech Stack:** Python (uv), Sphinx, sphinx-revealjs, sphinx-revealjs.ext.sass, sphinx-oceanid (Mermaid), MyST。

**Content source of truth:** すべてのスライドの内容・企業・数値・出典方針は
`docs/superpowers/specs/2026-07-18-semiconductor-slides-design.md`（特に §3 構成 と 付録A 企業/数値リスト）、
および根拠調査 `research/2026-07-18-semiconductor-gaps-research.md` に定義済み。本計画はそれを重複させず参照する。

## Global Constraints

- スライド構造は見出し階層で表す：`#`=タイトルスライド / `##`=各部の区切り / `###`=個別スライド（spec §6）
- **list-table は最大3列厳守**（revealjs-authoring スキル）。4項目以上を比べる場合は属性統合か2枚分割（spec §4）
- 図は Mermaid（sphinx-oceanid のサポート型のみ：flowchart / sequence / class / state / er / xychart-beta 等）
- **出典はMyST脚注を使わない**。各スライド末尾に小文字テキスト行＋CSSクラス `.source` で表示し、数値の隣に取得年を併記（spec §4/§5）
- 色の約束：設計=青 / 前工程=緑 / 後工程=橙 / 素材=紫。日本企業はバッジ強調（spec §4、CSSクラスで実装）
- 数値の**確度区分を厳守**（spec §5）：確度高＝断定可 / 概況＝「約」「〜年時点」で丸め。
  再確認対象（AMATイオン注入%、KLA指標、京セラEMC買収、Heraeus%）は数値を断定しない
- 断定禁止：熱処理・ALDの企業別シェア序列（spec §7）。荏原CMP2位・KOKUSAI単独序列は「概況」扱い
- 各コンテンツタスクは `uv run make -C docs revealjs` が**警告・エラーなく**通ることを完了条件に含める
- コミットはタスク単位で頻繁に。コミットメッセージ末尾に
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` を付す

---

### Task 1: プロジェクト雛形（Sphinx + revealjs ビルドが通る最小構成）

**Files:**
- Create: `pyproject.toml`（uv 管理）
- Create: `docs/conf.py`
- Create: `docs/index.md`
- Create: `docs/Makefile`（`sphinx-build` スキルの雛形に準拠）
- Create: `.gitignore`

**Interfaces:**
- Produces: ビルドコマンド `uv run make -C docs revealjs`、出力 `docs/_build/revealjs/index.html`、
  Sphinx ソースルート `docs/`、toctree ルート `docs/index.md`

> 補足：`revealjs-init` スキルは「既存 docs/ なし」が前提だが、本リポジトリには既に `docs/superpowers/**` が
> あるため使えない。よって手動スキャフォールドする。conf.py の細部（sass拡張・ハイライトCSS・プラグイン）で
> 迷ったら `revealjs-config` スキルを参照して補正する（目標状態は下記の通り）。

- [ ] **Step 1: uv プロジェクト初期化と依存追加**

```bash
cd /home/driller/repo/making-semiconductors
uv init --no-workspace --name making-semiconductors --python 3.12
uv add sphinx sphinx-revealjs sphinx-oceanid libsass
```

Expected: `pyproject.toml` と `uv.lock` が生成され、依存が解決される。

- [ ] **Step 2: `docs/conf.py` を作成**

```python
# docs/conf.py
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

# 既存の spec/plan は本スライドのビルド対象外
exclude_patterns = ["_build", "superpowers/**", "Thumbs.db", ".DS_Store"]

revealjs_static_path = ["_static"]
revealjs_style_theme = "white"
revealjs_script_conf = {
    "width": 1280,
    "height": 720,
    "slideNumber": "c/t",
    "hash": True,
}
# ハイライトCSSは必須（可視化のため）。_static/css に配置し下で読み込む。
revealjs_css_files = ["css/custom.css"]
```

> 注：`revealjs_css_files` にハイライトテーマCSSが要る（revealjs-config スキル指摘）。Task 2 で
> `_static/css/` にハイライトCSSを置き、必要ならこの配列に追記する。sass拡張の入力/出力設定名は
> `revealjs-config` スキルで確認して合わせる。

- [ ] **Step 3: `docs/index.md`（toctree ルート）を作成**

````markdown
# 半導体の製造工程と関連企業

```{toctree}
:maxdepth: 1
:hidden:

00-intro
01-design
02-frontend
03-backend
04-industry
```
````

- [ ] **Step 4: `docs/Makefile` を作成（sphinx-build スキルの標準雛形）**

```makefile
# docs/Makefile
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

- [ ] **Step 5: 各部の最小ファイルを作成（ビルドを通すためのプレースホルダ見出しのみ）**

`docs/00-intro.md` … `docs/04-industry.md` を作り、各ファイル先頭に部タイトルだけ置く。例：

```markdown
# 導入
## 導入
```

（他4ファイルも同様に `# 設計` `# 前工程` `# 後工程` `# 業界俯瞰` を置く。内容は後続タスクで差し替え）

- [ ] **Step 6: `.gitignore` を作成**

```gitignore
docs/_build/
.venv/
__pycache__/
```

- [ ] **Step 7: ビルドしてスモーク確認**

Run: `uv run make -C docs revealjs`
Expected: エラーなく完了し、`docs/_build/revealjs/index.html` が生成される。

Run: `test -f docs/_build/revealjs/index.html && echo OK`
Expected: `OK`

- [ ] **Step 8: コミット**

```bash
git add pyproject.toml uv.lock docs/conf.py docs/index.md docs/Makefile docs/00-intro.md docs/01-design.md docs/02-frontend.md docs/03-backend.md docs/04-industry.md .gitignore
git commit -m "chore: scaffold sphinx-revealjs slide project

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: カスタムSCSS（色分け・日本企業バッジ・出典行）と Mermaid スモーク

**Files:**
- Create: `docs/_static/scss/custom.scss`（sass拡張でコンパイル）
- Modify: `docs/conf.py`（sass入出力とハイライトCSSの設定を確定）
- Create: `docs/_static/css/`（ハイライトCSS配置先）

**Interfaces:**
- Produces: CSSクラス `.design` `.frontend` `.backend` `.material`（工程色）、`.jp`（日本企業バッジ）、
  `.source`（出典行）。後続の全コンテンツタスクがこれらを使う。

- [ ] **Step 1: `revealjs-config` スキルを参照して sass 拡張とハイライトCSSを conf.py に設定**

目標状態：`docs/_static/scss/custom.scss` が `_static/css/custom.css` にコンパイルされ、
`revealjs_css_files` にハイライトテーマCSS（例 `css/highlight-github.css`）と `css/custom.css` が入る。
（設定キー名の正確な綴りは revealjs-config スキルに従う）

- [ ] **Step 2: `docs/_static/scss/custom.scss` を作成**

```scss
// 工程種別の色（spec §4）
.design   { color: #1f6feb; }   // 設計=青
.frontend { color: #2ea043; }   // 前工程=緑
.backend  { color: #e0873d; }   // 後工程=橙
.material { color: #8957e5; }   // 素材=紫

// 見出し帯にも使えるよう背景版
.badge-design   { background:#1f6feb; color:#fff; }
.badge-frontend { background:#2ea043; color:#fff; }
.badge-backend  { background:#e0873d; color:#fff; }
.badge-material { background:#8957e5; color:#fff; }

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
  color: #8b949e;
  margin-top: 0.6em;
  display: block;
}
```

- [ ] **Step 3: `docs/00-intro.md` に Mermaid スモークと `.source` を仮置き**

````markdown
# 導入
## 導入
### スモークテスト

```{mermaid}
flowchart LR
  A[設計] --> B[前工程] --> C[後工程]
```

[出典: スモーク, 2026]{.source}
````

- [ ] **Step 4: ビルドして Mermaid とCSSクラスの反映を確認**

Run: `uv run make -C docs revealjs`
Expected: エラー・警告なく完了。

Run: `grep -R "class=\"source\"" docs/_build/revealjs/ | head -1`
Expected: `.source` クラスがHTMLに出力されている（1行以上ヒット）。

Run: `grep -R "mermaid" docs/_build/revealjs/00-intro.html | head -1`
Expected: Mermaid の描画要素が出力されている。

- [ ] **Step 5: ブラウザ目視（任意だが推奨）**

`run` スキルまたは手動で `docs/_build/revealjs/index.html` を開き、Mermaid図が描画され、
`.source` 行が小さく灰色で出ることを確認。

- [ ] **Step 6: コミット**

```bash
git add docs/_static docs/conf.py docs/00-intro.md
git commit -m "feat: add custom SCSS (process colors, JP badge, source line) and mermaid smoke

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### コンテンツ実装の共通ルール（Task 4〜9 で使う MyST テンプレート）

各コンテンツタスクは spec §3 のスライド定義と 付録A のデータを、以下のテンプレートに落とす。
**新しい事実を発明しない**。企業・数値・出典は spec/調査レポートにある範囲のみ。

**A. 工程スライドの定型3ブロック**（spec §4：①何をする→②図→③企業＋シェア）

````markdown
### ③リソグラフィ / 露光

パターンを転写する工程。ArF/EUV の光でレジストに回路を焼き付ける。

```{mermaid}
flowchart LR
  R[レジスト塗布] --> E[露光] --> D[現像]
```

```{list-table}
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
```

[出典: 装置シェアは概況/2024、spec 付録A。EUV独占は複数一次情報]{.source}
````

**B. 3列に収まらない比較（例：スライド2の半導体種類）** → 属性を「用途・特徴」に統合し3列に：

```{list-table}
:header-rows: 1

* - 種類
  - 用途・特徴
  - 代表企業
* - ロジック
  - 演算。微細化の主戦場
  - TSMC / NVIDIA / Intel
```

**C. 日本企業の強調** → セル内でロール付き：`` {span}`扶桑化学`{.jp} `` のように `.jp` を付す
（コンパイル後にバッジが出る。バッジが崩れる場合は行末に `🇯🇵` を直接置くフォールバックでも可）。

**D. 出典行** → 各 `###` スライド末尾に必ず1行 `[出典: … , 取得年]{.source}` を置く。
確度高は断定、概況は「約」。再確認対象（AMAT注入%・KLA指標・京セラ買収・Heraeus%）は数値を書かず定性表現。

各コンテンツタスクの完了条件（共通）：
- `uv run make -C docs revealjs` が警告・エラーなく通る
- そのファイルの `###` 見出し数が spec §3 の該当枚数と一致（`grep -c '^### ' docs/<file>.md`）
- そのファイルの各 `###` ブロックに `.source` 行が1つ以上ある

---

### Task 3: 第0部 導入（スライド1〜3）

**Files:**
- Modify: `docs/00-intro.md`

**Interfaces:**
- Consumes: Task 2 のCSSクラス。Produces: バリューチェーン鳥瞰図（後続の各部が参照する全体像）。

- [ ] **Step 1: スライド1〜3 を実装**

spec §3 第0部に従い、`docs/00-intro.md` を差し替え：
1. タイトルスライド（`#` タイトル＋副題）
2. 半導体の種類（テンプレB の3列 list-table：ロジック/DRAM/NAND/パワー × 用途・特徴 × 代表企業。
   「本編は先端ロジック/メモリを軸に」と明示）
3. 全体像アジェンダ（テンプレA の Mermaid で 設計→前工程→後工程→業界俯瞰 の鳥瞰図。工程色クラスを付与）

Task 2 で置いたスモークの `### スモークテスト` は削除する。

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。

Run: `grep -c '^### ' docs/00-intro.md`
Expected: `3`

- [ ] **Step 3: コミット**

```bash
git add docs/00-intro.md
git commit -m "feat: add part 0 intro slides (semiconductor types, value-chain overview)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 4: 第1部 設計（スライド4〜7）

**Files:**
- Modify: `docs/01-design.md`

**Interfaces:**
- Consumes: 鳥瞰図の設計フェーズ。Produces: 分業構造（IDM/ファブレス/ファウンドリ/OSAT）の語彙（後続で参照）。

- [ ] **Step 1: スライド4〜7 を実装（spec §3 第1部 / 付録A 設計エコシステム）**

4. 産業の分業構造（Mermaid で IDM / ファブレス / ファウンドリ / OSAT の関係図）
5. 設計工程の流れ（仕様→論理→回路→レイアウト→検証、Mermaid）
6. EDA・IP・ISA（3列表：EDA=Synopsys/Cadence/Siemens EDA、IP=Arm、オープンISA=RISC-V〔Tenstorrent〕）
7. 主要ファブレス（3列表：NVIDIA/Qualcomm/AMD/Apple/Broadcom と主力領域）

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/01-design.md`
Expected: `4`

- [ ] **Step 3: コミット**

```bash
git add docs/01-design.md
git commit -m "feat: add part 1 design slides (fabless/foundry split, EDA/IP/RISC-V, fabless leaders)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 5: 第2部 前工程① フロー〜マスク（スライド8〜14）

**Files:**
- Modify: `docs/02-frontend.md`（前半を追記）

**Interfaces:**
- Consumes: 分業構造の語彙。Produces: 前工程フロー図（Task 6 のまとめが参照）。

- [ ] **Step 1: スライド8〜14 を実装（spec §3 第2部前半 / 付録A 前工程装置・材料）**

8. 前工程全体フロー（Mermaid：成膜→リソ→エッチング→注入→CMP→洗浄→検査 のループ、前工程色）
9. ①ウェハー製造＋素材（信越化学・SUMCO、`.jp`）
10. ②成膜 CVD/PVD/ALD＋装置（AMAT/TEL/Lam/ASM International）＋熱処理（縦型炉 **TEL/KOKUSAI/ASM の3社で73%超**、序列は断定しない）
11. 成膜の材料（前駆体・特殊ガス：関東電化/大陽日酸/レゾナック/Air Liquide/Merck、スパッタターゲット：JX金属 約60%）
12-13. ③リソグラフィ/露光（テンプレAの例そのもの：ASML=EUV独占、Nikon/Canon=DUV競合、コータ/デベロッパ=TEL、レジスト=JSR/東京応化/信越）
14. マスク製造エコシステム（NuFlare描画 / レーザーテック＝**アクチニック（EUV光源）検査でほぼ100%** / **AGC約59%＞HOYA約34%** / 三井化学ペリクル。★日本の強み、`.jp`多用）

> 注：スライド14のレーザーテックは必ず「アクチニック」限定を残す。ブランクスは AGC→HOYA の順（数字順）。

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/02-frontend.md`
Expected: この時点で `7`（スライド8〜14）

- [ ] **Step 3: レーザーテックの限定表現を検証**

Run: `grep -n "アクチニック" docs/02-frontend.md`
Expected: スライド14に1件ヒット（限定条件が残っている）。

- [ ] **Step 4: コミット**

```bash
git add docs/02-frontend.md
git commit -m "feat: add front-end slides 8-14 (flow, wafer, deposition, litho, mask ecosystem)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 6: 第2部 前工程② エッチング〜まとめ（スライド15〜22）

**Files:**
- Modify: `docs/02-frontend.md`（後半を追記）

**Interfaces:**
- Consumes: 前工程フロー図。Produces: 装置マップ／材料マップ（第4部 業界俯瞰が参照）。

- [ ] **Step 1: スライド15〜22 を実装（spec §3 第2部後半 / 付録A）**

15. ④エッチング（Lam/TEL）＋エッチングガス
16. ⑤イオン注入（AMAT〔首位、**%は書かない＝再確認対象**〕/Axcelis/住友重機械）
17. ⑥CMP（装置：AMAT/荏原〔世界2位＝概況〕、スラリー：Entegris/DuPont/フジミ、**砥粒コロイダルシリカ：扶桑化学 世界90%超**`.jp`、パッド：DuPont約80%＝日本の弱点）
18. ⑦洗浄（SCREEN＝**枚葉式**31%首位/TEL、薬液：ステラケミファ/森田化学/三菱ガス化学）
19. ⑧計測・検査（KLA＝プロセス制御首位〔**"17%超"は書かない＝再確認対象**〕/日立ハイテク/Onto/Nova/Bruker、市場はWFEの約14%、NIST計測ギャップに言及）
20. 微細化と配線革新（FinFET→GAA、BSPDN、High-NA、**W→モリブデンALD**〔Lam ALTUS Halo 2025〕）
21-22. 前工程まとめ（装置マップ／材料マップ：ここまでの企業を工程色で一覧化、2枚）

> 注：スライド18は「枚葉式」（「単葉式」ではない）。スライド16/19は疑義数値を書かず定性表現。

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/02-frontend.md`
Expected: `15`（第2部合計＝8〜22）

- [ ] **Step 3: 誤記・疑義数値のガード**

Run: `grep -n "単葉式" docs/02-frontend.md || echo "OK-no-typo"`
Expected: `OK-no-typo`（「単葉式」が存在しない）。
Run: `grep -n "枚葉式" docs/02-frontend.md`
Expected: スライド18に1件ヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/02-frontend.md
git commit -m "feat: add front-end slides 15-22 (etch, implant, CMP, clean, metrology, scaling, maps)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 7: 第3部 後工程（スライド23〜31）

**Files:**
- Modify: `docs/03-backend.md`

**Interfaces:**
- Consumes: 前工程完了（薄化前のウェハー）。Produces: HBM/OSAT/先端パッケージの語彙（第4部が参照）。

- [ ] **Step 1: スライド23〜31 を実装（spec §3 第3部 / 付録A 後工程）**

23. 後工程全体（Mermaid：裏面研削→ダイシング→ボンディング→封止→検査、後工程色）
24. バックグラインド・ダイシング（ディスコ/東京精密、`.jp`、積層・薄型化と接続）
25. ボンディング・封止＋装置（ASMPT/Kulicke & Soffa/Besi/新川）
26. 後工程材料（封止材：**住友ベークライト世界1位**`.jp`／アンダーフィル：ナミックス〔独立系〕／ボンディングワイヤ：田中電子・日鉄マイクロメタル〔**全体首位は Heraeus、%は書かない**〕／リードフレーム：**三井ハイテック世界1位**`.jp`）
27. パッケージ基板（FC-BGA、**ABF=味の素**〔PC向けほぼ100%〕`.jp`、ガラスコア=Intel、Ibiden/新光/Unimicron/AT&S）
28. 先端パッケージング（各社ブランド：CoWoS/InFO/SoIC・Foveros/EMIB・I-Cube/X-Cube＋**UCIe**創設メンバー）
29. 積層化・3D実装（ハイブリッドボンディング/WoW/TSV、HBM積層構造を Mermaid で図解）
30. テスト工程（Advantest/Teradyne）＋OSAT順位（ASE/Amkor/JCET）
31. 後工程まとめ

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/03-backend.md`
Expected: `9`

- [ ] **Step 3: コミット**

```bash
git add docs/03-backend.md
git commit -m "feat: add part 3 back-end slides (dicing, packaging, ABF substrate, HBM/3D, test)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 8: 第4部 業界俯瞰（スライド32〜41）

**Files:**
- Modify: `docs/04-industry.md`（32〜41）

**Interfaces:**
- Consumes: 各部で登場した企業。Produces: 全体企業マップ・日本の強み総まとめ。

- [ ] **Step 1: スライド32〜41 を実装（spec §3 第4部 / 付録A 業界）**

32. バリューチェーン全体×企業マップ（Mermaid＋工程色で総まとめ）
33. 製造装置業界シェア（**ASML>AMAT>Lam>TEL>KLA**、トップ5でトップ10の約85%。xychart-beta 併用可）
34. 素材業界と日本の位置づけ（材料世界の約48%）
35. **日本の強み総まとめ**（確度高：レーザーテック/扶桑化学/信越化学/JX金属/三井化学/三井ハイテック・住友ベークライト、`.jp`。弱点：CMPパッド=DuPont約80%。※荏原・KOKUSAIは概況注記で「確度高断定」枠外）
36. ファウンドリ勢力図（TSMC/Samsung/Intel、2〜3nm、Rapidus。**Rapidus×Tenstorrent は2nm IP共同開発提携〔2023-11〕で製造委託ではない**と明記）
37. メモリ（DRAM：Samsung/SK hynix/Micron、NAND：層数競争/Kioxia）＋HBM順位（SK hynix首位/Samsung/Micron）
38. パワー半導体の別サプライチェーン（Infineon/STMicro/onsemi/ローム/三菱、SiC：Wolfspeed/Coherent/ローム。製造フロー詳細には踏み込まない）
39. 地政学・供給リスク（台湾集中/米中/各国補助金/CHIPS法）
40. トレンド（AI半導体・HBM・先端パッケージ・積層化）
41. まとめ

> 注：スライド35は §5 確度高リストと顔ぶれを一致させる。スライド36は「IP提携≠製造委託」を必ず区別。

- [ ] **Step 2: ビルドと構造チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/04-industry.md`
Expected: この時点で `10`（32〜41）

- [ ] **Step 3: Rapidusの限定表現を検証**

Run: `grep -n "IP" docs/04-industry.md | grep -i tenstorrent || grep -n "製造委託ではない\|IP共同開発" docs/04-industry.md`
Expected: スライド36に「IP共同開発／製造委託ではない」旨がある。

- [ ] **Step 4: コミット**

```bash
git add docs/04-industry.md
git commit -m "feat: add part 4 industry slides (equipment/materials share, Japan strengths, foundry/memory/power, geopolitics)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 9: 用語集・出典（スライド42〜43）＋ 全体ビルド・はみ出し・出典監査

**Files:**
- Modify: `docs/04-industry.md`（42〜43 追記）

**Interfaces:**
- Consumes: 全スライドの出典。Produces: データ出典の集約スライド。

- [ ] **Step 1: スライド42〜43 を実装**

42. 用語集（EUV/GAA/BSPDN/HBM/OSAT/FC-BGA/ABF/UCIe/RISC-V 等、deflist）
43. 参考文献・データ出典（spec §5 の確度区分と、付録A・調査レポートの主要出典URLを集約。
    「シェアは変動する／取得年明記」の注意書き）

- [ ] **Step 2: 全体ビルドと総枚数チェック**

Run: `uv run make -C docs revealjs`
Expected: 警告・エラーなし。
Run: `grep -c '^### ' docs/0[0-4]-*.md | awk -F: '{s+=$2} END{print s}'`
Expected: `43`（第2部が2枚に割れた場合は 44〜45。spec のバッファ内なら可）。

- [ ] **Step 3: 出典行の網羅監査（各スライドに `.source` があるか）**

Run: `for f in docs/0[0-4]-*.md; do echo "$f: ### =$(grep -c '^### ' $f) source=$(grep -c '{.source}' $f)"; done`
Expected: 各ファイルで `source` 数 ≥ `###` 数（用語集スライド等、出典不要な数枚を除き原則一致）。不足があれば補う。

- [ ] **Step 4: ブラウザ目視で「はみ出し」レビュー（特にスライド20）**

`run` スキルまたは手動で `docs/_build/revealjs/index.html` を開き、全スライドを送って
テキスト/表がスライド枠からはみ出していないか確認。**スライド20（微細化と配線革新）がはみ出す場合は
2枚に分割**（見出しを「微細化（FinFET→GAA→BSPDN）」と「配線革新（High-NA/モリブデンALD）」に。
総枚数44〜45はバッファ内）。分割したら Step 2 の期待値を更新。

- [ ] **Step 5: コミット**

```bash
git add docs/04-industry.md
git commit -m "feat: add glossary and data-source slides; full-deck build passes

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Self-Review（計画者によるチェック結果）

**1. Spec coverage:** spec §3 の全43スライドを Task 3〜9 に割当済み（0部→T3、1部→T4、2部→T5+T6、
3部→T7、4部→T8+T9）。§4 表現ルール（3列/Mermaid/出典行/色/バッジ）は共通ルール節＋Task 2 のCSSで担保。
§5 確度区分・再確認対象は各タスクの注記とガード grep で担保。§6 技術構成は Task 1/2。§7 スコープ外
（TDK不在・熱処理序列断定禁止・パワー詳細なし）は該当タスクの注記で担保。

**2. Placeholder scan:** Task 1 Step 5 の「部タイトルのみ」は意図的な足場で後続タスクが差し替える旨を明記済み。
コンテンツは spec/付録A を参照元とし、テンプレA〜Dで具体化。曖昧な「適切に実装」表現は不使用。

**3. Type consistency:** CSSクラス名は `.design/.frontend/.backend/.material/.jp/.source` で全タスク統一。
ビルドコマンド `uv run make -C docs revealjs`、構造チェック `grep -c '^### '`、出典 `{.source}` を全タスクで統一。

**既知のリスク/確認事項（実行時に解決）:**
- conf.py の sass拡張・ハイライトCSSの設定キー名は `revealjs-config` スキルで最終確認（Task 2 Step 1）
- `sphinx-autobuild`（livehtml）を使う場合は依存追加が必要（任意）
- 数値の再確認対象（AMAT注入%・KLA指標・京セラEMC買収・Heraeus%）は断定せず、実装中に一次情報が
  取れたスライドのみ数値化してよい（取れなければ定性表現のまま）
