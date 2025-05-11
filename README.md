# Football Scraper AE Project

This project scrapes player-level football data from SofaScore, preprocesses it, and applies an Autoencoder to generate player latent representations.

## Purpose 
This project scrapes football match statistics from SofaScore, preprocesses the data across multiple games, and trains an autoencoder model to extract meaningful player embeddings. The embeddings are visualized using PCA and t-SNE to reveal player similarity patterns across leagues and positions. 
The purpose is to fit a model that given past performances, extracts a player form for a fixed timestamp.
The end goal is to achieve a informative low dimension representation by using the encoders' output for latent space of players' game stats.

## System Requirements
To run this project locally, ensure that your environment includes the following:
- Python 3.8 or higher  
- Install all required libraries using:
  ```bash
  pip install -r requirements.txt
- The scraper uses Selenium with ChromeDriver. Please ensure you have Google Chrome installed and that the ChromeDriver version matches your browser version.



## Structure
- scraping: SofaScore game data scraper
- preprocessing: Data cleaning and normalization
- modeling: Autoencoder model, training, and latent extraction
- notebooks: Project walkthrough and visualizations
- data: Folder for raw scraped Excel files (not uploaded)
- outputs: Folder for outputs like final CSVs (not uploaded)

## General Steps
1. Scrape match data using sofascore_scraper.py.
2. Preprocess using preprocessing_pipeline.py.
3. Train Autoencoder and extract latent vectors.
4. Visualize and analyze results using project_walkthrough.ipynb.

## Scraping & Preprocessing 
Before training the autoencoder, raw match statitics are scraped from SofaScore and after that are preprocessed to autoencoder ready input.

**Scarping** -
First, the inputs are start date, end date, Country, league and season. the scraper is built from two main modules, the first one opens SofaScore, and navigates through the site to the specified season and league and collects the URLs of all matches played in that season in between the dates. The second module of the scraper gets all the URLs and iterates all over them and one by one, loads the match and scrapes all the stats to one data frame. lastly all the data concats and converted to one xlsx file.

**Important notes**  - the scraper navigates throught the site using HTML elements that might change overtime. It is recommended to first try explore this option in case of bugs. The first module (URL collection) is more prone to crashes from time to time, when scraping large amounnts of data (more than a couple os seasons), we recommend to verify that the URL collection is finished.

**Preprocessing** -
We identify uniqely each (playerID, date) as a different record.
Preprocessing takes in the data, keeps the relevant columns, extracts ratings table aside and the goes over the columns so that every important column consists of one number, so rates (succusful/attempted) columns are separated. position, home/away on the field also translated to numbers.
All aggregative stats are divided by minutes played attribute to normalize performances and finally miuntes played is normalized as well to (0,1]

**Further** explaination on technical steps and scraping and preprocessing can be found in [here](Data/Technicalities.md)


## Training 
Once preprocessing was complete, we trained a standard Autoencoder model using PyTorch. The model was designed to compress each player's match-level statistics into a low-dimensional latent vector, and then reconstruct the original input as accurately as possible.

- The input to the model was the normalized player stat vectors from the preprocessing pipeline.
- We used a symmetric Autoencoder architecture with fully connected layers and ReLU activations.
- The latent space was set to 16 dimensions.
- Training was performed with MSE loss and the Adam optimizer.
- We used early stopping based on reconstruction loss on a validation split.
- 
The objective was not only to minimize reconstruction error but also to ensure that the latent space meaningfully represents player traits — enabling player similarity and trend analysis.
The trained encoder was then used to transform all records into 16D latent vectors, which were later aggregated per player and visualized.

## Testing 
 We tested the model by examining both its reconstruction accuracy and the interpretability of the latent space. 
- Quantitative Evaluation: The model's MSE loss decreased consistently, indicating stable learning of player stats reconstruction.
- Qualitative Evaluation: We reduced the latent space to 2D using PCA and t-SNE to visually inspect how players with similar roles or league affiliations are organized.

Through these evaluations, we found that the Autoencoder captures meaningful structure: players with similar positions tend to appear closer in the embedding space. This confirms that the model did not overfit to noise, and instead learned generalizable patterns from player data.

## Visualize
We visualized the learned latent space of players using PCA and t-SNE, coloring the embeddings by **player position** and **league**.

### Key Observations:

1. **PCA - Position**  
   In the PCA projection, some local structure emerges between player positions (especially between Defenders and Midfielders), although overall separation is limited. This may reflect overlap in feature representations across roles.

2. **t-SNE - Position**  
   While there is no sharp clustering by position, local neighborhoods do show a tendency for similar positions (e.g., Midfielders in green, Defenders in blue) to be near each other. This implies that the model encodes soft distinctions between roles, without rigid boundaries.

3. **PCA - League**  
   No major grouping by league is observed, which suggests the autoencoder generalizes features beyond league-specific styles.

4. **t-SNE - League**  
   Slight regional groupings by league can be seen , potentially capturing differences in play style or team roles across competitions.
   


