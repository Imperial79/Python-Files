'''Consider an example of book shop which sells books & video tapes. It’s modelled by Book & Tape classes. These two classes are inherited from the abstract class called Media. The Media class has common data members such as title & publication. The Book class has data member for storing a no. of pages in a book & Tape class has the playing time in a tape. Each class will have method such as read () & show (). Write a program that models this class hierarchy & processes objects using reference to base class only.'''


class Media:

    title = ''
    publ = ''


class Book(Media):
    noOfPages = 0

    def read(self):
        self.title = input('Enter Book Title: ')
        self.publ = input('Enter Book Publication: ')

        self.noOfPages = int(input('Enter No. of Pages: '))

    def show(self):
        print('Book Title - ', self.title)
        print('Book Publication - ', self.publ)
        print('No. of Pages - ', self.noOfPages)


class Tape(Media):
    playingTime = 0

    def read(self):
        self.title = input('Enter Tape Title: ')
        self.publ = input('Enter Tape Publication: ')
        self.playingTime = int(input('Enter Playing Time of Tape: '))

    def show(self):
        print('Tape Title - ', self.title)
        print('Tape Publication - ', self.publ)
        print('Playing Time - ', self.playingTime)


if __name__ == "__main__":
    book = Book()
    tape = Tape()

    book.read()
    tape.read()
    print('-----------------------')
    book.show()
    tape.show()
