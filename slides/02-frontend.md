## 前工程

### 前工程全体フロー

前工程はウェハー上に成膜・リソグラフィ・エッチング・不純物注入などを繰り返し、微細な回路パターンを何層にも積み重ねる\
1枚のウェハーに数百の工程を経ることも珍しくない

:::{mermaid}
flowchart LR
  A[成膜] --> B[リソグラフィ] --> C[エッチング] --> D[イオン注入] --> E[CMP平坦化] --> F[洗浄] --> G[検査・計測] --> A
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class A,B,C,D,E,F,G fe
:::

[出典: 工程区分は一般的な前工程フロー\
詳細は docs「前工程」ページ]{.source}

### ①ウェハー製造 ＋ 素材

シリコンインゴットを薄くスライスし鏡面研磨したシリコンウェハーが、全工程の出発点となる基板

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - [信越化学]{.jp}
  - シリコンウェハー製造
  - 世界最大手
* - [SUMCO]{.jp}
  - シリコンウェハー製造
  - 信越化学と並ぶ大手
:::

[出典: シリコンウェハー市場, 2024年頃\
詳細は docs「前工程」ページ]{.source}

### シリコンウェーハとインゴット

:::::{list-table}
:header-rows: 0
:widths: 42 58

* - - 単結晶シリコンのインゴットを薄くスライスし鏡面研磨した基板
    - 全ての半導体チップの出発点
    - [信越化学]{.jp}・[SUMCO]{.jp}が世界2大手
  - :::{image} _static/images/shinetsu-silicon-ingot-wafer.jpg
    :alt: シリコンインゴットとウェーハ
    :width: 95%
    :align: center
    :::
:::::

[出典: 画像は信越化学工業 公式サイト]{.source}

### ②成膜 CVD/PVD/ALD ＋ 装置

外部の材料からウェハー上に絶縁膜・導電膜を「堆積」する工程\
CVD・PVD・ALDなど手法を使い分ける（基板を酸化させる熱酸化とは区別）

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 手法
  - 位置づけ
* - AMAT
  - CVD/PVD 等
  - 成膜装置全般で大手
* - [TEL]{.jp}
  - CVD 等
  - 成膜装置で大手
* - Lam Research
  - CVD 等
  - 成膜装置で大手
* - ASM International
  - ALD
  - ALD装置に強み
:::

[出典: 成膜装置は概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### CVD/PVD/ALDの使い分け

成膜には原理の異なる手法があり、膜種や求める品質で使い分ける

:::{list-table}
:header-rows: 1
:widths: auto

* - 手法
  - 原理
  - 主な用途
* - CVD
  - ガスの化学反応で膜を作る
  - 絶縁膜・W・poly-Si など最も汎用
* - PVD（スパッタ）
  - 物理的に叩き出した原子を積む
  - 金属配線・バリア・電極
* - ALD
  - 1原子層ずつ精密に積む
  - high-k・極薄バリア（先端で拡大）
:::

[出典: 手法の一般的な使い分け/2024年頃\
詳細は docs「前工程」ページ]{.source}

### 成膜の材料

成膜の材料は手法ごとに異なり、CVD/ALDはガス・前駆体、PVDは固体ターゲットを使う

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - 前駆体・特殊ガス（CVD/ALD用）
  - [関東電化]{.jp} / [大陽日酸]{.jp} / [レゾナック]{.jp} / Air Liquide / Merck
  - 高純度ガス・薬液を供給する専業各社
* - スパッタリングターゲット（PVD用）
  - [JX金属]{.jp}
  - 世界シェア約60%
:::

[出典: スパッタリングターゲットは約60%（2024年頃）\
詳細は docs「前工程」ページ]{.source}

### スパッタリング（PVD）の仕組み

真空中でイオンをターゲットに衝突させ、叩き出した原子をウェハーに積もらせる成膜法\
主に金属の薄膜（配線・バリア・電極）をつくる

:::::{list-table}
:header-rows: 0
:widths: 45 55

* - - Arガスをプラズマ化しAr+イオンを作る
    - イオンがターゲットに衝突し原子を弾き出す
    - 弾き出された原子がウェハーに堆積する
    - 銅配線・バリア(Ta/TiN)・電極に使う
  - :::{mermaid}
    flowchart TB
      Ar[Arプラズマ Ar+イオン] --> T[ターゲットに衝突]
      T --> A[金属原子を叩き出す]
      A --> W[ウェハーに堆積 薄膜化]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class Ar,W fe
      class T,A material
    :::
:::::

[出典: 機構は一般的なスパッタリング(PVD)の自作図/2024年頃\
詳細は docs「前工程」ページ]{.source}

### スパッタリングターゲット

:::::{list-table}
:header-rows: 0
:widths: 55 45

* - - PVD(スパッタ)で金属薄膜を成膜する原料
    - 銅配線・バリア(Ta/TiN)・電極などに使用
    - 高純度・低パーティクルが要求される
    - [JX金属]{.jp}が世界シェア約6割
  - :::{image} _static/images/jx-sputter-target.jpg
    :alt: スパッタリングターゲット
    :width: 300px
    :align: center
    :::
:::::

[出典: 画像はJX金属 公式サイト／シェアは概況2024年頃\
詳細は docs「前工程」ページ]{.source}

### ③リソグラフィ / 露光（露光装置）

パターンを転写する工程\
ArF/EUVの光でレジストに回路パターンを焼き付け、現像する

:::{mermaid}
flowchart LR
  R[レジスト塗布] --> E[露光] --> D[現像]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class R,E,D fe
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - ASML
  - EUV/DUV露光装置
  - EUVは唯一の供給元（代替なし）\
    High-NA機も展開
* - [Nikon]{.jp} / [Canon]{.jp}
  - DUV露光装置
  - 成熟ノードで競合（ArF液浸/KrF等、各社約5%程度、EUVは非供給）
:::

[出典: 露光装置シェアは概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### 露光装置の基本構成

光源からの光を照明系で整え、マスクの回路パターンを投影レンズで縮小してウェハーに転写する\
ウェハーを少しずつ動かして露光を繰り返す（ステップ&リピート）

:::{mermaid}
flowchart LR
  S[光源 ArF/EUV等] --> I[照明光学系] --> M[マスク レチクル] --> L[投影レンズ] --> W[ウェハー レジスト]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class S,I,M,L,W fe
:::

:::{note}
EUV(13.5nm)はレンズが使えず反射ミラー光学系を採用\
EUV露光装置はASMLが唯一の供給元
:::

### EUVとDUVの違い（光路）

EUVは物質に吸収されレンズを使えないため反射ミラー光学系を採用する\
DUVは従来どおりレンズを透過させる

:::::{list-table}
:header-rows: 1
:widths: 50 50

* - DUV（透過・レンズ）
  - EUV（反射・ミラー）
* - :::{mermaid}
    flowchart TB
      L[光源 ArF 193nm] --> M[透過マスク] --> Le[レンズ 透過] --> W[ウェハー]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      class L,M,Le,W fe
    :::
  - :::{mermaid}
    flowchart TB
      L2[光源 Sn 13.5nm] --> M2[反射マスク] --> Mi[ミラー 反射] --> W2[ウェハー]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class L2,W2 fe
      class M2,Mi material
    :::
:::::

### EUVとDUVの違い（仕様）

:::{list-table}
:header-rows: 1
:widths: auto

* - 項目
  - DUV
  - EUV
* - 波長
  - 193nm(ArF) / 248nm(KrF)
  - 13.5nm
* - 光学系
  - レンズ（透過）
  - ミラー（反射）
* - 環境
  - 大気・ArFは液浸
  - 真空
* - 供給
  - ASML / [Nikon]{.jp} / [Canon]{.jp}
  - ASMLのみ
:::

[出典: 露光方式の一般的な比較/2024年頃\
詳細は docs「前工程」ページ]{.source}

### EUV光学系：多段反射の仕組み

EUVは吸収されレンズを使えないため、全て真空中の反射ミラーで結像する\
集光から投影まで多数のミラーを経るのが特徴

:::::{list-table}
:header-rows: 0
:widths: 52 48

* - - ミラーはMo/Si多層膜で反射率は約70%止まり
    - 集光・照明・反射マスク・投影(6枚)で計10回前後反射
    - 反射のたびに減衰し光はウェハーで数%に（0.7を10回で約3%）
    - 損失を補うため250W級の高出力光源が必要
  - :::{mermaid}
    flowchart TB
      S[光源 100%] --> A[集光・照明ミラー]
      A --> M[反射マスク]
      M --> P[投影ミラー 6枚]
      P --> W[ウェハー 数%]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class S,W fe
      class A,M,P material
    :::
:::::

[出典: 多層膜ミラーの反射率・段数は一般的な概説/2024年頃\
詳細は docs「前工程」ページ]{.source}

### ③リソグラフィ / 露光（周辺装置・材料）

露光装置と一体で動くコータ・デベロッパ、および感光材料のレジスト

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - [TEL]{.jp}
  - コータ・デベロッパ
  - EUV用装置でほぼ100%
* - [JSR]{.jp} / [東京応化]{.jp} / [信越化学]{.jp}
  - フォトレジスト
  - 日本勢が世界シェアの大半を占める
:::

[出典: 装置・材料シェアは概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### フォトレジスト（感光材料）

光が当たった部分の溶解性が変わる感光性樹脂\
EUV用レジストは日本勢が圧倒的で微細化の鍵となる材料

:::::{list-table}
:header-rows: 0
:widths: 45 55

* - - ポジ型は露光部が現像で溶ける
    - EUVレジストは技術難度が高い
    - [JSR]{.jp}/[東京応化]{.jp}/[信越化学]{.jp}/[富士フイルム]{.jp}/[住友化学]{.jp}
  - :::{mermaid}
    flowchart TB
      A[レジスト塗布 スピンコート] --> B[露光 マスク経由で光照射]
      B --> C[現像 ポジ型は露光部が溶解]
      C --> D[パターン形成 エッチングへ]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class A,C material
      class B,D fe
    :::
:::::

[出典: プロセスは一般的なポジ型レジストの自作図/2024年頃\
詳細は docs「前工程」ページ]{.source}

### マスク製造エコシステム

フォトマスクは回路パターンの原版\
描画・検査・素材（ブランクス・ペリクル）のいずれも日本企業の存在感が大きい、日本の強みが最も光る領域

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - [NuFlare]{.jp}
  - マスク描画装置
  - マルチビーム方式で独占的
* - [レーザーテック]{.jp}
  - EUVマスク欠陥検査
  - アクチニック（EUV光源）方式でほぼ100%\
    e-beam方式は他社も存在
* - [AGC]{.jp}
  - マスクブランクス
  - 世界シェア約59%
* - [HOYA]{.jp}
  - マスクブランクス
  - 世界シェア約34%（AGCと2社で約93%）
* - [三井化学]{.jp}
  - EUVペリクル
  - 量産を担う中心企業
:::

[出典: マスク関連シェアは概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### EUVペリクル

:::::{list-table}
:header-rows: 0
:widths: 42 58

* - - マスクを異物から守る極薄の保護膜
    - EUV光を透過する必要があり技術難度が高い
    - [三井化学]{.jp}がASMLのライセンスで量産
  - :::{image} _static/images/mitsui-euv-pellicle.jpg
    :alt: EUVペリクル
    :width: 95%
    :align: center
    :::
:::::

[出典: 画像は三井化学 公式サイト]{.source}

### ④エッチング

成膜・露光で形成したパターン通りに、不要な膜を化学的・物理的に削り取る工程\
反応性ガスのプラズマを使うドライエッチングが主流

:::{mermaid}
flowchart LR
  M[マスク形成済みウェハー] --> P[プラズマ生成] --> E[選択的エッチング] --> R[レジスト除去]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class M,P,E,R fe
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - Lam Research
  - ドライエッチング装置
  - エッチング装置で大手
* - [TEL]{.jp}
  - ドライエッチング装置
  - エッチング装置で大手
* - 各社エッチングガス（フッ素系・塩素系）
  - 特殊ガス供給
  - 高純度ガスが不可欠
:::

[出典: エッチング装置は概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### ⑤イオン注入・ドーピング

シリコン結晶に不純物イオンを高速で打ち込み、電気的性質（n型／p型）を作り込む工程\
加速したイオンビームを照射する

:::{mermaid}
flowchart LR
  I[イオン源] --> A[加速・質量分離] --> W[ウェハーへ注入]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class I,A,W fe
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - AMAT
  - イオン注入装置
  - 世界首位
* - Axcelis
  - イオン注入装置
  - 専業大手
* - [住友重機械]{.jp}（SEN）
  - イオン注入装置
  - 主要プレイヤーの一角
:::

[出典: イオン注入装置は概況/2024年頃、各社シェアは出典未確定のため記載せず\
詳細は docs「前工程」ページ]{.source}

### 熱処理・アニール ＋ 装置

ウェハーを高温で加熱し、膜質・不純物・結晶状態を整える工程

酸化（熱酸化）
: シリコン基板そのものを酸化させSiO2膜を「成長」させる（外から積む成膜とは別）

アニール（活性化）
: イオン注入した不純物を電気的に活性化し結晶欠陥を回復する

RTP（急速熱処理）
: 短時間で加熱し不純物の余計な拡散を抑える

:::{note}
活性化アニールはこの位置、酸化など他の熱処理は工程の随所で使う補助工程
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 装置
  - 位置づけ
* - [TEL]{.jp} / [KOKUSAI ELECTRIC]{.jp} / ASM International
  - 縦型炉
  - 3社で世界シェア73%超（企業別の序列は断定できない）
:::

[出典: 縦型炉シェアは概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### ⑥CMP 平坦化

成膜を重ねるほど生じる表面の凹凸を、化学反応とスラリー研磨で平坦にする工程\
次の層を精度良く形成するために不可欠

:::{mermaid}
flowchart LR
  S[凹凸のある表面] --> C[化学反応+研磨] --> F[平坦な表面]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class S,C,F fe
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 分野
  - 代表企業
  - 位置づけ
* - CMP装置
  - AMAT / [荏原]{.jp}
  - 荏原は世界2位クラス（概況）
* - スラリー完成品
  - Entegris / DuPont / [フジミ]{.jp}
  - 研磨液を仕上げる完成品メーカー各社
* - CMP砥粒（コロイダルシリカ）
  - [扶桑化学]{.jp}
  - 世界シェア90%超
* - CMPパッド
  - DuPont
  - 世界シェア約80%（日本勢は手薄、弱点）
:::

[出典: CMP装置・材料は概況/2024年頃、扶桑化学の砥粒シェアは複数ソース一致\
詳細は docs「前工程」ページ]{.source}

### CMPの仕組み

化学反応と機械研磨を組み合わせてウェハー表面を平坦化する\
砥粒（コロイダルシリカ）と薬液を含むスラリーが鍵を握る

:::::{list-table}
:header-rows: 0
:widths: 45 55

* - - 研磨ヘッドがウェハーをパッドへ押し付ける
    - スラリーの化学＋砥粒の機械作用で削る
    - 砥粒は[扶桑化学]{.jp}が世界90%超
  - :::{mermaid}
    flowchart TB
      Head[研磨ヘッド ウェハー保持] --> Contact[パッドに押し付け 相対回転]
      Slurry[スラリー 砥粒+薬液] --> Contact
      Contact --> Flat[化学+機械で平坦化]
      classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
      classDef material fill:#6c71c4,color:#fdf6e3,stroke:#586e75
      class Head,Contact,Flat fe
      class Slurry material
    :::
:::::

[出典: 機構は一般的なCMPの自作図、砥粒シェアは複数ソース一致/2024年頃\
詳細は docs「前工程」ページ]{.source}

### ⑦洗浄

各工程の合間にウェハー表面のパーティクルや金属汚染を除去する工程\
1枚ずつ処理する枚葉式が高精度な洗浄で主流になっている

:::{mermaid}
flowchart LR
  W[汚染ウェハー] --> C[薬液洗浄+リンス] --> D[乾燥]
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  class W,C,D fe
:::

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - [SCREEN]{.jp}
  - 枚葉式洗浄装置
  - 枚葉式で世界シェア31%・首位
* - [TEL]{.jp}
  - 洗浄装置
  - 主要プレイヤーの一角
* - [ステラケミファ]{.jp} / [森田化学]{.jp} / [三菱ガス化学]{.jp}
  - 高純度ウェット薬液
  - 三菱ガス化学は過酸化水素で世界首位
:::

[出典: 洗浄装置・薬液は概況/2024年頃\
詳細は docs「前工程」ページ]{.source}

### ⑧計測・検査（メトロロジー）

各工程の後にパターン寸法・欠陥・膜厚などを測定し、歩留まりを支える工程\
微細化が進むほど計測精度の重要性が増す

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 役割
  - 位置づけ
* - KLA
  - 計測・検査装置全般
  - プロセス制御分野の首位
* - [日立ハイテク]{.jp}
  - CD-SEM
  - 寸法計測で主要プレイヤー
* - Onto Innovation / Nova / Bruker
  - 計測装置各種
  - 専業各社
:::

計測・検査市場は装置投資（WFE）全体の約14%を占める（2025年頃）\
米NISTはCHIPS法のもとで「計測ギャップ」を国家的な課題と位置づけている

[出典: 計測・検査市場は概況/2025年頃、KLAの数値指標は出典未確定のため記載せず\
詳細は docs「前工程」ページ]{.source}

### 微細化と配線革新

トランジスタの微細化は平面構造からFinFET、さらに全周を囲むGAA（Gate-All-Around）構造へと進化\
配線側でも電源配線を裏面に移すBSPDNや、より短波長のHigh-NA EUVが次の焦点となる

:::{list-table}
:header-rows: 1
:widths: auto

* - トピック
  - 内容
* - トランジスタ構造
  - FinFET → GAA（ナノシート）へ移行
* - バックサイド給電（BSPDN）
  - 電源配線をウェハー裏面に移し配線混雑を緩和
* - High-NA EUV
  - ASMLの次世代露光でさらなる微細化
* - 配線材料の刷新
  - 微細配線でW（タングステン）からモリブデンALDへ（Lam ALTUS Halo, 2025年）
:::

[出典: 微細化ロードマップは概況/2025年頃\
詳細は docs「前工程」ページ]{.source}

### 前工程まとめ：装置マップ

前工程を通じて登場した主要装置企業を工程別に整理する

:::{list-table}
:header-rows: 1
:widths: auto

* - 工程
  - 装置企業
  - 位置づけ
* - 成膜・熱処理
  - AMAT / [TEL]{.jp} / Lam / ASM International / KOKUSAI ELECTRIC
  - 縦型炉は3社で73%超
* - 露光・マスク
  - ASML / [Nikon]{.jp} / [Canon]{.jp} / [NuFlare]{.jp} / [レーザーテック]{.jp}
  - EUVはASML独占、マスク検査はレーザーテックがほぼ独占
* - エッチング・注入
  - Lam / [TEL]{.jp} / AMAT / Axcelis / [住友重機械]{.jp}
  - エッチングはLam・TELが大手
* - CMP・洗浄・計測
  - AMAT / [荏原]{.jp} / [SCREEN]{.jp} / KLA / [日立ハイテク]{.jp}
  - SCREENは枚葉式洗浄で首位
:::

[出典: 各工程シェアは概況/2024〜2025年頃\
詳細は docs「前工程」ページ]{.source}

### 前工程まとめ：材料マップ

前工程で使われる主要材料と、その供給企業を整理する\
日本企業が世界シェアで存在感を示す分野が多い

:::{list-table}
:header-rows: 1
:widths: auto

* - 材料
  - 代表企業
  - 位置づけ
* - シリコンウェハー
  - [信越化学]{.jp} / [SUMCO]{.jp}
  - 世界シェアの大半を日本勢が占める
* - フォトレジスト
  - [JSR]{.jp} / [東京応化]{.jp} / [信越化学]{.jp}
  - 日本勢で世界の8〜9割
* - スパッタターゲット
  - [JX金属]{.jp}
  - 世界シェア約60%
* - マスクブランクス・ペリクル
  - [AGC]{.jp} / [HOYA]{.jp} / [三井化学]{.jp}
  - AGC・HOYA2社で約93%、ペリクルは三井化学が中心
* - CMP砥粒
  - [扶桑化学]{.jp}
  - 世界シェア90%超
* - CMPパッド
  - DuPont
  - 世界シェア約80%（日本の弱点）
* - 高純度薬液
  - [ステラケミファ]{.jp} / [森田化学]{.jp} / [三菱ガス化学]{.jp}
  - 三菱ガス化学は過酸化水素で世界首位
:::

[出典: 各材料シェアは概況/2024年頃\
詳細は docs「前工程」ページ]{.source}
