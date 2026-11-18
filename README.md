# Football Analytics: Player Form Representations and Expected Goals

A two-stage project on Israeli Premier League data. The first stage scrapes player statistics and learns compact player style vectors with an autoencoder. The second stage uses those vectors, together with shot-level features, to predict the probability of a goal and compares the model with the official league xG.

## Stage 1: Scraping and player representations

- `scraper/`: collects match-level player statistics from SofaScore (Selenium with ChromeDriver).
- `preprocessing/`: cleans the data, normalizes stats per minute played, and encodes positions.
- `modeling/`: a fully connected autoencoder (PyTorch, 16-dimensional latent space) and latent vector extraction.
- `Plotting/`, `materials/`: PCA and t-SNE visualizations of the latent space, colored by position and league.

Setup: `pip install -r requirements.txt`. Google Chrome and a matching ChromeDriver are required for the scraper. Further details are in `Data/Technicalities.md`.

## Stage 2: Expected goals (`xg/`)

The notebooks in `xg/notebooks/` run in order:

1. `01_Data_Preprocessing_ETL.ipynb`: cleans the player statistics and the shot events, and maps player names between the two sources.
2. `02_Temporal_Feature_Engineering.ipynb`: computes exponential moving averages (EMA) of the 37 player statistics, so each shot uses only matches played before it.
3. `03_Representation_Learning_and_Fusion.ipynb`: trains an autoencoder on the EMA features and attaches the shooter and goalkeeper style vectors to each shot. Training data is augmented (foot mirroring and small coordinate shifts) on the training split only.
4. `04_Modeling_and_Evaluation.ipynb`: splits the data chronologically at 2025-01-07, trains baseline and XGBoost, MLP and Ridge models, and evaluates them against the official xG with Brier score, log-loss and AUC.

Requirements: Python 3.10 to 3.12, pandas, numpy, scikit-learn, torch, xgboost, openpyxl, joblib, matplotlib, seaborn. On macOS, XGBoost also needs `brew install libomp`.

### Results

On 2,577 test shots from 2024/25 that match the official league file (89% of the test set), the best model (XGBoost, with player style features) reaches:

| Model | Brier score | AUC |
|---|---|---|
| Official league xG | 0.0796 | 0.816 |
| Best model (XGBoost) | 0.0711 | 0.874 |

That is about 11% lower Brier score than the official xG.

### Data

- **Shot events:** Israeli Premier League shot data from the league administration (ISA), seasons 2023-24 and 2024-25.
- **Player statistics:** collected with the scraper in Stage 1.

The raw data is not included in this repository.
