import graphene
from graphene_django import DjangoObjectType
from .models import Book

# Define a GraphQL type for Book
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author")

# Queries (read)
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int(required=True))

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        return Book.objects.get(pk=id)

# -------------------

# Mutations (write)
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, title, author):
        book = Book.objects.create(title=title, author=author)
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
