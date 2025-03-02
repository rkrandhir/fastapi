from fastapi import Body, FastAPI
app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        

BOOKS = [
    Book(1, "Godaan", "Premchand", "A great book in Hindi", 5),
    Book(2, "Gaban", "Premchand", "A great book in Hindi", 5),
    Book(3, "Puzzle", "Shakuntala Devi", "A Brain Refresher", 5),
    Book(4, "You can win", "Shiv Kheda", "Life changing book", 5),
    Book(5, "Title 1", "Author 1", "Desc of title 1", 2),
    Book(6, "Title 2", "Author 2", "Desc of title 2", 3),
    Book(7, "Title 3", "Author 3", "Desc of title 3", 4)
]

@app.get('/project2/books/')
async def get_books():
    return BOOKS

@app.post('/project2/books/')
async def add_books(newBook = Body()):
    return BOOKS.append(newBook)