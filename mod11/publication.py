class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    
    def print_info(self):
        print(f"Kirja: {self.name}")
        print(f"Kirjoittaja: {self.author}")
        print(f"Sivut: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    
    def print_info(self):
        print(f"Lehti: {self.name}")
        print(f"Päätoimittaja : {self.editor}")




book = Book("Hytti n6", "Rosa Liksom", 200)
magazine = Magazine("Aku Ankka", "Aki Hyyppä")

book.print_info()
magazine.print_info()


