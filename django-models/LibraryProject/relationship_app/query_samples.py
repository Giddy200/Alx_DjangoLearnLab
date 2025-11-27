

from relationship_app.models import Author, Book, Library, Librarian

def setup_sample_data():
    """
    Creates necessary sample data to execute the queries.
    This function should be run once before calling run_queries().
    """
    print("\n--- Setting Up Sample Data ---")
    
    # 1. Authors
    author_jane, _ = Author.objects.get_or_create(name='Jane Austen')
    author_scott, _ = Author.objects.get_or_create(name='F. Scott Fitzgerald')

    # 2. Librarian (One-to-One prerequisite)
    librarian_alice, _ = Librarian.objects.get_or_create(name='Alice Smith')

    # 3. Library (One-to-One relationship to Librarian)
    # Using update_or_create to handle re-runs
    library_central, _ = Library.objects.update_or_create(
        name='Central Library', 
        defaults={'librarian': librarian_alice}
    )

    # 4. Books (ForeignKey relationship to Author)
    book_pride, _ = Book.objects.get_or_create(title='Pride and Prejudice', author=author_jane)
    book_sense, _ = Book.objects.get_or_create(title='Sense and Sensibility', author=author_jane)
    book_gatsby, _ = Book.objects.get_or_create(title='The Great Gatsby', author=author_scott)

    # 5. Link Books to Library (Many-to-Many relationship)
    # Clear existing links to ensure accurate data before adding
    library_central.book_set.clear() 
    library_central.book_set.add(book_pride, book_sense, book_gatsby)
    
    print("Sample data created and relationships established.")
    return author_jane, library_central

def run_queries(author_jane, library_central):
    """
    Executes and prints the results for the three required relationship queries.
    """
    print("\n" + "="*50)
    print("Executing Required Queries")
    print("="*50)
    
    # --- 1. Query all books by a specific author (One-to-Many: Author -> Book) ---
    print("\n--- Query 1: All books by a specific author ---")
    
    # The 'book_set' manager is automatically created by Django on the Author model 
    # because the Book model has a ForeignKey pointing to Author.
    jane_books = author_jane.book_set.all()
    
    print(f"Books by {author_jane.name}: ({jane_books.count()} found)")
    for book in jane_books:
        print(f"  - {book.title}")

    # --- 2. List all books in a library (Many-to-Many: Library -> Book) ---
    print("\n--- Query 2: All books in a library ---")
    
    # Since the ManyToManyField 'libraries' is on the Book model, the reverse 
    # lookup manager 'book_set' is used on the Library instance.
    library_books = library_central.book_set.all()
    
    print(f"Books available at {library_central.name}: ({library_books.count()} found)")
    for book in library_books:
        print(f"  - {book.title} (Author: {book.author.name})")

    # --- 3. Retrieve the librarian for a library (One-to-One: Library -> Librarian) ---
    print("\n--- Query 3: Retrieve the librarian for a library ---")
    
    # Access the directly related object defined by the OneToOneField on the Library model.
    head_librarian = library_central.librarian
    
    print(f"The Head Librarian for {library_central.name} is:")
    print(f"  - {head_librarian.name}")
    print("="*50)

if __name__ == '__main__':
    # To run this script:
    # 1. Open Django Shell: python manage.py shell
    # 2. Execute: exec(open('relationship_app/query_samples.py').read())
    
    # Note: Ensure you have run python manage.py makemigrations/migrate before executing.
    try:
        author_jane, library_central = setup_sample_data()
        run_queries(author_jane, library_central)
    except Exception as e:
        print(f"\n[ERROR] Could not run queries. Ensure models are migrated and Django is configured.")
        print(f"Details: {e}")