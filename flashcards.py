from menu import Menu


def start_menu():
    flashcards_menu = Menu()
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
                print("Bye bye!")
                break
            case _:
                print("Unknown command!")


if __name__ == '__main__':
    start_menu()
