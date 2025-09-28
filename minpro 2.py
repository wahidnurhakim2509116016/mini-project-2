from prettytable import PrettyTable
import pwinput 

akun ={
    "admin": {"password": "admin1", "role": "admin"},
    "user": {"password": "user1", "role": "user"}
}

order = {}

lingkungan = ["rumah", "sekolah", "kantor"]
layanan = ["menyapu halaman","membersihkan toilet","membuang sampah"]
status = ["sedang dalam antrian", "pesanan dibatalkan", "pesanan diterima"]

def c_order():
    try:
        print("\n++ silahkan pilih lingkungan ++")
        for i, l in enumerate(lingkungan, start=1):
            print(f"{i}. {l}")
        p_ling = int(input("pilih kategori lingkungan: ")) - 1

        if p_ling not in range(len(lingkungan)):
            print("pilihan tyydacckk valiiidd")
            return
        
        print(f"\n =+= layanan {lingkungan[p_ling]} =+=")
        for i, l in enumerate(layanan, start=1):
            print(f"{i}. {l}")
        p_lay = int(input("pilih layanan yang diinginkan: ")) -1

        if p_lay not in range(len(layanan)):
            print("pilihan tyydacckk valiiidd")

        # biodata
        nama = input("Masukkan nama      : ")
        alamat = input("Masukkan alamat    : ")
        no_telp = input("Masukkan No.Telp   : ")

        #simpan
        id_o = len(order) + 1
        order[id_o] = {
            "nama": nama,
            "alamat": alamat,
            "no_telp": no_telp,
            "lingkungan": lingkungan[p_ling],
            "layanan": layanan[p_lay],
            "status": status[0]
        }
        print(f"\npesanan berhasil dengan no pesanan {id_o}")
    
    except ValueError:
        print("pake angka dong cintaaahh")
    except KeyboardInterrupt:
        print("pasti tepencet ctrl + c yaaa!!!!")

def r_order():
    if not order:
        print("\n kamu belum ada mesannn")
        return
    print("\n=== DAFTAR PESANAN ===")
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Alamat", "No.Telp", "Lingkungan", "Layanan", "Status"]
    for id_o, data in order.items():
        table.add_row([id_o, data["nama"], data["alamat"], data["no_telp"], data["lingkungan"], data["layanan"], data["status"]])
    print(table)

def u_order():
    try:
        r_order()
        if not order:
            return
        id_o = int(input("\n masukkan no pesanan yang ingin diubah status: "))
        if id_o not in order:
            print(" No pesanan tidak adaa")
            return

        print("\npilih status baru: ")
        for i, s in enumerate(status, start=1):
            print(f"{i}. {s}")
        p_status = int(input("masukkan status (angka): ")) - 1

        if 0 <= p_status < len(status):
            order[id_o]["status"] = status[p_status]
            print(f"\nStatus pesanan {id_o} sekarang: {order[id_o]['status']}")
            print("status nya sudah berhasil diperbaruiii")
        else:
            print("pilihan kamu tydaack validd")
    except ValueError:
        print("pake angka dong cintaaahh")
    except KeyboardInterrupt:
        print("\nInput dibatalkan (Ctrl+C)")

def d_order():
    try:
        r_order()
        if not order:
            return
        id_o = int(input("\n masukkan no pesanan yang ingin dihapus"))
        if id_o in order:
            de = order.pop(id_o)
            print(f"pesanan {de['nama']} berhasil dihapus")
        else:
            print("no pesanan tidak ditemukan")
    except ValueError:
        print("pake angka dong cintaaahh")
    except KeyboardInterrupt:
        print("pasti tepencet ctrl + c yaaa!!!!") 

#Menu 
#admin
def menu_A():
    while True:
        print("\n==-== MENU ADMIN ==-==")
        print("1. Tambah pesanan")
        print("2. Lihat pesanan")
        print("3. Ubah status pesanan")
        print("4. Hapus pesanan")
        print("5. Logout")

        pilihan = input("pilih menu (1-5): ")
        if pilihan == "1":
            c_order()
        elif pilihan == "2":
            r_order()
        elif pilihan == "3":
            u_order()
        elif pilihan == "4":
            d_order()
        elif pilihan == "5":
            print("admin jan galak galak yaa!!!")
            break
        else:
            print("pilihan andaa tydackk valiiid")

#user
def menu_U():
    while True:
        print("\n=== MENU USER ===")
        print("1. Tambah Pesanan")
        print("2. Lihat Pesanan")
        print("3. Logout")

        pilihan = input("Pilih menu (1-3): ")
        if pilihan == "1":
            c_order()
        elif pilihan == "2":
            r_order()
        elif pilihan == "3":
            print("jangan lupa pesan lagi yaaa :)")
            break
        else:
            print("pilihan andaa tydackk valiiid")

def login():
    username = input("Masukkan username : ")
    password = pwinput.pwinput("Masukkan password : ")

    if username in akun and akun[username]["password"] == password:
        print(f"\n anda login sebagai {akun[username]['role'].upper()}")
        if akun[username]["role"] == "admin":
            menu_A()
        else:
            menu_U()
    else:
        print("\nusername atau paswword salah")

while True:
    login()
    ulang = input('\napakah anda yakin ingin keluar? (yes/no): ')
    if ulang != "no":
        print ("\nTERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI")
        break