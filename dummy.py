from repository.book_repository import TextBooksRepository
from repository.user_repository import TextUsersRepository
from repository.booking_repository import TextBookingsRepository


repository = TextBooksRepository("books.txt")
repository_user = TextUsersRepository("users.txt")
repository_booking = TextBookingsRepository("bookings.txt")


repository.create_book_with_details(
    "The Great Gatsby", "F. Scott Fitzgerald", "1925", "9780743273565"
)
repository.create_book_with_details(
    "To Kill a Mockingbird", "Harper Lee", "1960", "9780061120084"
)
repository.create_book_with_details("1984", "George Orwell", "1949", "9780451524935")


repository_user.create_user_with_details("John Doe", "john@example.com", "password123")
repository_user.create_user_with_details(
    "Alice Smith", "alice@example.com", "securepwd456"
)
repository_user.create_user_with_details(
    "Bob Johnson", "bob@example.com", "mysecretp@ssword"
)


repository_booking.create_booking_with_details(
    "2023-11-01", "1", "2023-11-08", "2023-11-10", "Pinjam", "0"
)
repository_booking.create_booking_with_details(
    "2023-11-03", "2", "2023-11-10", "2023-11-15", "Pinjam", "0"
)
repository_booking.create_booking_with_details(
    "2023-11-05", "3", "2023-11-12", "2023-11-18", "Pinjam", "0"
)
