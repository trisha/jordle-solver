CATEGORY_FILE = {
    "AC": "altador_cup/names.txt",
    "p2s": "petpets/names.txt"
              }

def solve_jordle(category, letters=[], placement=[], nonletters=[]):
    if category not in CATEGORY_FILE:
        print("Category must be 'AC' or 'p2s' and is case sensitive.")
        return
    file_path = CATEGORY_FILE[category]

    # Read the URLs from the file
    with open(file_path, 'r') as file:
        all_names = file.read().splitlines()

    names = [] 
    # print(all_names)

    for name in all_names:
        if check_letters(name, letters, nonletters) and check_order(name, placement):
            names.append(name)
    
    print(f"Possible {category} names are {names}")
    return names

def check_letters(word, letters=[], nonletters=[]):
    for letter in letters:
        if letter.lower() not in word.lower():
            return False
    for nonletter in nonletters:
        if nonletter.lower() in word.lower():
            return False    
    return True

def check_order(word, placement):
    for i, letter in enumerate(placement):
        if letter == "_":
            continue
        else:
            if word[i].lower() != letter.lower():
                return False
    return True

# category={"AC" | "p2s"}, included_letters=[], placement=["_", "_", "_", "_", "_"], excluded_letters=[]
# solve_jordle("AC", ["t", "e", "a"], ["_", "_", "_", "_", "_"], ["r", "s", "l", "u", "n", "c", "h"]) # Note: Xila Kitae is missing cus she's a former player not listed on TDN, but is on JN https://bookofages.jellyneo.net/characters/141/
solve_jordle("AC", ["t", "e", "a"], ["_", "_", "_", "_", "_"], [])
# solve_jordle("p2s", ["t", "a", "l"], ["_", "_", "_", "_", "_"], ["e", "r", "s", "u", "n", "c", "h"])