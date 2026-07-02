# Visual analytics braintumor

Nothing serious here gng , just sum course bs i need to keep track of 

```mermaid
flowchart TD
    
    Phase 1: Data Processing Pipeline
        D1[CuMiDa GSE50161 Dataset\n54,676 Features]:::data --> D2[Variance Threshold Filtering\nPandas]:::data
        D2 -->|Isolate Top 1000| D3[Ensembl BioMart API\nSpatial Coordinate Mapping]:::data
        D3 --> D4[(OncoLens_Annotated_Top1000.csv)]:::data
    end

    subgraph Phase 2: Backend Analytical Engines
        D4 --> B1[Dysregulation Index Engine\nNumPy Standard Scaling]:::backend
        D4 --> B2[KDE Topography\nSciPy 2D Boundaries]:::backend
        D4 --> B3[Co-occurrence Network\nNetworkX Graphing]:::backend
        D4 --> B4[Distance-Based Classifier\nScikit-learn Softmax]:::backend
    end

    subgraph Phase 3: Interactive Visualizations
        B1 --> V1[Chromosomal Hotspot Map\nPlotly Linear Facet]:::viz
        B1 --> V2[Subtype Biomarker Profiles\nViolin & Box Plots]:::viz
        B2 --> V3[Phenotypic Contour Plot\n2D Density Landfill]:::viz
        B3 --> V4[Gene Interaction Network\n2D Node-Link Graph]:::viz
        B4 --> V5[Virtual Expression Assayer\nLive Probability Sliders]:::viz
    end

    subgraph Phase 4: Full System Deployment
        V1 & V2 & V3 & V4 & V5 --> F1[Python Dash / React.js UI\nIntegrated Dashboard]:::main
        F1 --> F2[OncoLens Visual Analytics Platform]:::main
    end
