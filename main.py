from repository.book_repository import TextBooksRepository
from repository.user_repository import TextUsersRepository
from repository.booking_repository import TextBookingsRepository
from service.book_service import BooksService
from service.user_service import UsersService
from service.booking_service import BookingsService

from display.user_display import TextUserDisplay
from display.book_display import TextBookDisplay
from display.booking_display import TextBookingDisplay


# Instantiating repository instances for books, users, and bookings
books_repository = TextBooksRepository("books.txt")
users_repository = TextUsersRepository("users.txt")
bookings_repository = TextBookingsRepository("bookings.txt")

# Initializing services for books, users, and bookings using their respective repositories
books_service = BooksService(books_repository)
users_service = UsersService(users_repository)
bookings_service = BookingsService(bookings_repository)


def display_menu():
    print("===== Book Management System =====")
    print("1. Tampilkan Display Buku")
    print("2. Tampilkan Display Pengguna")
    print("3. Tampilkan Display Peminjaman")

    print("0. Keluar")
    print("=================================")


def display_menu_buku():
    print("\n===== Menu Buku =====")
    print("1. Tampilkan Semua Buku")
    print("2. Tambah Buku")
    print("3. Perbarui Informasi Buku")
    print("4. Hapus Buku")
    print("0. Kembali")
    print("======================")


def display_menu_pengguna():
    print("\n===== Menu Buku =====")
    print("1. Tampilkan Pengguna Buku")
    print("2. Tambah Pengguna Buku")
    print("3. Perbarui Informasi Buku")
    print("4. Hapus Buku")
    print("0. Kembali")
    print("======================")


def display_menu_peminjam():
    print("\n===== Menu Buku =====")
    print("1. Tampilkan Pinjam Buku")
    print("2. Tambah Pinjam Buku")
    print("3. Perbarui Informasi Pinjam Buku")
    print("4. Hapus Buku")
    print("0. Kembali")
    print("======================")


def main():
    while True:
        display_menu()
        choice = input("Pilih operasi yang ingin Anda lakukan: ")

        if choice == "1":
            display_menu_buku()
            display_buku = TextBookDisplay(service=books_service)

            choice_buku = input("Pilih operasi untuk buku: ")

            if choice_buku == "1":
                display_buku.all_books()
            elif choice_buku == "2":
                display_buku.create_book()
            elif choice_buku == "3":
                display_buku.update_book()
            elif choice_buku == "4":
                display_buku.delete_book()
            elif choice_buku == "0":
                continue
            else:
                print("Pilihan tidak valid. Silakan pilih operasi yang sesuai.")

        elif choice == "2":
            display_menu_pengguna()
            display_user = TextUserDisplay(service=users_service)

            choice_pengguna = input("Pilih operasi untuk pengguna buku: ")

            if choice_pengguna == "1":
                display_user.all_users()
            elif choice_pengguna == "2":
                display_user.create_user()
            elif choice_pengguna == "3":
                display_user.update_user()
            elif choice_pengguna == "4":
                display_user.delete_user()
            elif choice_pengguna == "0":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih operasi yang sesuai.")

        elif choice == "3":
            display_menu_peminjam()

            display_booking = TextBookingDisplay(service=bookings_service)

            choice_booking = input("Pilih operasi untuk booking buku: ")
            if choice_booking == "1":
                display_booking.all_bookings()

            elif choice_booking == "2":
                display_booking.create_booking()

            elif choice_pengguna == "3":
                display_booking.update_booking()

            elif choice_booking == "4":
                display_booking.delete_booking()
            elif display_booking == "0":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih operasi yang sesuai.")

        elif choice == "0":
            print("Terima kasih! Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih operasi yang sesuai.")


if __name__ == "__main__":
    main()
