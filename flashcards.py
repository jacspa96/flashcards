from utils import (get_and_log_user_input, add_card, remove_card, import_cards,
                   export_cards, ask_about_cards, write_logs,
                   find_the_hardest_terms, reset_mistakes_count)


def start_menu():
    # sys.stdout = logger = Logger()  # redirect stdout to Logger class
    cards = {}
    while True:
        command = get_and_log_user_input("\nInput the action (add, remove, import, "
                                         "export, ask, exit, log, hardest card, reset stats):")
        match command:
            case "add":
                cards = add_card(cards)
            case "remove":
                cards = remove_card(cards)
            case "import":
                cards = import_cards(cards)
            case "export":
                export_cards(cards)
            case "ask":
                cards = ask_about_cards(cards)
            case "log":
                write_logs()
            case "hardest card":
                find_the_hardest_terms(cards)
            case "reset stats":
                reset_mistakes_count(cards)
            case "exit":
                print("Bye bye!")
                break
            case _:
                print("Unknown command!")


if __name__ == '__main__':
    start_menu()
