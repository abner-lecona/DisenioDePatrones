class QuoteTerminalView:
    @staticmethod
    def menu():
        return input("1- Select, 2- Insert, 3- Delete (exit)\n")

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
