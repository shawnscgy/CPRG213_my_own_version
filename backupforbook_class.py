class Book:
    GENRE_DICT = {0:'Romance', 1:'Mystery', 2:'Science Fiction',3:'Thriller',
                  4:'Young Adult', 5:'Children\'s Fiction', 6:'Self-help',
                  7:'Fantasy', 8:'Historical Fiction', 9:'Poetry'}
    # Constructor
    def __init__(self, isbn, title, author, genre, availability):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__availability = availability
    # Getter
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre_name(self):
        return Book.GENRE_DICT[self.__genre]
    def get_availability(self):
        if self.__availability == True:
            status = 'Available'
        else:
            status = 'Borrowed'
        return status
    # Setter
    def set_isbn(self, isbn):
        self.__isbn = isbn
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_genre(self, genre):
        self.__genre = genre
    def set_availability(self, availability):
        self.__availability = availability

    def borrow_it(self):
        self.__availability = False
    def return_it(self):
        self.__availability = True
    def __str__(self):
        str = f'{self.__isbn:14} {self.__title:25} {self.__author:25} {self.get_genre_name():<20} {self.get_availability()}'
        return str
  