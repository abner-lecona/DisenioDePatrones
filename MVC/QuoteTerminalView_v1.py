class QuoteTerminalView:
    @staticmethod
    def menu():
        return input("""Teclea el número de la opción que te gustaría seleccionar:
        1: Consulta una cita
        2: Ingresa una cita
        3: Elimina una cita
        exit: Salir\n""")

    @staticmethod
    def select_quote():
        return input("Ingresa el número de cita que deseas ver\n")

    @staticmethod
    def show(quote):
        print(f"La cita es:\n{quote}")

    @staticmethod
    def insert_quote():
        return input("Ingresa la cita\n")

    @staticmethod
    def quote_inserted(index):
        print(f"Se incertó la cita con el índice: {index}")

    @staticmethod
    def delete_quote():
        return input("Ingresa el número de la cita que deseas eliminar\n")

    @staticmethod
    def error(msg):
        print(f"Error: {msg}")
