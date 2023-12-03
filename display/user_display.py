class TextUserDisplay:
    def __init__(self, service):
        self.service = service

    # Display all existing users of the book service
    def all_users(self):
        all_users = self.service.read_all_users()

        if all_users:
            print("\nDaftar Pengguna Buku: ")

            for idx, user in enumerate(all_users):
                print(f"{idx + 1}. {user.strip()}")
        else:
            print("Tidak ada pengguna buku")

    # Create a new user for the book service
    def create_user(self):
        name = input("Masukkan nama pengguna: ")
        email = input("Masukkan alamat email: ")
        password = input("Masukkan kata sandi: ")

        # Call the service to create a new user with provided details
        self.service.create_user(name, email, password)
        print("Pengguna buku telah ditambahkan.")

    # Update an existing user's information
    def update_user(self):
        self.all_users()

        user_id = int(input("Pilih ID pengguna buku yang ingin diperbarui: ")) - 1
        if 0 <= user_id < len(self.service.read_all_users()):
            name = input(
                "Masukkan nama baru (biarkan kosong jika tidak ingin mengubah): "
            )
            email = input(
                "Masukkan email baru (biarkan kosong jika tidak ingin mengubah): "
            )
            password = input(
                "Masukkan kata sandi baru (biarkan kosong jika tidak ingin mengubah): "
            )

            # Call the service to update the selected user's information
            self.service.update_user(user_id, name, email, password)
            print("Informasi pengguna buku telah diperbarui.")
        else:
            print("ID pengguna buku tidak valid.")

    # Delete an existing user from the book service
    def delete_user(self):
        self.all_users()

        user_id = int(input("Pilih ID pengguna buku yang ingin dihapus: ")) - 1
        if 0 <= user_id < len(self.service.read_all_users()):
            # Call the service to delete the selected user
            self.service.delete_user(user_id)
            print("Pengguna buku telah dihapus.")
        else:
            print("ID pengguna buku tidak valid.")
