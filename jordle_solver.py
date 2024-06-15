CATEGORY_FILE = {
    "AC": "altador_cup/names.txt",
    "p2s": "petpets/names.txt"
              }

def solve_jordle(category, letters, placement):
    if category not in CATEGORY_FILE:
        print("Category must be 'AC' or 'p2s' and is case sensitive.")
        return
    file_path = CATEGORY_FILE[category]

    # Read the URLs from the file
    with open(file_path, 'r') as file:
        all_names = file.read().splitlines()

    names = [] 
    print(all_names)

    for name in all_names:
        if check_letters(name, letters) and check_order(name, placement):
            names.append(name)
    
    print(f"Possible {category} names are {names}")
    return names

def check_letters(word, letters):
    for letter in letters:
        if letter.lower() not in word.lower():
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

# solve_jordle("AC", ["i", "k"], ["_", "i", "_", "_", "_"])