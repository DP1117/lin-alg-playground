from tabulate import tabulate
import Interface, EditMatrix, AccessMatrix, ElementaryOperations, EchelonForms

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
            case "32":
                print("\n!!!SCALE A ROW!!!\n")
                matrix = ElementaryOperations.scale_rows(matrix)
            case "33":
                print("\n!!!INTERCHANGE TWO ROWS!!!\n")
                matrix = ElementaryOperations.interchange_rows(matrix)
            case "41":
                print("\n!!!REF FORM!!!\n")
                EchelonForms.ref(matrix)
            case "42":
                print("\n!!!RREF FORM!!!\n")
                EchelonForms.rref(matrix)
            case _:
                print("\n!!!INVALID OPTION!!!\n")
        choice = Interface.menu()
    print("Bye Bye!")

run()