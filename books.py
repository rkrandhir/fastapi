from fastapi import Body, FastAPI
app = FastAPI()

BOOKS = [
    {"title": "Book1", "author": "author 1", "subject": "Maths"},
    {'title': 'Book2', 'author': 'author 2', 'subject': 'Maths'},
    {'title': 'Book3', 'author': 'author 3', 'subject': 'English'},
    {'title': 'Book4', 'author': 'author 4', 'subject': 'English'},
    {'title': 'Book5', 'author': 'author 5', 'subject': 'English'},
    {'title': 'Book1', 'author': 'author 6', 'subject': 'Maths'},
]


'''
*********************************************************************
GET API (R)
*********************************************************************
'''

@app.get("/books")
def read_all_books():
    return BOOKS

#using dynamic params
#get the books based on subject in BOOKS
@app.get("/books/")
def read_book(title: str):
    books = []
    for book in BOOKS:
        if (book.get('subject').casefold() == title.casefold()):
            books.append(book)
    return books        

@app.get("/books/{title}")
def get_book_by_title(title: str, subject: str):
    books = []
    for book in BOOKS:
        if (book.get('title').casefold() == title.casefold() and book.get('subject').casefold() == subject.casefold()):
            books.append(book)
    return books        


'''
*********************************************************************
POST API (C)
*********************************************************************
'''

@app.post('/books/add_book')
async def add_book(new_book=Body()):
    BOOKS.append(new_book)
    
    
'''
*********************************************************************
PUT API (U)
*********************************************************************
'''

@app.put('/books/update_books')
async def update_books(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            
'''
*********************************************************************
DELETE API (D)
*********************************************************************
'''


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


'''
*********************************************************************
ASSIGNMENT - GET API
*********************************************************************
'''

@app.get('/books/author/')
async def getBooks(author: str):
    book_list = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_list.append(book)
    return book_list
         
