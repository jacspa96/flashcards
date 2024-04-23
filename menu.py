import random
import logging
from sys import stdout
from io import StringIO

DEFINITION_KEY = "definition"
MISTAKES_KEY = "mistakes"


class Menu:
    def __init__(self):
        self.text_stream = StringIO()
        self.logger = self.__setup_logging()
        self.cards = {}

    def __setup_logging(self) -> logging.Logger:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_handlers = logging.StreamHandler(stdout), logging.StreamHandler(self.text_stream)
        for log_handler in log_handlers:
            log_handler.setFormatter(logging.Formatter("%(message)s"))
            logger.addHandler(log_handler)
        return logger

    def get_and_log_user_input(self, prompt: str) -> str:
        self.logger.info(prompt)
        value = input()
        print(value, file=self.text_stream)
        return value

    def add_card(self) -> None:
        term = self.get_and_log_user_input(f"The card:")
        while term in self.cards.keys():
            term = self.get_and_log_user_input(f'The term "{term}" already exists. Try again:')

        definition = self.get_and_log_user_input(f"The definition of the card:")
        previous_definitions = [term_info[DEFINITION_KEY] for term_info in self.cards.values()]
        while definition in previous_definitions:
            definition = self.get_and_log_user_input(f'The definition "{definition}" already exists. Try again:')

        self.cards[term] = {DEFINITION_KEY: definition, MISTAKES_KEY: 0}
        self.logger.info(f'The pair ("{term}":"{definition}") has been added.')

    def remove_card(self) -> None:
        term = self. get_and_log_user_input("Which card?")
        try:
            self.cards.pop(term)
        except KeyError:
            self.logger.warning(f'Can\'t remove "{term}": there is no such card.')
        else:
            self.logger.info("The card has been removed.")

    def import_cards(self) -> None:
        file_name = self.get_and_log_user_input("File name:")
        try:
            file = open(file_name)
            lines = file.readlines()
            num_of_lines = len(lines)
            assert num_of_lines % 3 == 0, ("Can't import cards: number of lines not divisible by 3 "
                                           "-> uneven number of terms, definitions and/or mistakes counters!")
        except FileNotFoundError:
            self.logger.warning("File not found.")
        except AssertionError as assertionError:
            self.logger.error(assertionError)
        else:
            lines = [line.strip() for line in lines]
            for i in range(0, num_of_lines - 1, 3):
                term = lines[i]
                definition = lines[i + 1]
                mistakes = lines[i + 2]
                self.cards[term] = {DEFINITION_KEY: definition, MISTAKES_KEY: mistakes}
            self.logger.info(f"{num_of_lines // 3} cards have been loaded.")

    def export_cards(self) -> None:
        file_name = self.get_and_log_user_input("File name:")
        with open(file_name, "w") as f:
            for term, term_info in self.cards.items():
                f.write(term + "\n")
                f.write(term_info[DEFINITION_KEY] + "\n")
                f.write(str(term_info[MISTAKES_KEY]) + "\n")
        num_of_cards = len(self.cards)
        self.logger.info(f"{num_of_cards} cards have been saved.")

    def ask_about_cards(self) -> None:
        num_of_cards = int(self.get_and_log_user_input("How many times to ask?"))
        terms = random.choices(list(self.cards.keys()), k=num_of_cards)
        for term in terms:
            answer = self.get_and_log_user_input(f'Print the definition of "{term}":')
            definition = self.cards[term][DEFINITION_KEY]
            if answer == definition:
                self.logger.info("Correct!")
            elif answer in [term_info[DEFINITION_KEY] for term_info in self.cards.values()]:
                correct_term = self._find_correct_term(answer)
                self.logger.info(f'Wrong. The right answer is "{definition}", '
                                 f'but your definition is correct for "{correct_term}".')
                self.cards[term][MISTAKES_KEY] += 1
            else:
                self.logger.info(f'Wrong. The right answer is "{definition}".')
                self.cards[term][MISTAKES_KEY] += 1

    def write_logs(self) -> None:
        file_name = self.get_and_log_user_input("File name:")
        with open(file_name, "w") as f:
            f.write(self.text_stream.getvalue())
        self.logger.info("The log has been saved.")

    def find_the_hardest_terms(self) -> None:
        max_mistakes = max((term_info[MISTAKES_KEY] for term_info in self.cards.values()), default=0)
        if max_mistakes == 0:
            self.logger.info("There are no cards with errors.")
            return
        terms_with_most_mistakes = [term for term in self.cards
                                    if self.cards[term][MISTAKES_KEY] == max_mistakes]
        num_of_terms = len(terms_with_most_mistakes)
        if num_of_terms == 1:
            self.logger.info(f'The hardest card is "{terms_with_most_mistakes[0]}". '
                             f'You have {max_mistakes} errors answering it')
        else:
            terms_to_be_printed = '", '.join(terms_with_most_mistakes)
            self.logger.info(f'The hardest cards are "{terms_to_be_printed}". '
                             f'"You have {max_mistakes} errors answering them."')

    def reset_mistakes_count(self) -> None:
        for term in self.cards:
            self.cards[term][MISTAKES_KEY] = 0
        self.logger.info("Card statistics have been reset.")

    def _find_correct_term(self, answer: str) -> str:
        for aux_term in self.cards:
            if self.cards[aux_term][DEFINITION_KEY] == answer:
                return aux_term
