## 設計

### 産業の分業構造

半導体産業は「設計と製造を垂直統合する企業」と「工程ごとに専業化した企業」に分かれる

:::{mermaid}
flowchart LR
  subgraph IDM["IDM（垂直統合型）"]
    I1[設計] --> I2[製造]
  end
  subgraph SPLIT["水平分業型"]
    F[ファブレス: 設計に特化] -->|製造委託| FD[ファウンドリ: 製造専業]
    FD --> O[OSAT: 組立・検査専業]
  end
  classDef design fill:#268bd2,color:#fdf6e3,stroke:#586e75
  classDef fe fill:#859900,color:#fdf6e3,stroke:#586e75
  classDef be fill:#cb4b16,color:#fdf6e3,stroke:#586e75
  class I1,F design
  class I2,FD fe
  class O be
:::

[出典: 産業構造区分は概況\
詳細は docs「設計」ページ]{.source}

### 設計工程の流れ

:::{mermaid}
flowchart LR
  S[仕様] --> L[論理設計] --> C[回路設計] --> P[レイアウト] --> V[検証]
  classDef design fill:#268bd2,color:#fdf6e3,stroke:#586e75
  class S,L,C,P,V design
:::

[出典: 設計フローは一般的な工程区分\
詳細は docs「設計」ページ]{.source}

### EDA・IP・ISA

設計を支えるソフトウェア（EDA）と、回路を再利用可能にするIP、命令セット（ISA）が設計エコシステムの土台

:::{list-table}
:header-rows: 1
:widths: auto

* - 領域
  - 代表企業・規格
  - 位置づけ
* - EDA
  - Synopsys / Cadence / Siemens EDA
  - 設計自動化ツールの大手3社
* - IP
  - Arm
  - モバイル・組込み向け命令セット・コア設計で主流
* - オープンISA
  - RISC-V（Tenstorrent 等）
  - ライセンス不要のオープン命令セット\
    Arm代替の潮流
:::

[出典: 企業・規格の位置づけは概況\
詳細は docs「設計」ページ]{.source}

### 主要ファブレス

:::{list-table}
:header-rows: 1
:widths: auto

* - 企業
  - 主な注力領域
  - 備考
* - NVIDIA
  - GPU・AIアクセラレータ
  - 生成AI向け需要で急成長
* - Qualcomm
  - モバイル向けSoC・通信
  - スマートフォン向けチップで大手
* - AMD
  - CPU・GPU
  - サーバー・PC向けで存在感
* - Apple
  - 自社製品向けSoC
  - 設計は自社／製造はTSMC委託のファブレス
* - Broadcom
  - 通信・ネットワーク半導体
  - カスタムASIC・IPも展開
:::

[出典: 企業の注力領域は概況\
詳細は docs「設計」ページ]{.source}
