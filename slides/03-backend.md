## 後工程

### 後工程全体

前工程で回路パターンを形成したウェハーを、個々のチップに切り出し、外部と電気的に接続し、外部環境から保護する一連の工程\
近年は高性能化を支える先端パッケージング技術の重要性が増している

:::{mermaid}
flowchart LR
  A[裏面研削] --> B[ダイシング] --> C[ボンディング] --> D[封止] --> E[検査]
  classDef be fill:#cb4b16,color:#fdf6e3,stroke:#586e75
  class A,B,C,D,E be
:::

[出典: 工程区分は一般的な後工程フロー\
詳細は docs「後工程」ページ]{.source}

### バックグラインド・ダイシング

ウェハーの裏面を薄く削る「バックグラインド」と、個々のチップに切り分ける「ダイシング」が後工程の入り口\
積層パッケージやスマートフォン向けの薄型化が進むほど、ウェハーをより薄く精密に加工する技術が重要になる

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 装置
  - 位置づけ
* - [ディスコ]{.jp}
  - バックグラインダー / ダイシングソー
  - 両分野で世界的な大手
* - [東京精密]{.jp}
  - バックグラインダー / ダイシングソー
  - [ディスコ]{.jp}と並ぶ主要プレイヤー
:::

[出典: バックグラインド・ダイシング装置は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### 精密ダイシング・グラインド（ディスコ）

:::::{list-table}
:header-rows: 0
:widths: 42 58

* - - ウェハーを切断・薄化する精密加工装置
    - 「切る・削る・磨く」で歩留りを支える
    - [ディスコ]{.jp}が世界7〜8割の準独占
  - :::{image} _static/images/disco-dicing-saw.jpg
    :alt: ダイシングソー（ディスコ）
    :width: 420px
    :align: center
    :::
:::::

[出典: 画像はディスコ 公式サイト／シェアは概況2024年頃]{.source}

### リードフレーム

切り出したチップを載せ、ボンディングと封止の土台となる部材

:::::{list-table}
:header-rows: 0
:widths: 42 58

* - - チップと外部端子をつなぐ金属の枠
    - 微細な打ち抜き・エッチング加工で製造
    - [三井ハイテック]{.jp}が世界シェア1位
  - :::{image} _static/images/mitsui-hitec-leadframe.jpg
    :alt: リードフレーム
    :width: 95%
    :align: center
    :::
:::::

[出典: 画像は三井ハイテック 公式サイト]{.source}

### ボンディング ＋ 装置

切り出したチップを基板やリードフレームに固定し、電気的に接続する工程\
接続方式は用途により使い分けられる

ワイヤボンディング
: 金属細線でチップと基板の端子を接続する方式

ダイボンディング
: チップを基板やリードフレームに固定する工程

フリップチップボンディング
: チップ表面のバンプで直接接続する方式

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 装置
  - 位置づけ
* - ASMPT
  - ワイヤ/ダイボンダー
  - ボンディング装置全般で大手
* - Kulicke & Soffa
  - ワイヤボンダー
  - ワイヤボンディングで主要プレイヤー
* - Besi
  - ダイ/フリップチップボンダー
  - 高精度実装装置で大手
* - [新川]{.jp}
  - ワイヤボンダー
  - 日本の主要プレイヤー
:::

[出典: ボンディング装置は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### 封止（モールド） ＋ 装置

ボンディング後のチップをモールド樹脂（EMC）で覆い、外部環境から保護する工程\
封止材そのものは「後工程材料」で扱う

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 装置
  - 位置づけ
* - [TOWA]{.jp}
  - モールディング装置
  - 封止装置で世界大手
* - ASMPT
  - モールディング装置
  - ボンディングと併せ後工程装置を広くカバー
* - Besi
  - モールディング装置
  - 実装〜封止の装置を手がける
:::

[出典: 封止装置は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### パッケージの断面構造

ここまでの工程で組み上がるパッケージの構造\
従来型と先端型では土台と接続方式が異なる

:::{image} _static/images/package-cross-section.svg
:alt: パッケージ断面の模式図（リードフレーム型とFC-BGA型）
:width: 70%
:align: center
:::

[出典: 構造は一般的な模式図]{.source}

### 後工程材料

封止材やアンダーフィル、ボンディングワイヤ、リードフレームなど、後工程を支える材料群にも日本企業の強みが目立つ分野がある

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - 封止材/モールド樹脂（EMC）
  - [住友ベークライト]{.jp}
  - 世界シェア1位
* - アンダーフィル
  - [ナミックス]{.jp}
  - 独立系（レゾナック傘下ではない）
* - ボンディングワイヤ
  - [田中電子工業]{.jp}（金線）/ [日鉄マイクロメタル]{.jp}（銅線）
  - 全体では独Heraeusが首位とされる（シェアは出典未確定のため記載せず）
* - リードフレーム
  - [三井ハイテック]{.jp}
  - 世界シェア1位
:::

[出典: 封止材・リードフレームは確度高（複数ソース一致）、その他は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### パッケージ基板

高性能チップの周辺には、微細配線を持つパッケージ基板が必要になる\
FC-BGA基板の絶縁材料ABF（Ajinomoto Build-up Film）は[味の素]{.jp}がほぼ独占的に供給しており、日本企業の強みが際立つ分野\
次世代ではガラスをコア材に使う「ガラスコア基板」をIntelが推進している

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - ABF（絶縁材料）
  - [味の素]{.jp}
  - PC向けほぼ100%、ハイエンド帯でも95〜100%
* - FC-BGA基板
  - [Ibiden]{.jp} / [新光電気工業]{.jp} / Unimicron / AT&S
  - 主要な基板メーカー各社
* - ガラスコア基板
  - Intel
  - 次世代基板として開発を推進
:::

[出典: ABFシェアは確度高（複数ソース一致）、その他は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### 味の素ビルドアップフィルム(ABF)

味の素のアミノ酸関連技術から生まれた層間絶縁フィルム\
PC向けCPU基板でほぼ100%のシェアを持つ

:::::{list-table}
:header-rows: 0
:widths: 55 45

* - - フィルム状で厚みが均一
    - 液状インクより工程を短縮できる
    - 微細化・多層化に対応
  - :::{mermaid}
    flowchart TB
      A[保護フィルム] --- B[ABF樹脂 絶縁層] --- C[支持体 PET]
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class A,B,C material
    :::
:::::

[出典: 構造・用途は味の素の公開情報を基に自作図/2024年頃\
詳細は docs「後工程」ページ]{.source}

### ABFの役割（FC-BGA基板）

チップと基板をつなぐ層間絶縁材として微細配線を多層化する\
コア基板の上にABF絶縁層と銅配線を交互に積み上げる（ビルドアップ）

:::::{list-table}
:header-rows: 0
:widths: 55 45

* - - 高密度な再配線を実現
    - 高性能CPU/GPUのFC-BGAに不可欠
    - 次世代はガラスコア基板の動きも
  - :::{mermaid}
    flowchart TB
      Chip[半導体チップ] --- BU[ビルドアップ層 ABF絶縁+銅配線] --- Core[コア基板] --- Ball[はんだボール BGA]
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      classDef be fill:#cb4b16,color:#fdf6e3,stroke:#586e75
      class BU material
      class Chip,Core,Ball be
    :::
:::::

[出典: 構成は一般的なFC-BGAビルドアップ基板の自作図/2024年頃\
詳細は docs「後工程」ページ]{.source}

### 先端パッケージング

複数のチップを1パッケージに統合する2.5D/3D実装やチップレット構成、HBM（広帯域メモリ）の搭載が先端半導体の性能を左右するようになっている\
大手各社はそれぞれ独自ブランドの先端パッケージング技術を展開する

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - ブランド
  - 概要
* - TSMC
  - CoWoS / InFO / SoIC
  - 2.5D（CoWoS）・ファンアウト（InFO）・3D積層（SoIC）
* - Intel
  - Foveros / EMIB
  - 3D積層（Foveros）・チップ間ブリッジ接続（EMIB）
* - Samsung
  - I-Cube / X-Cube
  - 2.5D（I-Cube）・3D積層（X-Cube）
:::

異なるベンダーのチップレットを組み合わせるには接続方式の標準化が欠かせない\
**UCIe（Universal Chiplet Interconnect Express）**はその業界標準で、AMD・Arm・Intel・TSMC・Samsungなどが創設メンバーとして参加する

[出典: 各社ブランドとUCIe創設メンバーは公表情報、2024年頃\
詳細は docs「後工程」ページ]{.source}

### 積層化・3D実装

チップを垂直に積み、TSV（シリコン貫通電極）で層間を直接接続して配線距離を縮める\
バンプを使わず銅パッド同士を直接接合する**ハイブリッドボンディング**やWafer-on-Wafer（WoW）が採用され始め、HBMはその象徴

```{raw} html
<div style="display:flex;flex-direction:column;align-items:center;margin:.4em 0;">
  <div style="width:13em;text-align:center;padding:.3em 0;background:#cb4b16;color:#fdf6e3;border:1px solid #fdf6e3;">DRAMダイ #4</div>
  <div style="width:13em;text-align:center;padding:.3em 0;background:#cb4b16;color:#fdf6e3;border:1px solid #fdf6e3;border-top:none;">DRAMダイ #3</div>
  <div style="width:13em;text-align:center;padding:.3em 0;background:#cb4b16;color:#fdf6e3;border:1px solid #fdf6e3;border-top:none;">DRAMダイ #2</div>
  <div style="width:13em;text-align:center;padding:.3em 0;background:#cb4b16;color:#fdf6e3;border:1px solid #fdf6e3;border-top:none;">DRAMダイ #1</div>
  <div style="width:13em;text-align:center;padding:.3em 0;background:#586e75;color:#fdf6e3;border:1px solid #fdf6e3;border-top:none;">ベースダイ（ロジック）</div>
  <div style="margin-top:.35em;font-size:.8em;color:#657b83;">層間は TSV（シリコン貫通電極）で垂直接続</div>
</div>
```

[出典: 積層技術・HBM構造は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### テスト工程

封止後のチップは、テスタを用いた電気的検査で良品を選別する\
この最終検査を含む後工程全体を専門に請け負う企業群がOSAT（Outsourced Semiconductor Assembly and Test）と呼ばれる

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - 半導体テスタ
  - [Advantest]{.jp} / Teradyne
  - テスタ市場の二強
* - OSAT
  - ASE（首位）/ Amkor / JCET
  - 後工程を専門に請け負う受託企業
:::

[出典: テスタ・OSAT順位は概況/2024年頃\
詳細は docs「後工程」ページ]{.source}

### 後工程まとめ

裏面研削・ダイシングからボンディング・封止・パッケージ基板・先端パッケージング・テストまで、後工程には多くの専業企業が関わる\
特に封止材・リードフレーム・ABFなど材料分野では日本企業の存在感が大きい

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - 加工装置
  - [ディスコ]{.jp} / [東京精密]{.jp} / ASMPT / Besi / Kulicke & Soffa / [新川]{.jp}
  - バックグラインド・ダイシング・ボンディングを担う
* - 材料
  - [住友ベークライト]{.jp} / [ナミックス]{.jp} / [田中電子工業]{.jp} / [日鉄マイクロメタル]{.jp} / [三井ハイテック]{.jp} / [味の素]{.jp}
  - 封止材・リードフレーム・ABFで日本勢が強み
* - パッケージング・テスト
  - TSMC / Intel / Samsung / [Advantest]{.jp} / ASE
  - 先端パッケージングとテスト・OSATの主要プレイヤー
:::

[出典: 各分野シェアは概況/2024年頃\
詳細は docs「後工程」ページ]{.source}
