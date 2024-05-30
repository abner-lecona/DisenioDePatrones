quotes = [
    "As I said before, I never repeat myself",
    "No free lunch",
    "May the Force be with you"
]

class QuoteModel:
    @staticmethod
    def get_quote(index):
        try:
            value = quotes[index]
            return value
        except IndexError:
            raise IndexError(f"Índice no válido: {index}")

    @staticmethod
    def insert_quote(quote):
        quotes.append(quote)
        return len(quotes) - 1

    @staticmethod
    def remove_quote(index):
        try:
            quotes.pop(index)
        except IndexError:
            raise IndexError(f"Índice no válido: {index}")