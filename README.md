# jordle-solver
For solving petpet and Altador Cup Jordle categories


[Jordle](https://www.jellyneo.net/jordle/) is a Wordle game that uses words from Neopets.com, instead of English words. JellyNeo is the Neopets fansite that runs Jordle, hence the J instead of the W.

Sometimes the category is "Altador Cup (AC) player" or "petpet", and there are some obscure 5-letter ones that I wouldn't be able to come up with myself. To save myself the trouble of going through all the AC players or petpet names each time, I decided to create a script to help me. 


# Coding Process
- Scrape AC player names that are 5L by visiting each [team](https://thedailyneopets.com/altador-cup/altador-cup-teams) and looking at the [roster](https://thedailyneopets.com/altador-cup/altador/) for each
- Scrape petpet names that are 5L by viewing all [petpets](https://items.jellyneo.net/search/all-petpets/?limit=75&petpet_colour=1000) in their base color
- Create a script that takes in a set of known letters as well as known letter locations, plus category, to find possible matches
