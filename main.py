from tabulate import tabulate
import Interface, EditMatrix, AccessMatrix, ElementaryOperations

matrix = []

def run():
    print("Welcome to the Matrix Calculator!")
    matrix = EditMatrix.create_matrix()
    choice = Interface.menu()
    while(choice != "Exit"):
        match choice:
            case "Return":
                pass
            case "11":
                print("\n!!!CREATE NEW MATRIX!!!\n")
                matrix = EditMatrix.create_matrix()
            case "12":
                print("\n!!!EDIT ENTRY!!!\n")
                matrix = EditMatrix.change_entry(matrix)
            case "21":
                print("\n!!!GET ROW!!!\n")
                AccessMatrix.get_row(matrix)
            case "22":
                print("\n!!!GET COLUMN!!!\n")
                AccessMatrix.get_column(matrix)
            case "31":
                print("\n!!!ADD TWO ROWS!!!\n")
                matrix = ElementaryOperations.add_rows(matrix)
            case _:
                print("\n!!!INVALID OPTION!!!\n")
        choice = Interface.menu()
    print("Bye Bye!")

run()