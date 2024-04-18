num_of_cards = int(input("Input the number of cards:\n"))
cards = {}
for i in range(num_of_cards):
    term = input(f"The term for card #{i + 1}:\n")
    while term in cards.keys():
        term = input(f'The term "{term}" already exists. Try again:\n')

    definition = input(f"The definition for card #{i + 1}:\n")
    while definition in cards.values():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')

    cards[term] = definition

for term, definition in cards.items():
    answer = input(f'Print the definition of "{term}":\n')
    if answer == definition:
        print("Correct!")
    elif answer in cards.values():
        correct_term = [aux_term for aux_term in cards if cards[aux_term] == answer]
        print(f'Wrong. The right answer is "{definition}", \
                but your definition is correct for "{correct_term}".')
    else:
        print(f'Wrong. The right answer is "{definition}".')
