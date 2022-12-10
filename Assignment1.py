# Build library management system
import datetime
import os

class LMS: # create object called LMS
    # create a function to create attributes of object
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books
        self.books_dict = {}
        self.borrowed_books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{'books_title':line.split(",")[0],'author':line.split(",")[1].replace("\n", ""), 'status':'Available'}})
            id += 1 

    # create a function to view all book in the library
    def view_books(self):
        print("-----------------------------------List of Books-----------------------------------------------------")
        print("Books ID"," "*(9 - len("Books ID")), "Title"," "*(20 - len("Title")),"Author"," "*(20 - len("Author")), "Status")
        print("-----------------------------------------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key," "*(6),value.get("books_title")," "*(20-len(value.get("books_title"))),value.get("author")," "*(20-len(value.get("author"))), value.get("status"))
    
    # create a function to view all borrowed book in the library
    def view_borrowed_books(self):
        print("-----------------------------------List of Borrowed Books-----------------------------------------------------")
        print("Books ID"," "*(9 - len("Books ID")), "Title"," "*(20 - len("Title")),"Author"," "*(20 - len("Author")),"Lender_name"," "*(15 - len("Author")),"lend_date")
        print("--------------------------------------------------------------------------------------------------------------")
        for key, value in self.borrowed_books_dict.items():
            print(key," "*(6),value.get("books_title")," "*(20-len(value.get("books_title"))),value.get("author")," "*(20 -len(value.get("author"))), value.get("lender_name")," "*(15- len(value.get("lender_name"))),value.get("lend_date"))

    # create a function to borrow books
    def Borrow_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(f"This book is already issued to {self.borrowed_books_dict[books_id]['lender_name']} on {self.borrowed_books_dict[books_id]['lend_date']}")
                return self.Borrow_books()
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.borrowed_books_dict.update({str(books_id):{'books_title':self.books_dict[books_id]['books_title'],'author':self.books_dict[books_id]['author'],'lender_name' : your_name,'lend_date': current_date}})
                self.books_dict[books_id]['status'] = "Unavailable"
                print("Book Borrowed Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Borrow_books()
    
    # create a function to add book into the library
    def add_books(self):
        new_books = input("Enter Books Title : ")
        book_author = input("Enter author Of new book: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines("\n"+ new_books + "," +book_author )
            self.books_dict.update({str(int(max(self.books_dict)) + 1):{'books_title':new_books,'author':book_author,'lender_name':'None','lend_date':'None', 'status':'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")
    
    # create a function to delete a book from the library
    def delete_books(self):
        del_book = input("Enter Book ID: ")
        if del_book in self.books_dict.keys():
            if self.books_dict[del_book]['status'] == 'Available':
                self.books_dict.pop(del_book)
                print("Book has already deleted successfully")
                with open(self.list_of_books, "w") as b:
                    for key, value in self.books_dict.items():
                        if key == max(self.books_dict):
                            b.writelines(value.get("books_title")+","+value.get("books_title"))
                        else:
                            b.writelines(value.get("books_title")+","+value.get("books_title")+"\n")
                            
            elif not self.books_dict[del_book]['status'] == 'Available':
                print("Sorry! This book is being borrowed! You can't delete it")
                return self.delete_books()
        else:
            print("Your del_book doesn't exist! Please enter again")
            return self.delete_books()
    
    # create a function to return book after borrowing
    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.borrowed_books_dict.pop(books_id)
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Returned !!!\n")
        else:
            print("Book ID Not Found !!!")

# main program to run 
if __name__ == "__main__":
    
        mylms = LMS("list_of_books.txt")
        press_key_list = {"1": "View Books", "2": "Borrow Books", "3": "Add Books","4": "Delete a book", "5": "Return Books","6":"View borrowed books", "7": "Quit"}    
        
        key_press = False

        while not (key_press == "7"):
            print(f"\n----------Welcome To FPT's Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)

            key_press = input("Press Key : ")
            if key_press == "1":
                print("\nCurrent Selection : VIEW ALL BOOKS\n")
                mylms.view_books()

            elif key_press == "2":
                print("\nCurrent Selection : BORROW BOOK\n")
                mylms.Borrow_books()
                
            elif key_press == "3":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()
            elif key_press == "4":
                print("\nCurrent Selection : DELETE A BOOK\n")
                mylms.delete_books()
                
            elif key_press == "5":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()

            elif key_press == "6":
                print("\nCurrent Selection : VIEW BORROW BOOKS\n")
                mylms.view_borrowed_books()

            elif key_press == "7":
                break

            else:
                continue