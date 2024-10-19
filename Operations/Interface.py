# Showing menu options
@staticmethod
def show(list):
    print("-" * 20)
    i = 1
    for option in list:
        print(option + f"({i})")
        i += 1
    print("-" * 20)
    print("Enter an option: ", end="")
    return int(input())


# Calculator home
@staticmethod
def menu():
    options = {
        "Edit Matrix": ["Create a new matrix", "Change an entry"],
        "Access Matrix": ["Return a row", "Return a column"],
        "Perform Elementary Row Operations": ["Add rows", "Scale Rows", "Interchange rows"],
        "Compute Echelon Forms": {"REF, RREF"},
    }
    # General list
    general_choice = show(list(options.keys()) + ["Exit"])

    if general_choice == len(options) + 1:
        return "Exit"
    elif general_choice < 1 or general_choice > len(options) + 1:
        print("Invalid option")
        menu()

    choice = options[list(options.keys())[general_choice - 1]]

    # Sub list
    sub_choice = show(choice + ["Return"])

    if sub_choice == len(choice) + 1:
        return "Return"

    return str(general_choice) + str(sub_choice)