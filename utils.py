import random
from typing import Dict


def add_card(cards: Dict) -> Dict:
    term = input(f"The card:\n")
    while term in cards.keys():
        term = input(f'The term "{term}" already exists. Try again:\n')

    definition = input(f"The definition of the card:\n")
    while definition in cards.values():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')

    cards[term] = definition
    print(f'The pair ("{term}":"{definition}") has been added.')
    return cards


def remove_card(cards: Dict) -> Dict:
    term = input("Which card?\n")
    try:
        cards.pop(term)
    except KeyError:
        print(f'Can\'t remove "{term}": there is no such card.')
    else:
        print("The card has been removed.")
    finally:
        return cards


def import_cards(cards: Dict) -> Dict:
    file_name = input("File name:\n")
    try:
        file = open(file_name)
        lines = file.readlines()
        num_of_lines = len(lines)
        assert num_of_lines % 2 == 0, ("Can't import cards: uneven number of lines "
                                       "-> uneven number of terms and definitions!")
    except FileNotFoundError:
        print("File not found.")
    except AssertionError as assertionError:
        print(assertionError)
    else:
        lines = [line.strip() for line in lines]
        for i in range(0, len(lines) - 1, 2):
            term = lines[i]
            definition = lines[i + 1]
            cards[term] = definition
        print(f"{num_of_lines // 2} cards have been loaded.")
    finally:
        return cards


def export_cards(cards: Dict) -> None:
    file_name = input("File name:\n")
    with open(file_name, "w") as f:
        for term, definition in cards.items():
            f.write(term + "\n")
            f.write(definition + "\n")
    num_of_cards = len(cards)
    print(f"{num_of_cards} cards have been saved.")


def ask_about_cards(cards: Dict) -> None:
    num_of_cards = int(input("How many times to ask?\n"))
    terms = random.choices(list(cards.keys()), k=num_of_cards)
    for term in terms:
        answer = input(f'Print the definition of "{term}":\n')
        definition = cards[term]
        if answer == definition:
            print("Correct!")
        elif answer in cards.values():
            correct_term = [aux_term for aux_term in cards if cards[aux_term] == answer]
            print(f'Wrong. The right answer is "{definition}",'
                  f'but your definition is correct for "{correct_term}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')
