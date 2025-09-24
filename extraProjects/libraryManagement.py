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
                        break 
                    elif book_name==x[1] and int(x[3])>0:
                        print("book not available for borrow")
                        break
                    else:
                        print("invalid entry")
        
