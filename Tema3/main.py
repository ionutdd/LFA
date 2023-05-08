with open("gramatica.in", "r") as grammar_file:
    grammar = {}
    for line in grammar_file:
        productions = line.split()
        grammar[productions[0]] = productions[1:]

with open("cuvinte.in", "r") as words_file:
    for word in words_file:
        word = word.strip()
        current_keys = ['S']
        current_index = 0
        word_accepted = True

        while current_index < len(word):
            next_keys = []
            letter = word[current_index]
            for key in current_keys:
                for production in grammar[key]:
                    if production[0] == letter and production[1] not in next_keys:
                        next_keys.append(production[1])
            if not next_keys:
                word_accepted = False
                break
            current_keys = next_keys
            current_index += 1
        
        if word_accepted:
            final_productions = []
            for key in current_keys:
                final_productions.extend(grammar[key])
            if "lambda" in final_productions:
                print("Cuvantul E acceptat")
            else:
                print("Cuvantul NU E acceptat la sfarsit")
        else:
            print("Cuvantul NU E acceptat din prima")
