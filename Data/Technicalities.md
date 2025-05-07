This documents the technical and minor notes and details about the code

## Raw Data
The data scraped contains all information SofaScore keeps track, which means some or all stats won't be available for some leagues.
**Stats** -
[Player	Player_ID (unique to player)	Team	Goals	Assists	Total tackles	Accurate passes	Duels (won)	Ground duels (won)	Aerial duels (won)	Minutes played	Position	Sofascore Rating	Shots on target	Expected Goals (xG)	Shots off target	Shots blocked	Dribble attempts (succ.)	Notes Attack	Defensive actions	Clearances	Blocked shots	Interceptions	Dribbled past	Notes Defence	Touches	Key passes	Crosses (acc.)	Long balls (acc.)	Notes Passing	Possession lost	Fouls	Was fouled	Offsides	Saves	Goals prevented	Punches	Runs out (succ.)	High claims	Notes Goalkeeper]

[Home/Away	Date	Score] are added seperatly from main scrpaing

*all field players have GK attributes with 0 padded.


## Scraper - notes and workflow
*input should match text from sofaScore site
*Nulls and dashes are replaced by 0, some special cases (dash in name) are treated yet maybe be missed
Sofa score site is loaded and then according to input, expands the countries list and locates country. Then we click on input league on go to matching season. By date (sorting) button is clicked and all URLs in the given time span are collected.
*many HTML elements are prone to change or hardcoded so keep in mind if code is not working properly
*scraper may crash from time to time with no apparent reason, another run sometimes do fix it
The second part goes through all of the URLs, and then performs for each one the following: Opens it, clicks on player stats nutton, and iterates over all tables, and for each table in a single game scrapes the content and joins it to earlier (same match) tables.
This occurs for each game and afterwards, each game (approx. 30 rows, one for each player) is stacked with other games in the scraping process, resulting in one DataFrame to converts to Excel that contains all performances.
*This process is more fluent, yet important to note that SofaScore may contain invalid data (e.g. 0 minutes played) which could disrupt future machine training.


## Preprocess workflow
This script processes raw SofaScore player match data into a clean, structured format suitable for modeling and analysis. It handles multiple layers of data preparation to ensure consistency, interpretability, and normalization across different seasons and formats.
The pipeline starts by resolving season-specific inconsistencies in date formats, assigning correct years to ambiguous or shortened dates. It then parses performance metrics that are originally stored in compound formats—for example, "10 (6)" becomes 10 Total and 6 Successful, and pass completion stats like "45/60" are split into successful attempts and totals.
*Coulmns dropped - duels won and defensive action are both sums of other categories, notes can be used after making them categorical, and rating is a benchmark option.
*Code for transforming categories to 
After parsing, all relevant statistics are normalized per 90 minutes of play to enable fair comparisons across players regardless of time on the pitch. Player positions are mapped to numerical values (G=0, D=1/3, M=2/3, F=1) for modeling, and match scores are interpreted to extract goals for and against, based on home or away status.
Missing values are filled with zeros to simplify downstream processing, and columns irrelevant to modeling (such as player names or notes) are dropped. The final output consists of two DataFrames:
A normalized, feature-rich dataset ready for modeling.
A lightweight dataset preserving only original SofaScore ratings for evaluation or separate use.

