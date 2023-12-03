class TextBookDisplay:
    def __init__(self, service):
        self.service = service

    # Display all available books
    def all_books(self):
        all_book = self.service.get_all_books()

        if all_book:
            print("\nDaftar Buku: ")

            for idx, book in enumerate(all_book):
                print(f"{idx + 1}. {book.strip()}")
        else:
            print("Tidak ada buku")

    # Create a new book entry
    def create_book(self):
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama pengarang: ")
        publish_year = input("Masukkan tahun terbit: ")
        isbn = input("Masukkan ISBN buku: ")

        # Call the service to create a new book with provided details
        self.service.create_book(title, author, publish_year, isbn)

        print("Buku berhasil ditambahkan.")

    # Update an existing book entry
    def update_book(self):
        self.all_books()

        book_id = int(input("Pilih ID buku yang ingin diperbarui: ")) - 1
        if 0 <= book_id < len(self.service.get_all_books()):
            # Collect updated details for the chosen book
            book_id = int(input("Masukkan ID buku yang ingin diupdate: "))
            title = input("Masukkan judul baru (kosongkan jika tidak ingin diubah): ")
            author = input(
                "Masukkan pengarang baru (kosongkan jika tidak ingin diubah): "
            )
            publish_year = input(
                "Masukkan tahun terbit baru (kosongkan jika tidak ingin diubah): "
            )
            isbn = input("Masukkan ISBN baru (kosongkan jika tidak ingin diubah): ")

            # Call the service to update the chosen book
            self.service.update_book(book_id, title, author, publish_year, isbn)

            print("Buku berhasil diperbarui.")

    # Delete an existing book entry
    def delete_book(self):
        self.all_books()

        book_id = int(input("Pilih ID pengguna buku yang ingin dihapus: ")) - 1
        if 0 <= book_id < len(self.service.get_all_books()):
            # Call the service to delete the chosen book
            self.service.delete_book(book_id)
            print("Buku telah dihapus.")
        else:
            print("ID buku tidak valid.")
