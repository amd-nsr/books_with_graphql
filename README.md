# Books with GraphQL

A small Django project that exposes a `Book` model (title, author) through GraphQL using [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/).

## Requirements

- Python 3.10 or newer (recommended)
- Django 5.2.x and `graphene-django` 3.x

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Apply migrations and create the database:

```bash
python manage.py migrate
```

Optional: create an admin user to manage books in Django Admin:

```bash
python manage.py createsuperuser
```

## Run the server

```bash
python manage.py runserver
```

- **GraphQL (GraphiQL):** [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
- **Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## GraphQL API

**Queries**

- `allBooks` — list all books
- `book(id: Int!)` — one book by primary key

**Mutations**

- `createBook(title: String!, author: String!)` — create a book

### Example (GraphiQL)

```graphql
query {
  allBooks {
    id
    title
    author
  }
}
```

```graphql
mutation {
  createBook(title: "Example", author: "Jane Doe") {
    book {
      id
      title
      author
    }
  }
}
```

## Project layout

- `book_store/` — Django project settings and root GraphQL schema wiring
- `books/` — `Book` model, GraphQL types, queries, and mutations

The default database is SQLite (`db.sqlite3` at the project root). That file is listed in `.gitignore` and is not committed.
