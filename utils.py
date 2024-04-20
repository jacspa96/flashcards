import random
import logging
from sys import stdout
from io import StringIO
from typing import Dict

DEFINITION_KEY = "definition"
MISTAKES_KEY = "mistakes"

text_stream = StringIO()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_handlers = logging.StreamHandler(stdout), logging.StreamHandler(text_stream)
for log_handler in log_handlers:
    log_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(log_handler)


def get_and_log_user_input(prompt: str) -> str:
    logger.info(prompt)
    value = input()
    print(value, file=text_stream)
    return value


def add_card(cards: Dict) -> Dict:
    term = get_and_log_user_input(f"The card:")
    while term in cards.keys():
        term = get_and_log_user_input(f'The term "{term}" already exists. Try again:')

    definition = get_and_log_user_input(f"The definition of the card:")
    previous_definitions = [term_info[DEFINITION_KEY] for term_info in cards.values()]
    while definition in previous_definitions:
        definition = get_and_log_user_input(f'The definition "{definition}" already exists. Try again:')

    cards[term] = {DEFINITION_KEY: definition, MISTAKES_KEY: 0}
    logger.info(f'The pair ("{term}":"{definition}") has been added.')
    return cards


def remove_card(cards: Dict) -> Dict:
    term = get_and_log_user_input("Which card?")
    try:
        cards.pop(term)
    except KeyError:
        logger.warning(f'Can\'t remove "{term}": there is no such card.')
    else:
        logger.info("The card has been removed.")
    finally:
        return cards


def import_cards(cards: Dict) -> Dict:
    file_name = get_and_log_user_input("File name:")
    try:
        file = open(file_name)
        lines = file.readlines()
        num_of_lines = len(lines)
        assert num_of_lines % 3 == 0, ("Can't import cards: number of lines not divisible by 3 "
                                       "-> uneven number of terms, definitions and/or mistakes counters!")
    except FileNotFoundError:
        logger.warning("File not found.")
    except AssertionError as assertionError:
        logger.error(assertionError)
    else:
        lines = [line.strip() for line in lines]
        for i in range(0, num_of_lines - 1, 3):
            term = lines[i]
            definition = lines[i + 1]
            mistakes = lines[i + 2]
            cards[term] = {DEFINITION_KEY: definition, MISTAKES_KEY: mistakes}
        logger.info(f"{num_of_lines // 3} cards have been loaded.")
    finally:
        return cards


def export_cards(cards: Dict) -> None:
    file_name = get_and_log_user_input("File name:")
    with open(file_name, "w") as f:
        for term, term_info in cards.items():
            f.write(term + "\n")
            f.write(term_info[DEFINITION_KEY] + "\n")
            f.write(str(term_info[MISTAKES_KEY]) + "\n")
    num_of_cards = len(cards)
    logger.info(f"{num_of_cards} cards have been saved.")


def ask_about_cards(cards: Dict) -> Dict:
    num_of_cards = int(get_and_log_user_input("How many times to ask?"))
    terms = random.choices(list(cards.keys()), k=num_of_cards)
    for term in terms:
        answer = get_and_log_user_input(f'Print the definition of "{term}":')
        definition = cards[term][DEFINITION_KEY]
        if answer == definition:
            logger.info("Correct!")
        elif answer in [term_info[DEFINITION_KEY] for term_info in cards.values()]:
            correct_term = _find_correct_term(cards, answer)
            logger.info(f'Wrong. The right answer is "{definition}", '
                        f'but your definition is correct for "{correct_term}".')
            cards[term][MISTAKES_KEY] += 1
        else:
            logger.info(f'Wrong. The right answer is "{definition}".')
            cards[term][MISTAKES_KEY] += 1

    return cards


def write_logs() -> None:
    file_name = get_and_log_user_input("File name:")
    with open(file_name, "w") as f:
        f.write(text_stream.getvalue())
    logger.info("The log has been saved.")


def find_the_hardest_terms(cards: Dict) -> None:
    max_mistakes = max((term_info[MISTAKES_KEY] for term_info in cards.values()), default=0)
    if max_mistakes == 0:
        logger.info("There are no cards with errors.")
        return
    terms_with_most_mistakes = [term for term in cards
                                if cards[term][MISTAKES_KEY] == max_mistakes]
    num_of_terms = len(terms_with_most_mistakes)
    if num_of_terms == 1:
        logger.info(f'The hardest card is "{terms_with_most_mistakes[0]}". '
                     f'You have {max_mistakes} errors answering it')
    else:
        terms_to_be_printed = '", '.join(terms_with_most_mistakes)
        logger.info(f'The hardest cards are "{terms_to_be_printed}". '
                     f'"You have {max_mistakes} errors answering them."')


def reset_mistakes_count(cards: Dict) -> Dict:
    for term in cards:
        cards[term][MISTAKES_KEY] = 0
    logger.info("Card statistics have been reset.")
    return cards


def _find_correct_term(cards: Dict, answer: str) -> str:
    for aux_term in cards:
        if cards[aux_term][DEFINITION_KEY] == answer:
            return aux_term
