import argparse
from menu import Menu


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--import_from")
    parser.add_argument("--export_to")
    args = parser.parse_args()
    return args.import_from, args.export_to


def main():
    flashcards_menu = Menu()

    import_from, export_from = parse_args()
    if import_from is not None:
        flashcards_menu.import_cards(import_from)

    while True:
        command = flashcards_menu.get_and_log_user_input("\nInput the action (add, remove, import, "
                                                         "export, ask, exit, log, hardest card, reset stats):")
        match command:
            case "add":
                flashcards_menu.add_card()
            case "remove":
                flashcards_menu.remove_card()
            case "import":
                flashcards_menu.import_cards()
            case "export":
                flashcards_menu.export_cards()
            case "ask":
                flashcards_menu.ask_about_cards()
            case "log":
                flashcards_menu.write_logs()
            case "hardest card":
                flashcards_menu.find_the_hardest_terms()
            case "reset stats":
                flashcards_menu.reset_mistakes_count()
            case "exit":
                if export_from is not None:
                    flashcards_menu.export_cards(export_from)
                else:
                    print("Bye bye!")
                break
            case _:
                print("Unknown command!")


if __name__ == '__main__':
    main()
