## はじめに

### 半導体の種類

:::{list-table}
:header-rows: 1
:widths: auto

* - 種類
  - 用途・特徴
  - 代表企業
* - ロジック
  - 演算処理\
    微細化の主戦場
  - TSMC / NVIDIA / Intel / AMD
* - DRAM
  - 主記憶\
    高速・揮発性
  - Samsung / SK hynix / Micron
* - NAND
  - 大容量ストレージ\
    不揮発性・層数競争
  - Samsung / [Kioxia]{.jp} / SK hynix / Micron
* - パワー
  - 電力変換・制御\
    自動車/産業機器向け
  - Infineon / STMicro / [ローム]{.jp}
:::

本編は先端ロジック/メモリを軸に（パワーは別系統）

[出典: 代表企業は概況（＝民間調査の推計のおおよその値）\
詳細は docs「概要」ページ]{.source}

### トランジスタの仕組み（電圧で動くスイッチ）

チップの中身はトランジスタ＝ゲート電圧でON/OFFする電気のスイッチ\
ON＝電流あり＝1 OFF＝電流なし＝0 として2進数を扱う

:::{image} _static/images/logic-1-transistor-switch.svg
:alt: ゲート電圧が1でON（出力1）0でOFF（出力0）になるトランジスタスイッチ
:width: 74%
:align: center
:::

[出典: 動作は一般的なMOSスイッチの自作図]{.source}

### スイッチから論理ゲートへ（1/0の演算）

スイッチ（1/0）の組み合わせでAND/OR/NOT/XORなどの論理ゲートを作る

:::{image} _static/images/logic-2-gates.svg
:alt: AND・OR・NOT・XORゲートの記号と真理値表
:width: 80%
:align: center
:::

[出典: 論理ゲートの記号・真理値表は一般的な定義]{.source}

### 論理ゲートで2進数を計算する（半加算器）

XORで和 ANDで桁上げを作ると1桁の2進加算ができる\
A＝1 B＝1 なら 和0・桁上げ1 で 1＋1＝10（2進）になる

:::{image} _static/images/logic-3-binary-adder.svg
:alt: 半加算器 XORで和 ANDで桁上げ 1+1=10（2進）
:width: 80%
:align: center
:::

[出典: 半加算器は一般的な論理回路の自作図]{.source}

### 微細化するとなぜ嬉しいか

トランジスタ（スイッチ）を小さくするほど 速く・安く・省電力になる\
だから各社は微細化＝トランジスタを小さくする競争にしのぎを削る

:::{mermaid}
flowchart LR
  T[トランジスタを小さく<br/>＝微細化] --> F[速い]
  T --> L[安い]
  T --> P[省電力]
  classDef design fill:#268bd2,color:#fdf6e3,stroke:#586e75
  class T,F,L,P design
:::

[出典: 入門的な一般説明\
詳細は docs「概要」ページ]{.source}

### アジェンダ

:::{mermaid}
flowchart LR
  D[設計] --> F[前工程] --> B[後工程] --> I[業界俯瞰]
  classDef design fill:#268bd2,color:#fdf6e3,stroke:#586e75
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  classDef be fill:#cb4b16,color:#fdf6e3,stroke:#586e75
  classDef ov fill:#586e75,color:#fdf6e3,stroke:#073642
  class D design
  class F fe
  class B be
  class I ov
:::

[出典: 本編の章構成に対応\
詳細は docs「概要」ページ]{.source}
