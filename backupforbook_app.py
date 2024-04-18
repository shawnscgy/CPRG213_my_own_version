import backupforbook_class as b
import os

# Load
def load_books(book_list, file_name):
    
    book_file = open(file_name, 'r')
    number_of_books = 0
    for line in book_file:
        line_list = line.rstrip().split(',')
        isbn = line_list[0]
        title = line_list[1]
        author = line_list[2]
        genre = int(line_list[3])
        if line_list[4] =='True':
            availability = True
        else:
            availability = False
        book = b.Book(isbn, title, author, genre, availability)
        book_list.append(book)
        number_of_books += 1
    book_file.close()
    print('Book catalog has been loaded.')
    return number_of_books

# Menu
def print_menu(menu_title, menu_dict):
    print(menu_title)
    for key,value in menu_dict.items():
        print(f'{key}. {value}')
    selection = input('Enter your selection: ')

    while selection not in menu_dict and selection != '2130':
        print('Invalid option')
        selection = input('Enter your selection: ')
    
    return selection

# Search
def search_books(book_list, search_str):
    search_result = []
    for book in book_list:
        book_str = book.get_isbn() + book.get_title() + book.get_author() + book.get_genre_name()
        search_str.lower()
        if search_str.lower() in book_str.lower():
            search_result.append(book)
    return search_result

# Print books
def print_books(intended_list):
    HEADING_DICT = {'ISBN':14, 'Title':25, 'Author':25, 'Genre':20, 'Availability':12}
    for key, value in HEADING_DICT.items():
        print(key + ' ' * (value - len(key)), end = ' ')
    print()
    for value in HEADING_DICT.values():
        print('-' * value, end = ' ')
    print()
    for book in intended_list:
        print(book)
    

# Borrow
def borrow_book(book_list):
    isbn_code = input('Enter the 13-digit ISBN (format 999-999999999): ')
    index = find_book_by_isbn(book_list, isbn_code)
    if index == -1:
        print('No book found with that ISBN.')
    else:
        book = book_list[index]
        title = book.get_title()
        if book.get_availability() == 'Borrowed':
            print(f'\'{title}\' with ISBN {isbn_code} is not currently available.\n')
        elif book.get_availability() == 'Available':
            book.borrow_it()
            print(f'\'{title}\' with ISBN {isbn_code} successfully borrowed.\n')

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
    else:
        book = book_list[index]
        title = book.get_title()
        isbn = book.get_isbn()
        if book.get_availability() == 'Available':
            print(f'\'{title}\' with ISBN {isbn} is not currently borrowed.\n')
        elif book.get_availability() == 'Borrowed':
            book.return_it()
            print(f'\'{title}\' with ISBN {isbn} successfully returned.\n')

# Add
def add_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-999999999): ')
    title = input('Enter title: ')
    author = input('Enter author name: ')
    genre_name = input('Enter genre: ')
    # Correct genre name
    while genre_name not in b.Book.GENRE_DICT.values():
        print('Invalid genre. Choices are: ', end='')
        for name in b.Book.GENRE_DICT.values():
            if name == b.Book.GENRE_DICT[max(b.Book.GENRE_DICT)]:
                print(name)
            else:
                print(name, end = ',')
        genre_name = input('Enter genre: ')
    # get genre number
    for key, value in b.Book.GENRE_DICT.items():
        if value == genre_name:
            genre = key
    # make a new book instance, and add to the list
    book = b.Book(isbn, title, author, genre, availability = True)
    book_list.append(book)
    print(f'\'{title}\' with ISBN {isbn} successfully added.')

# Remove
def remove_book(book_list):
    isbn_code = input('Enter the 13-digit ISBN (format 999-999999999): ')
    index = find_book_by_isbn(isbn_code)
    if index == -1:
        print('No book found with that ISBN.')
    else:
        book = book_list.pop(index)
        title = book.get_title()
        isbn = book.get_isbn()
        print(f'\'{title}\' with ISBN {isbn} successfully removed.\n')

# Save
def save_books(book_list, file_name):
    book_file = open(file_name, 'w')
    for book in book_list:
        # get isbn title genre
        item_list = [book.get_isbn(), book.get_title(), book.get_author()]
        
        # get genre number
        genre_name = book.get_genre_name()
        for key, value in b.Book.GENRE_DICT.items():
            if value == genre_name:
                genre = str(key)
        item_list.append(genre)

        # get availability
        status = book.get_availability()
        if status == 'Available':
            availability = 'True'
        else:
            availability = 'False'
        item_list.append(availability)
    
        line = ','.join(item_list) + '\n'
        book_file.write(line)
    book_file.close()
    print('Book catalog has been saved.')


def main():
    input('Starting the system ...')
    
    # menu title
    MAIN_MENU_TITLE = '\nReader\'s Guild Library - Main Menu\n' + '=' * 34
    LIB_MENU_TITLE = '\nReader\'s Guild Library - Librarian Menu\n' + '=' * 39
    
    # menu dictionary
    MAIN_MENU_DICT = {'1':'Search for books', '2':'Borrow a book', '3':'Return a book'}
    LIB_MENU_DICT = {'4':'Add a book', '5':'Remove a book', '6':'Print catalog'}
    MENU_EXIT = {'0':'Exit the system'}
    
    # get list loaded by file
    book_list = []
    file_name = input('Enter book catalog filename: ')
    while not os.path.exists(file_name):
        file_name = input('File not found. Re-enter book catalog filename: ')
    load_books(book_list, file_name) # Load
    
    # first tiem load menu
    MAIN_MENU_DICT.update(MENU_EXIT)
    menu_dict = MAIN_MENU_DICT
    menu_title = MAIN_MENU_TITLE
    selection = print_menu(menu_title, menu_dict)

    while selection != 'quit':
        if selection != '2130' and selection != '0':
            match selection:
                case '1':
                    print(f'\n-- {menu_dict["1"]} --')
                    search_str = input('Enter search value: ')
                    search_result = search_books(book_list, search_str)
                    if len(search_result) == 0:
                        print('No matching books found.')
                    else:
                        print_books(search_result)
                case '2':
                    print(f'\n-- {menu_dict["2"]} --')
                    borrow_book(book_list)
                case '3':
                    print(f'\n-- {menu_dict["3"]} --')
                    return_book(book_list)
                case '4':
                    print(f'\n-- {menu_dict["4"]} --')
                    add_book(book_list)
                case '5':
                    print(f'\n-- {menu_dict["5"]} --')
                    remove_book(book_list)
                case '6':
                    print('\n-- Print book catalog --')
                    print_books(book_list)
            selection = print_menu(menu_title, menu_dict)

        elif selection == '0':
            print(f'\n-- {menu_dict["0"]} --')
            save_books(book_list, file_name)
            print('Good bye!')
            selection = 'quit'

            
        else:
            MAIN_MENU_DICT.update(LIB_MENU_DICT)
            MAIN_MENU_DICT.update(MENU_EXIT)
            menu_dict = MAIN_MENU_DICT
            menu_title = LIB_MENU_TITLE
            selection = print_menu(menu_title, menu_dict)

        
       

if __name__ == '__main__':
    main()