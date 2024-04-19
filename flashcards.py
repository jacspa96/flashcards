from utils import add_card, remove_card, import_cards, export_cards, ask_about_cards


def start_menu():
    cards = {}
    while True:
        command = input("\nInput the action (add, remove, import, export, ask, exit):\n")
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
                ask_about_cards(cards)
            case "exit":
                print("Bye bye!")
                break
            case _:
                print("Unknown command!")


if __name__ == '__main__':
    start_menu()
