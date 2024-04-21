import book as b
# Find
def find_book_by_isbn(book_list, isbn_code):
    index = 0
    for book in book_list:
        if book.get_isbn() == isbn_code:
            break
        index += 1
    else:
        index = -1
    return index

# Return
def return_book(book_list):
    isbn_code = input('Enter the 13-digit ISBN (format 999-999999999): ')
    index = find_book_by_isbn(book_list, isbn_code)
    if index == -1:
        print('No book found with that ISBN.')
    # get the object using index returned, get available status then determine
    else:
        book = book_list[index]
        title = book.get_title()
        isbn = book.get_isbn()
        if book.get_available() == True:
            print(f'\'{title}\' with ISBN {isbn} is not currently borrowed.\n')
        elif book.get_available() == False:
            book.return_it()
            print(f'\'{title}\' with ISBN {isbn} successfully returned.\n')

# Add
def add_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-999999999): ')
    title = input('Enter title: ')
    author = input('Enter author name: ')
    genre_name = input('Enter genre: ')
    # correct genre name until valid
    while genre_name not in b.Book.GENRE_LIST:
        print('Invalid genre. Choices are: ', end='')
        for name in b.Book.GENRE_LIST:
            if name == b.Book.GENRE_LIST[-1]:
                print(name)
            else:
                print(name, end = ', ')
        genre_name = input('Enter genre: ')
    # get genre number
    genre = b.Book.GENRE_LIST.index(genre_name)
    # instantiate a new book, and add to the list
    book = b.Book(isbn, title, author, genre, available = True)
    book_list.append(book)
    print(f'\'{title}\' with ISBN {isbn} successfully added.\n')



def main():
    pass



if __name__ == "__main__":
    main()