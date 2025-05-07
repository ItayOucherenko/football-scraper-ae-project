This documents the technical and minor notes and details about the code

## Raw Data
The data scraped contains all information SofaScore keeps track, which means some or all stats won't be available for some leagues.
**Stats** -
[Player	Player_ID (unique to player)	Team	Goals	Assists	Total tackles	Accurate passes	Duels (won)	Ground duels (won)	Aerial duels (won)	Minutes played	Position	Sofascore Rating	Shots on target	Expected Goals (xG)	Shots off target	Shots blocked	Dribble attempts (succ.)	Notes Attack	Defensive actions	Clearances	Blocked shots	Interceptions	Dribbled past	Notes Defence	Touches	Key passes	Crosses (acc.)	Long balls (acc.)	Notes Passing	Possession lost	Fouls	Was fouled	Offsides	Saves	Goals prevented	Punches	Runs out (succ.)	High claims	Notes Goalkeeper]

[Home/Away	Date	Score] are added seperatly from main scrpaing

*all field players have GK attributes with 0 padded.


## Scraper - notes and workflow
*input should match text from sofaScore site
Sofa score site is loaded and then according to input, expands the countries list and locates country. Then we click on input league on go to matching season. By date (sorting) button is clicked and all URLs in the given time span are collected.
*many HTML elements are prone to change or hardcoded so keep in mind if code is not working properly
*scraper may crash from time to time with no apparent reason, another run sometimes do fix it
The second part goes through all of the URLs, and then performs for each one the following: Opens it, clicks on player stats nutton, and iterates over all tables, and for each table in a single game scrapes the content and joins it to earlier (same match) tables.
This occurs for each game and afterwards, each game (approx. 30 rows, one for each player) is stacked with other games in the scraping process, resulting in one DataFrame to converts to Excel that contains all performances.
*This process is more fluent, yet important to note that SofaScore may contain invalid data (e.g. 0 minutes played)


## Preprocess workflow

