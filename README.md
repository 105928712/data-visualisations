# Phishing URL Data Visualisations
COS30049 Computing Technology Innovation Project - Phishing Link Detection data analysis (EDA)

The repository includes `eda_raw.ipynb` to perform a bias check on the raw input data, as well as `eda_features.ipynb` to analyse the cleaned data and extracted features through class balancing, distribution checks, correlations, and PCA, with all generated charts saved directly to the figures/ directory.

## Installation

Depending on what OS you are running, you will need to use a different command for installation:

For Windows:
```bash
setup.bat
```
or
```bash
. .\setup.ps1
```

For macOS and Linux/Unix:
```bash
source setup.sh
```

## Usage

The setup scripts initialise a Python virtual environment (venv) with the libraries required that are listed in `requirements.txt`.

Before running the notebooks, ensure you extract the CSV files into the current directory to provide the necessary data inputs. 

After the venv is initialised and the files are extracted, select a notebook and attempt to run it using the 'Run All' option. You may be prompted to install the Jupyter extension, proceed with installation if so.

Selecting the 'Run All' option will prompt you to choose a kernel, select the .venv one, which resides in the current directory.

The notebook will then run and you will be able to see outputs and visualisations.

## Notebooks Summary - Exploratory Data Analysis

### `eda_raw.ipynb` - Raw Data

This notebook analyses the raw base Kaggle dataset before any cleaning to identify any anomalies as well as systematic and formatting flaws. It uncovers critical dataset biases, such as an artificial formatting gap in URL schemes and `www` prefixes, alongside two blocks of mislabelled rows at the end of the file. The findings directly inform the structural cleaning script, which re-labels the incorrect blocks, strips formatting biases, and handles broken strings.

### `eda_features.ipynb` - Cleaned Data & Features

This notebook checks the data after cleaning to test feature strength and guide model selection. In the base Kaggle dataset, it reveals a heavy 83.3% legitimate class imbalance, meaning standard accuracy is misleading and forces the team to use metrics like F1-score instead. By mapping feature correlations and using 2D charts (PCA), it exposes overlapping data and near-duplicate features. These insights prove that non-linear tree models will perform best and show that phishing URLs form clear sub-groups for clustering.