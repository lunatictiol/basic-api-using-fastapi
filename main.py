
from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {'title': 'book1', 'author': 'author1','category': 'science'},
    {'title': 'book2', 'author': 'author2','category': 'math'},
    {'title': 'book2', 'author': 'author2','category': 'math'},
    {'title': 'book2', 'author': 'author2','category': 'math'},
    {'title': 'book2', 'author': 'author2','category': 'math'},
    {'title': 'book2', 'author': 'author2','category': 'math'},
    {'title': 'book3', 'author': 'author3','category': 'science'},
    {'title': 'book4', 'author': 'author4','category': 'math'},
    {'title': 'book5', 'author': 'author5','category': 'science'},

]

@app.delete("/books/{title}")
async def delete_book(title: str):
    for i in range(len(books)):
        if books[i].get('title').casefold() == title.casefold():
            books.pop(i)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}

@app.put("/books/{title}")
async def update_book(title: str, book=Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == title.casefold():
            books[i] = book
            return {"message": "Book updated","book":book}
    return {"message": "Book not found","book":{}}

@app.post("/books/create")
async def create_book(book=Body()):
    books.append(book)
    return {"message": "Book created","book":book}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    return {"books": books}

#qury parameters
@app.get("/books/{title}")
async def get_books_by_title(title: str):
    for book in books:
        if book['title'].casefold() == title.casefold():
            return { "message":"Book found","book":book}
    return {"message": "Book not found","book":{}}


@app.get("/books/")
async def get_books_by_category(category: str):
    books_found = []
    for book in books:
        if book['category'].casefold() == category.casefold():
            books_found.append(book)
    if books_found:
        return { "message":"Books found","books":books_found}
    return {"message": "Books not found","books":{}}
@app.get("/books/{author}/")
async def get_books_by_author_and_category(author: str,category: str):
    books_found = []
    for book in books:
        if book['author'].casefold() == author.casefold() and book['category'].casefold() == category.casefold():
            books_found.append(book)
    if books_found:
        return { "message":"Books found","books":books_found}
    return {"message": "Books not found","books":{}}