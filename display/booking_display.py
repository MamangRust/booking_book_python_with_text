from datetime import datetime


class TextBookingDisplay:
    def __init__(self, service_booking, service_user, service_book) -> None:
        self.service_booking = service_booking
        self.service_user = service_user
        self.service_book = service_book

    # Display all existing bookings
    def all_bookings(self):
        all_bookings = self.service_booking.get_all_bookings()

        if all_bookings:
            print("\nDaftar Booking Buku")

            for idx, booking in enumerate(all_bookings):
                print(f"{idx + 1}. {booking.strip()}")
        else:
            print("Tidak ada booking buku")

    # Create a new booking entry
    def create_booking(self):
        # Display lists of users and books
        print("\n Daftar User")
        print(self.service_user.get_all_users())

        print("\n Daftar Book")
        print(self.service_book.get_all_books())

        # Collect booking details from user input
        tgl_pinjam = input("Masukkan Tanggal Peminjaman buku (YYYY-MM-DD): ")
        user_id = input("Masukkan User id: ")
        tgl_kembali = input("Masukkan Tanggal Kembali Buku (YYYY-MM-DD): ")
        tgl_pengembalian = input("Masukkan Tanggal Pengembalian Buku (YYYY-MM-DD): ")
        status = input("Masukkan Status (Kembali/Pinjam): ")
        total_denda = input(
            "Masukkan Denda buku (Jika terjadi keterlambatan kembali buku): "
        )

        try:
            # Convert input dates to datetime objects
            tgl_pinjam = datetime.strptime(tgl_pinjam, "%Y-%m-%d")
            tgl_kembali = datetime.strptime(tgl_kembali, "%Y-%m-%d")
            tgl_pengembalian = datetime.strptime(tgl_pengembalian, "%Y-%m-%d")
        except ValueError:
            print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
            return

        # Call the service to create a new booking with provided details
        self.service_booking.create_booking(
            tgl_pinjam, user_id, tgl_kembali, tgl_pengembalian, status, total_denda
        )

    # Update an existing booking entry
    def update_booking(self):
        self.all_bookings()

        booking_id = int(input("Pilih ID booking buku yang ingin diperbarui: ")) - 1
        if 0 <= booking_id < len(self.service.read_all_bookings()):
            # Display lists of users and books for reference
            print("\n Daftar User")
            print(self.service_user.get_all_users())

            print("\n Daftar Book")
            print(self.service_book.get_all_books())

            # Collect updated booking details from user input
            tgl_pinjam = input("Masukkan Tanggal Peminjaman buku (YYYY-MM-DD): ")
            user_id = input("Masukkan User id: ")
            tgl_kembali = input("Masukkan Tanggal Kembali Buku (YYYY-MM-DD): ")
            tgl_pengembalian = input(
                "Masukkan Tanggal Pengembalian Buku (YYYY-MM-DD): "
            )
            status = input("Masukkan Status (Kembali/Pinjam): ")
            total_denda = input(
                "Masukkan Denda buku (Jika terjadi keterlambatan kembali buku): "
            )

            try:
                # Convert input dates to datetime objects
                tgl_pinjam = datetime.strptime(tgl_pinjam, "%Y-%m-%d")
                tgl_kembali = datetime.strptime(tgl_kembali, "%Y-%m-%d")
                tgl_pengembalian = datetime.strptime(tgl_pengembalian, "%Y-%m-%d")
            except ValueError:
                print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
                return

            # Call the service to update the chosen booking
            self.service_booking.update_booking(
                booking_id,
                tgl_pinjam,
                user_id,
                tgl_kembali,
                tgl_pengembalian,
                status,
                total_denda,
            )

            print("Informasi booking buku telah diperbarui.")
        else:
            print("ID booking buku tidak valid.")

    # Delete an existing booking entry
    def delete_booking(self):
        self.all_bookings()

        booking_id = int(input("Pilih ID booking buku yang ingin diperbarui: ")) - 1
        if 0 <= booking_id < len(self.service.read_all_bookings()):
            # Call the service to delete the chosen booking
            self.service_booking.delete_booking(booking_id)

            print("Booking buku telah dihapus.")
        else:
            print("ID Booking buku tidak valid")
