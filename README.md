# Phishing URL Data Visualisations
COS30049 Computing Technology Innovation Project - Phishing Link Detection Exploratory Data Analysis (EDA)

The repository includes `eda_raw.ipynb` to perform a bias check on the raw input data, `eda_features.ipynb` to analyse the cleaned data and extracted features through class balancing, distribution checks, correlations, and PCA, and `eda_merged.ipynb` to check that the extra Mendeley data fits in with the Kaggle data. All generated charts are saved to the `figures/` directory.

## Installation

The datasets in `datasets/` are zips stored with Git LFS

**Automatic** (venv): create the environment, install the packages, download the LFS files and unzip them into `datasets/`:
- Windows: `setup.bat` (Command Prompt) or `. .\setup.ps1` for (PowerShell)
- macOS / Linux: `source setup.sh`

**Manual** (Conda):
```bash
conda create -n phishing-visualisations python=3.13 -y
conda activate phishing-visualisations
pip install -r requirements.txt
git lfs install
git lfs pull
```
Then unzip `datasets/Final Tree.zip` and `datasets/Extra Data.zip` inside `datasets/`

## Data

Every notebook starts with `FINAL_TREE = "datasets/Final Tree"`. It must be downloaded and extracted or this will not work.

```
datasets/
├── Final Tree.zip  
├── Extra Data.zip  
├── Final Tree/          raw -> cleaned -> merged -> features.csv
└── Extra Data/          tranco_1m, tranco_processed, urlset
```

## Usage

1. Run the setup, which also downloads and unzips the datasets
2. Open the folder in VS Code and pick the environment as the kernel
3. Open a notebook and use **Run All**. Charts are written to `figures/`.

Run order doesn't matter, but it reads best as `eda_raw` -> `eda_features` -> `eda_merged`.

## Notebooks Summary - Exploratory Data Analysis

### `eda_raw.ipynb` - Raw Data

This notebook analyses the raw base Kaggle dataset before any cleaning to identify any anomalies as well as systematic and formatting flaws. It uncovers critical dataset biases, such as an artificial formatting gap in URL schemes and `www` prefixes, alongside two blocks of mislabelled rows at the end of the file. The findings directly inform the structural cleaning script, which re-labels the incorrect blocks, strips formatting biases, and handles broken strings.

### `eda_features.ipynb` - Cleaned Data & Features

This notebook checks the data after cleaning to test feature strength and guide model selection. In the base Kaggle dataset, it reveals a heavy 83.3% legitimate class imbalance, meaning standard accuracy is misleading and forces the team to use metrics like F1-score instead. By mapping feature correlations and using 2D charts (PCA), it exposes overlapping data and near-duplicate features. These insights suggest that non-linear tree models will perform best and show that phishing URLs form clear sub-groups for clustering.

### `eda_merged.ipynb` - Kaggle & Mendeley

This notebook checks the extra data the final model trains on. It shows what each source actually adds after cleaning and de-duplication (Mendeley adds mostly phishing URLs, so phishing class distribution goes from 16.7% to 35%), proves the per-source cleaning removed the formatting differences between sources (scheme and `www.` go to 0% on all sources), explains why Tranco and urlset datasets were dropped, and finally verifies that no feature becomes a shortcut once the sources are merged to one set.
