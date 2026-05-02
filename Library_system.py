def show_help():
    print("Supported commands:")
    print(" ADD_SUBURB <Suburb_Name> <2-digit_Suburb_Code>")
    print(" ADD_MEMBER <Member_Full_Name> <MemberID>")
    print(" ADD_BOOK <Book_Name> <Number_of_Copies>")
    print(" BORROW <MemberID> <Book_Name>")
    print(" RETURN <MemberID> <Book_Name>")
    print(" HELP")
    print(" EXIT")


def add_suburb(parts, suburbs):
    if len(parts) != 3:
        print('Incorrect number of inputs for command ADD_SUBURB. Please use HELP for guidance.')
        return

    suburb_name = parts[1]
    suburb_code = parts[2]

    if not suburb_code.isdigit() or len(suburb_code) != 2:
        print('Incorrect digit code format for ADD_SUBURB command. Please check the details.')
        return

    if suburb_name in suburbs:
        print('The item already exists in the system. Please check the details.')
        return

    suburbs[suburb_name] = suburb_code
    print(f'A new suburb of {suburb_name} with suburb code {suburb_code} has been added to the system.')

def add_member(parts, suburbs, members):
    if len(parts) != 3:
        print('Incorrect number of inputs for command ADD_MEMBER. Please use HELP for guidance.')
        return

    member_name = parts[1]
    member_id = parts[2]

    if not member_id.isdigit() or len(member_id) != 8:
        print('Member ID is not an 8-digit number. Member was not added.')
        return

    if member_id in members:
        print('The item already exists in the system. Please check the details.')
        return

    suburb_code = member_id[:2]
    valid_code = False

    for code in suburbs.values():
        if suburb_code == code:
            valid_code = True

    if valid_code == False:
            print('Incorrect suburb code in member ID. Member was not added.')
            return

    members[member_id] = [member_name, []]
    print(f'A new member with name {member_name} and member ID {member_id} has been added.')
        

def add_book(parts, books):
    if len(parts) != 3:
        print('Incorrect number of inputs for command ADD_BOOK. Please use HELP for guidance.')
        return

    book_name = parts[1]
    book_copies = parts[2]

    if not book_copies.isdigit():
        print('Please provide a correct number of copies.')
        return

    copies = int(book_copies)

    if copies <= 0:
        print('Please provide a correct number of copies.')
        return

    if book_name in books:
        books[book_name][0] = books[book_name][0] + copies
    else:
        books[book_name] = [copies, 0]

    print(f'We now have {book_name} with {books[book_name][0]} copies in our system.')

def borrow_book(parts, members, books):
    if len(parts) != 3:
        print('Incorrect number of inputs for command BORROW. Please use HELP for guidance.')
        return

    member_id = parts[1]
    book_name = parts[2]

    if member_id not in members:
        print(f'ID number: {member_id} is not in the system.')
        return

    if book_name not in books:
        print(f'{book_name} is not in the system.')
        return

    member_name = members[member_id][0]
    borrowed_books = members[member_id][1]

    if len(borrowed_books) >= 2:
        print(f'{member_name} has already borrowed two items. Each member can borrow a maximum of two books.')
        return

    if book_name in borrowed_books:
        print(f'{member_name} has already borrowed this book.')
        return

    total_copies = books[book_name][0]
    borrowed_copies = books[book_name][1]
    available_copies = total_copies - borrowed_copies

    if available_copies <= 0:
        print(f'Dear {member_name}, we are sorry to inform you that we have run out of copies of {book_name}.')
        return

    borrowed_books.append(book_name)
    books[book_name][1] = books[book_name][1] + 1
    print(f'{member_name} has borrowed {book_name}.')

def return_book(parts, members, books):

    if len(parts) != 3:
        print(f'Incorrect number of inputs for command RETURN. Please use HELP for guidance.')
        return

    member_id = parts[1]
    book_name = parts[2]

    if member_id not in members:
        print(f'ID number: {member_id} is not in the system.')
        return

    if book_name not in books:
        print(f'{book_name} is not in the system.')
        return

    member_name = members[member_id][0]
    borrowed_books = members[member_id][1]

    if book_name not in borrowed_books:
        print(f'Dear {member_name} you cannot return {book_name}, because you never borrowed it!')
        return

    borrowed_books.remove(book_name)
    books[book_name][1] = books[book_name][1] - 1
    print(f'{member_name} has returned {book_name}.')


def main():
    suburbs = {}
    members = {}
    books = {}

    print('Welcome to the Sutherland Shire Library Management System!')

    while True:
        command_line = input('Enter command: ')
        parts = command_line.split()

        if len(parts) == 0:
            continue

        command = parts[0]

        if command == 'ADD_SUBURB':
            add_suburb(parts, suburbs)

        elif command == 'ADD_MEMBER':
            add_member(parts, suburbs, members)

        elif command == 'ADD_BOOK':
            add_book(parts, books)

        elif command == 'BORROW':
            borrow_book(parts, members, books)

        elif command == 'RETURN':
            return_book(parts, members, books)

        elif command == 'HELP':
            if len(parts) != 1:
                print('Incorrect number of inputs for command HELP. Please use HELP for guidance.')
            else:
                show_help()

        elif command == "EXIT":
            if len(parts) != 1:
                print('Incorrect number of inputs for command EXIT. Please use HELP for guidance.')
            else:
                print('Goodbye!')
                break

        else:
            print(f'Incorrect number of inputs for command {command}. Please use HELP for guidance.')


main()

