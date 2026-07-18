## 導入

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

[出典: 代表企業は概況\
詳細は docs「概要」ページ]{.source}

### 全体像アジェンダ（バリューチェーン鳥瞰図）

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
