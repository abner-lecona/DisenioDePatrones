from QuotesModel import *
from QuoteTerminalView import *

class QuoteTerminalController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):
        while True:
            try:
                user_input = self.view.menu()
                if user_input == "exit":
                    break
                option = int(user_input)
                if option == 1:
                    user_input = self.view.select_quote()
                    i = int(user_input)
                    quote = self.model.get_quote(i)
                    self.view.show(quote)
                elif option == 2:
                    user_input = self.view.insert_quote()
                    i = self.model.insert_quote(user_input)
                    self.view.quote_inserted(i)
                elif option == 3:
                    user_input = self.view.delete_quote()
                    i = int(user_input)
                    self.model.remove_quote(i)
                    print(f"La cita con el índice {i} ha sido eliminada")
                else:
                    raise IndexError
            except ValueError:
                self.view.error("Entrada no válida. Por favor, ingrese un número.")
            except IndexError as e:
                self.view.error(e)

def main():
    model = QuoteModel()
    view = QuoteTerminalView()
    controller = QuoteTerminalController(view, model)
    controller.run()

main()
