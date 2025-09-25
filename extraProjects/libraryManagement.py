import csv
while True:
    print("1. borrow a book")
    print("2. return a book")
    print("3. search book")
    print("4. add new books")
    print("5. exit")
    choice=int(input("enter a option from above"))
    match choice:
        case 1:
            book_name=input("enter book name:")
            with open("books.csv") as b:
                find=csv.reader(b)
                next(find)
                for x in find:
                    if book_name==x[1] and int(x[3])>0:
                        print("book available")
                        remain=str(int(x[3]))
                        print("remaining books",remain)
                        borrow=input(f"do you want to borrow {book_name}?(YES/NO)")
                        if borrow.lower()=="yes":
                            borrowed=True
                            remain=int(remain)-1
                            print(f"you borrowed book {book_name}")
                            print("Now remaining books",remain)
                        else:
                            print("borrowing canceled")
                            break
                        break 
                    elif book_name==x[1] and int(x[3])>0:
                        print("book not available for borrow")
                        break
                    else:
                        print("invalid entry")
        case 2:
            book_name=input("enter the book name:")
            with open("books.csv") as b:
                find=csv.reader(b)
                next(find)
                for x in find:
                    if x[1]==book_name:
                        print("you returned book")
                        remain=int(remain)+1
                        print(f"the number of {book_name} is:",remain)
        case 3:
            print("i. search book by name")
            print("ii. search book by author name")
            print("iii. cancel searching")
            view=(input("enter your choice:"))
            match view:
                case 'i':
                    book_name=input("enter book's name:")
                    with open("books.csv") as b:
                        find=csv.reader(b)
                        next(find)
                        for x in find:
                            if book_name==x[1] and int(x[3])>0:
                                print("book available")
                                print(b.readline())
                case 'ii':
                    author_name=input("enter author name:")
                    with open("books.csv") as b:
                        find=csv.reader(b)
                        next(find)
                        for x in find:
                            if author_name.lower()==x[2]:
                                print(f"book of author {author_name} is available")
                                print(b.readline)
                case 'iii':
                    print("searching cancelled")
                    break
        case 4:
            id=input("enter book id")
            book_name=(input("enter book's name:")).lower()
            book_author=(input("enter book's author name:")).lower()
            quantity=input("enter the number of books to add:")
            new_data=[id,book_name,book_author,quantity]
            with open("books.csv","a",newline="") as b:
                writer=csv.writer(b)
                writer.writerow(new_data)
            print("new book added")
        case 5:
            break
