# jordle-solver
For solving petpet and Altador Cup Jordle categories


[Jordle](https://www.jellyneo.net/jordle/) is a Wordle game that uses words from Neopets.com, instead of English words. JellyNeo is the Neopets fansite that runs Jordle, hence the J instead of the W.

Sometimes the category is "Altador Cup player" or "petpet", and there are some obscure 5-letter ones that I wouldn't be able to come up with myself. To save myself the trouble of going through all the AC players or p2 names each time, I decided to create a script to help me. 

# How to use
## Run locally
- Clone the repository locally
- Open the `jordle_solver.py` file
- Edit the variables in the function call at bottom of the page
- In your terminal while in the project folder, run `python jordle_solver.py`
- Answer(s) will be printed in your terminal!

## Run on Repl.it
- Copy over `altador_cup/names.txt`, `petpets/names.txt`, and `jordle_solver.py`
- Confirm that the file path names match
- Edit the variables in the function call at bottom of `jordle_solver.py`
- Run the `jordle_solver.py` file

## To re-run the AC player names web scraper,
- In your terminal while in the project folder, run `python altador_cup/get_urls.py` to update the list of Altador Cup teams
- Run `python altador_cup/get_names.py` to update the list of players on each team

## To update the petpet names, 
- Replicate the ChatGPT screenshot OCR process I outlined in `petpets/petpet_scraper.md`

# Coding Plan
- Scrape AC player names that are 5L by visiting each [team](https://thedailyneopets.com/altador-cup/altador-cup-teams) and looking at the [roster](https://thedailyneopets.com/altador-cup/altador/) for each
- Scrape petpet names that are 5L by viewing all [petpets](https://items.jellyneo.net/search/all-petpets/?limit=75&petpet_colour=1000) in their base color
-- JellyNeo doesn't allow scraping so I used ChatGPT to OCR the names from screenshots
- Create a script that takes in a set of known letters as well as known letter locations, plus category, to find possible matches
