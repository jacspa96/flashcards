num_of_cards = int(input("Input the number of cards:\n"))
cards = []
for i in range(num_of_cards):
    term = input(f"The term for card #{i + 1}:\n")
    definition = input(f"The definition for card #{i + 1}:\n")
    cards.append((term, definition))

for term, definition in cards:
    answer = input(f'Print the definition of "{term}":\n')
    if answer == definition:
        print("Correct!")
    else:
        print(f'Wrong. The right answer is "{definition}".')