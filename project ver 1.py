from datetime import timedelta
#######################################################################################################################################################################
class Person():
    def __init__ (self,name,address,contact_number,gender,age):
        self.name=name
        self.address=address
        self.contact_number=contact_number
        self.gender=gender
        self.age=age
    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setaddress (self,address):
        self.address=address

    def getaddress (self):
        return self.address

    def setcontact_number (self,contact_number):
        self.contact_number=contact_number

    def getcontact_number (self):
        return self.contact_number

    def setgender (self,gender):
        self.gender=gender

    def getgender (self):
        return self.gender

    def setage (self,age):
        self.age=age

    def getage (self):
        return self.age
#######################################################################################################################################################################
class Library():
    lib=0
    def __init__(self,name,start_time,end_time,capacity):
        self.library_id=Library.lib
        Library.lib+=1
        self.name=name
        self.start_time=start_time
        self.end_time=end_time
        self.capacity=capacity
        self.current_member=0
        self.library_departments=[]
        self.library_members=[]
        self.members_in=[]

    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setstart_time (self,start_time):
        self.start_time=start_time

    def getstart_time (self):
        return self.start_time

    def setend_time(self,end_time):
        self.end_time=end_time

    def getend_time(self):
        return self.end_time

    def setcapacity(self,capacity):
        self.capacity=capacity

    def getcapacity(self):
        return self.capacity

    def setcurrent_member(self,currnet_member):
        self.current_member=current_member

    def getcurrent_member(self):
        return self.current_member

    def setlibrary_departments(self,library_departments):
        self.library_departments=library_departments

    def getlibrary_departments(self):
        return self.library_departments

    def setlibrary_members(self,library_members):
        self.library_members=libary_members

    def getlibrary_members (self):
        return self.library_members

    def getlibrary_id(self):
        return self.library_id

    def member_enter(self,member_id,enter_time):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                break
            i+=1
        else:
            return None
        if enter_time < self.start_time:
            return None
        if self.capacity==self.current_member:
            return None
        self.current_member+=1
        self.library_members[i].setenter_time(enter_time)
        self.members_in.append(self.library_members[i])
        return 1
    def member_exit  (self,member_id,exit_time):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                break
            i+=1
        else:
            return None
        if exit_time > self.exit_time:
            return None
        j=0
        while j<len(self.members_in):
            if member_id==self.members_in[j].getmember_id():
                break
            j+=1
        else:
            return None
        self.current_member-=1
        del self.members_in[j]
        self.library_members[i].setexit_time(exit_time)
        timein=self.library_members[i].getenter_time - self.library_members[i].getexit_time
        secondsvalue=timein.seconds
        secondsvalue+=1799
        moneyneeded=secondsvalue//1800
        return moneyneeded

    def add_new_department(self,new_department):
        self.library_departments.append(new_department)

    def add_new_member(self,new_member):
        self.library_members.append(new_member)

    def delelte_department_byID (self,department_id):
        i=0
        while i<len(self.library_departments):
            if department_id==self.library_departments[i].getdepartment_id():
                del self.library_departments[i]
            i+=1

    def delelte_member_byID (self,member_id):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                del self.library_members[i]
            i+=1

    def search_department_byID  (self,department_id):
        i=0
        while i<len(self.library_departments):
            if department_id==self.library_departments[i].getdepartment_id():
                return self.library_departments[i]
            i+=1

    def search_member_byID (self,member_id):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                return self.library_members[i]
            i+=1

    def search_librarian_byID (self,librarian_id):
        i=0
        j=0
        while i<len(self.library_departments):
            while j<len(self.library_departments[i].getdepartment_librarians()):
                if self.library_departments[i].getdepartment_librarians()[j].getlibrarian_id()==librarian_id:
                    return self.library_departments[i].getdepartment_librarians()[j]
                j+=1
            i+=1        
            j=0

    def print_department_details(self):
        i=0
        print("departments' details are:")
        while i<len(self.library_departments):
            self.library_departments[i].print_department_details()
            self.library_departments[i].print_author_details()
            self.library_departments[i].print_books_details()
            i+=1

    def print_librarian_details(self):
        i=0
        print("librarians' details are:")
        while i<len(self.library_departments):
            self.library_departments[i].print_librarians_details()
            i+=1

    def print_member_details (self):
        i=0
        print("members' details are:")
        while i<len(self.library_members):
            self.library_members[i].print_member_details()
            i+=1

    def print_library_details(self):
        print("library's name is:",self.name)
        print("library's start time is:",self.start_time)
        print("library's end time is:",self.end_time)
        print("library's capacity is:",self.capacity)
        print("library's ID is:",self.library_id)
        print("library's number of current members is:",self.current_member)
#######################################################################################################################################################################
class Department ():
    did=0
    def __init__(self,name):
        self.name=name
        self.department_authors=[]
        self.department_librarians=[]
        self.department_id=Department.did
        Department.did+=1

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setdepartment_authors (self,department_authors):
        self.department_authors=department_authors

    def getdepartment_authors(self):
        return self.department_authors

    def setdepartment_librarians(self,department_librarians):
        self.department_librarians=department_librarians

    def getdepartment_librarians(self):
        return self.department_librarians

    def getdepartment_id (self):
        return self.department_id

    def add_new_author (self,new_author):
        self.department_authors.append(new_author)

    def add_new_librarian (self,new_librarian):
        self.department_librarians.append(new_librarian)

    def search_book_byID(self,book_id):
        i=0
        while i<len(self.department_authors):
            if (self.department_authors[i].search_book_byID(book_id))!= None:
               return self.department_authors[i].search_book_byID(book_id)
            i+=1

    def search_author_byID(self,author_id):
        i=0
        while i<len(self.department_authors):
            if author_id==self.department_authors[i].getauthor_id():
                return self.department_authors[i]
            i+=1

    def search_librarian_byID(self,librarian_id):
        i=0
        while i<len(department_librarians):
            if librarian_id==self.department_librarians[i].getlibrarian_id():
                return self.department_librarians[i]
            i+=1
    
    def delete_author_byID(self,author_id):
        i=0
        while i<len(self.department_authors):
            if author_id==self.department_authors[i].getauthor_id():
                del self.department_authors[i]
                break
            i+=1

    def delete_librarian_byID(self,librarian_id):
        i=0
        while i<len(department_librarians):
            if librarian_id==self.department_librarians[i].getlibrarian_id():
                del self.department_librarians[i]
                break
            i+=1

    def print_authors_details (self):
        i=0
        print("department's author(s) is(are):")
        while i<len(self.department_authors):
            self.department_authors[i].print_author_details()
            i+=1

    def print_books_details (self):
        i=0
        print("department's book(s) is(are):")
        while i<len(self.department_authors):
            self.department_authors[i].print_books_details()
            i+=1

    def print_librarians_details (self):
        i=0
        print("department's librarian(s) is(are):")
        while i<len(self.department_librarians):
            self.department_librarians[i].print_librarian_details()
            i+=1

    def print_department_details (self):
        print("department's name is:",self.getname())
        print("department's ID is:",self.getdepartment_id())
#######################################################################################################################################################################
class Author (Person):
    aid=0
    def __init__ (self,name,address,contact_number,gender,age):
        self.author_books=[]
        super(Author,self).__init__(name,address,contact_number,gender,age)
        self.author_id=Author.aid
        Author.aid+=1

    def setauthor_books (self,author_books):
        self.author_books=author_books

    def getauthor_books (self):
        return self.author_books

    def getauthor_id (self):
        return self.author_id

    def add_new_book (self,new_book):
        self.author_books.append(new_book)

    def search_book_byID (self,temp_book_id):
        i=0
        while i<len(self.author_books):
            if author_books[i].getbook_id() == temp_book_id :
                return author_books[i]
            i+=1

    def print_books_details (self):
        print(self.getname()+"'s book(s) is(are):")
        i=0
        while i<len(self.author_books):
            self.author_books[i].print_book_details()
            i+=1
            
    def print_author_details(self):
        print("Author's name is:",self.name)
        print("Author's address is:",self.address)
        print("Author's contact number is:",self.contact_number)
        print("Author's gender is:",self.gender)
        print("Author's age is:",self.age)
        print("Author's ID is:",self.author_id)
#######################################################################################################################################################################       
class Librarian (Person):
    lid=0
    def __init__ (self,name,address,contact_number,gender,age):
        self.librarian_department= None
        self.librarian_id=Librarian.lid
        Librarian.lid+=1
        super(Librarian,self).__init__(name,address,contact_number,gender,age)

    def setdepartment (self,department):
        self.librarian_department=department

    def getlibrarian_department (self):
        return self.librarian_department

    def getlibrarian_id(self):
        return self.librarian_id

    def print_librarian_details(self):
        print("librarian's name is:",self.name)
        print("librarian's address is:",self.address)
        print("librarian's contact number is:",self.contact_number)
        print("librarian's gender is:",self.gender)
        print("librarian's age is:",self.age)
        print("librarian's ID is:",self.librarian_id)

    def print_department_details(self):
        print("librarian department is:")
        (self.librarian_department).print_department_details()
#######################################################################################################################################################################
class Member(Person):
    mid=0
    def __init__ (self,name,address,contact_number,gender,age):
        super(Member,self).__init__(name,address,contact_number,gender,age)
        self.member_id=Member.mid
        Member.mid+=1
        self.enter_time=timedelta()
        self.exit_time=timedelta()
        self.books_borrow=[]

    def setenter_time(self,enter_time):
        self.enter_time=enter_time

    def getenter_time(self):
        return self.enter_time

    def setexit_time(self,exit_time):
        self.exit_time=exit_time

    def getexit_time(self):
        return self.exit_time

    def setbooks_borrow(self,books_borrow):
        self.books_borrow=books_borrow

    def getbooks_borrow(self):
        return self.books_borrow

    def getmember_id (self):
        return self.member_id

    def add_new_book_borrow (self,new_book):
        if len(self.books_borrow)<3:
            self.books_borrow.append[new_book]
        else:
            return True

    def search_book_borrow_byID (self,book_id):
        i=0
        while i<len(self.books_borrow):
            if self.books_borrow[i].getbook_id()==book_id:
                return self.books_borrow[i]
            i+=1

    def delete_book_borrow_byID (self,book_id):
        i=0
        while i<len(self.books_borrow):
            if self.books_borrow[i].getbook_id()==book_id:
                del self.books_borrow[i]
            i+=1        

    def print_books_borrow_details (self):
        i=0
        print("member's borrowed book(s) is(are):")
        while i<len(self.books_borrow):
            self.books_borrow[i].print_book_details()
            self.books_borrow[i].print_author_details()
            self.books_borrow[i].print_department_details()
            i+=1

    def print_member_details(self):
        print("member's name is:",self.name)
        print("member's address is:",self.address)
        print("member's contact number is:",self.contact_number)
        print("member's gender is:",self.gender)
        print("member's age is:",self.age)
        print("member's ID is:",self.member_id)
        print("member's enter time is:",self.enter_time)
        print("member's exit time is:",self.exit_time)
#######################################################################################################################################################################
class Book ():
    bid=0
    def __init__ (self,name,author,cnt_copy_book,book_department):
        self.name=name
        self.author=author
        self.cnt_copy_book=cnt_copy_book
        self.cnt_copy_available=cnt_copy_book
        self.cnt_copy_borrow=0
        self.book_department=book_department
        self.book_id=Book.bid
        Book.bid+=1
        
    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setauthor(self,author):
        self.author=author

    def getauthor(self):
        return self.author

    def setcnt_copy_book (self,cnt_copy_book):
        self.cnt_copy_book=cnt_copy_book

    def getcnt_copy_book(self):
        return self.cnt_copy_book

    def setcnt_copy_available(self,cnt_copy_available):
        self.cnt_copy_available=cnt_copy_available

    def getcnt_copy_available (self):
        return self.cnt_copy_available

    def setcnt_copy_borrow (self,cnt_copy_borrow):
        self.cnt_copy_borrow=cnt_copy_borrow

    def getcnt_copy_borrow(self):
        return self.cnt_copy_borrow

    def setbook_department(self,book_department):
        self.book_department=book_department

    def getbook_department(self):
        return self.book_department

    def getbook_id(self):
        return self.book_id

    def increase_cnt_copy (self,addedbooks):
        self.cnt_copy_book+=addedbooks
        self.cnt_copy_available+=addedbooks

    def make_borrow_operation (self):
        self.cnt_copy_available-=1
        self.cnt_copy_borrow+=1

    def make_receive_book_operation (self):
        self.cnt_copy_available+=1
        self.cnt_copy_borrow-=1    

    def print_book_details (self):
        print ("Book's name is:",self.name)
        print ("Book's total count of copies is:",self.cnt_copy_book)
        print ("Book's count of available copies is:",self.cnt_copy_available)
        print ("Book's count of borrowed copies is:",self.cnt_copy_borrow)
        print ("Book's ID",self.book_id)

    def print_author_details(self):
        (self.author).print_author_details()

    def print_department_details(self):
        (self.book_department).print_department_details()
#######################################################################################################################################################################



def createauthor():
    tempname=input("please enter the Author's name:")
    tempaddress=input("please enter the Author's address:")
    tempcontact_number=input("please enter the Author's contact number:")
    tempgender=input("please enter the Author's gender:")
    tempage=input("please enter the Author's age:")
    tempauthor_books=[]
    while 1:
        wannaadd=input("please press y to enter a new book")
        if wannaadd=='y':
                  tempbookname=input("please enter the book's name:")
                  i=0
                  while i<Book.bid:
                      if book[i].getname()==tempbookname:
                          tempauthor_books.append(book[i])
                          break
                      i+=1
        else:
                  break
        
    author.append(Author(tempname,tempaddress,tempcontact_number,tempgender,tempage,tempauthor_books))



def createbook ():
    tempname=input("please enter the book's name:")
    tempcnt_copy_book=int(input("please enter the total number of copies of the book:"))
    tempcnt_copy_available=int(input("please enter the number of available copies:"))
    tempcnt_copy_borrow=int(input("please enter the number of borrowed copies:"))
    tempauthor_name=input("please enter the author's name:")
    tempdepartment_name=input("please enter the department's name:")
    i=0
    while i<Author.aid:
        if author[i].getname()==tempauthor_name:
            tempauthor=author[i]
            break
        i+=1
    i=0
    while i<Department.did:
        if department[i].getname()==tempdepartment_name:
            tempdepartment=department[i]
            break
        i+=1
    book.append(Book(tempname,tempauthor,tempcnt_copy_book,tempcnt_copy_available,tempcnt_copy_borrow,tempdepartment))    

def createlibrarian ():
    tempname=input("please enter the librarian's name:")
    tempaddress=input("please enter the librarian's address:")
    tempcontact_number=input("please enter the librarian's contact number:")
    tempgender=input("please enter the librarian's gender:")
    tempage=input("please enter the librarian's age:")
    tempdepartment_name=input("please enter the department's name:")
    i=0
    while i<Department.did:
        if department[i].getname()==tempdepartment_name:
            tempdepartment=department[i]
            break
        i+=1
    librarian.append(Librarian(tempname,tempaddress,tempcontact_number,tempgender,tempage,tempdepartment))


librarian=[]
author=[]
book=[]
department=[]
member=[]
author.append(Author("author1","address1","01111111111","male","101"))
author.append(Author("author2","address2","02222222222","male","102"))
author.append(Author("author3","address3","03333333333","male","103"))
department.append(Department("department12"))
department.append(Department("department23"))
department.append(Department("department31"))
department[0].setdepartment_authors([author[0],author[1]])
department[1].setdepartment_authors([author[1],author[2]])
department[2].setdepartment_authors([author[2],author[0]])
librarian.append(Librarian("librarian1","address11","00000000001","male","101"))
librarian.append(Librarian("librarian2","address22","00000000002","male","102"))
librarian.append(Librarian("librarian3","address33","00000000003","male","103"))
librarian[0].setdepartment(department[0])
librarian[1].setdepartment(department[1])
librarian[2].setdepartment(department[2])
department[0].setdepartment_librarians([librarian[0]])
department[1].setdepartment_librarians([librarian[1]])
department[2].setdepartment_librarians([librarian[2]])
book.append(Book("book1",author[0],11,department[0]))
book.append(Book("book2",author[1],22,department[1]))
book.append(Book("book3",author[2],33,department[2]))
author[0].setauthor_books([book[0]])
author[1].setauthor_books([book[1]])
author[2].setauthor_books([book[2]])
member.append(Member("member1","address111","01111100000","male","101"))
member.append(Member("member2","address222","02222200000","male","102"))
member.append(Member("member3","address333","03333300000","male","103"))
member[0].setenter_time(timedelta(seconds=13*60*60))
member[1].setenter_time(timedelta(seconds=14*60*60))
member[2].setenter_time(timedelta(seconds=15*60*60))
member[0].setexit_time(timedelta(seconds=14*60*60))
member[1].setexit_time(timedelta(seconds=16*60*60))
member[2].setexit_time(timedelta(seconds=18*60*60))
member[0].setbooks_borrow([book[0]])
member[1].setbooks_borrow([book[0],book[1]])
member[2].setbooks_borrow([book[0],book[1],book[2]])
member[0].print_member_details()
member[1].print_books_borrow_details()






wannaout='y'
whatdoyouwant=""
while wannaout=='y':
    whatdoyouwant=input("what do you want sir/madame:")
    if whatdoyouwant=='create author':
        createauthor()
    elif whatdoyouwant=='print author':
        whatid=int(input("please enter Author's id:"))
        author[whatid].print_author_details()
        author[whatid].print_books_details()        
    elif whatdoyouwant=='create book':
        createbook()
    elif whatdoyouwant=='print book':
        whatid=int(input("please enter book's id:"))
        book[whatid].print_book_details()
        book[whatid].print_author_details()
        book[whatid].print_department_details()
    elif     whatdoyouwant=='add new book':
        tempbook_name=input("please enter book's name:")
        tempauthor_name=input("please enter author's name:")
        i=0
        while i<Author.aid:
            if author[i].getname()==tempauthor_name:
                tempauthor=author[i]
                break
            i+=1

        
        i=0
        while i<Book.bid:
            if book[i].getname()==tempbook_name:
                tempauthor.add_new_book(book[i])
                break
            i+=1
    elif  whatdoyouwant=='create librarian':
        createlibrarian()
    elif whatdoyouwant=='print librarian':
        whatid=int(input("please enter librarian's id:"))
        librarian[whatid].print_librarian_details()
        librarian[whatid].print_department_details()
    wannaout=input("if you want to continue press y:")

























        
