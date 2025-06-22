#nama = "Faishal" #pager itu komen
#usia = 20
#tinggi_Badan = 192
#menyapa = "Halo Semua"
#str(usia) yang tadinya integer 20 jadi string "20"
#int(nama) yang tadinya string "Faishal" jadi integer Faishal
#tips di atas bisa dipake juga di print untuk + bukan "," koma. Contoh:
#print(nama + str(usia)) --> agar tidak eror saja
#print('2.',"Umur saya", usia,"tahun")
#print('3.',"Tinggi Badanku adalah", tinggi_Badan, "cm","\n")

# pegawai = []
# while True:
#     print('Program Pendataan Pegawai:')
#     print('1. Tambahkan Pegawai Baru')
#     print('2. Cari Pegawai')
#     print('3. Pecat Pegawai')
#     print('4. Data Pegawai')
#     print('5. Keluar')

#     pilihan = input('Masukkan Pilihan Anda: ')
#     if pilihan == '1':
#         pegawai_baru = input('Nama Pegawai Baru: ')
#         pegawai.append(pegawai_baru)
#         print(pegawai_baru, 'telah ditambahkan!')
#         print(' ')
#     elif pilihan == '2':
#         cari = input('Nama Pegawai: ')
#         if cari in pegawai:
#             print(cari, 'terdaftar!')
#             print(' ')
#         else:
#             print(cari, 'tidak terdaftar!')
#             print(' ')
#     elif pilihan == '3':
#         pecat = input('Masukkan Nama Pegawai: ')
#         if pecat in pegawai:
#             pegawai.remove(pecat)
#             print(f'{pecat} telah dipecat!')
#             print(' ')
#         else:
#             print(pecat, 'tidak terdaftar!')
#             print(' ')
#     elif pilihan == '4':
#         if pegawai:
#             for nama, angka in enumerate(pegawai, start=1):
#                 print(nama,angka)
#         else:
#             print("Tidak ada pegawai yang terdaftar!")
#         print(' ')
#     elif pilihan == '5':
#         print('Anda keluar dari program!')
#         break
#     else:
#         print('Masukkan pilihan yang tersedia!')
#         print(' ')


# file = open("namaFile.txt",'mode')
# mode:
# w = write mode / mode menulis dan menghapus file lama
# r = read mode only / hanya bisa baca
# a = appending mode / menambahkan data di akhir baris
# r+ = read and write mode / bisa baca dan menulis

# file = open("data.txt",'w')
# file.write('ini adalah data text yang dibuat dengan python')
# file.write("\nini baris kedua")
# file.write("\nini baris ketiga")
# file.write("\nini baris keempat")
# file.close()

# file2 = open('data.txt', 'r')
# print(file2.read())
# print(file2.readline())
# file2.close()

# file3 = open('data.txt', 'a') #kalau 'a' mah gabakal ditimpa file.write sebelumnya (menambahkan), sedangkan 'w' akan menggantikan file.write sebelumnya
# file3.write('\nBaris ini dibuat dengan menggunakan mode append')
# file3.close()

# import os
# os.chdir(r'C:\Users\Faisal\OneDrive\Desktop\Tugas-tugas pemrog\Semester 2\Algoritma dan Pemrograman\Projek UAS')
# print(os.path.exists('dataPegawai.py'))

# Data Pegawai
import os
import datetime
from colorama import init, Back
init(autoreset=True)

def bacaPegawai():
    if not os.path.exists('pegawai.txt'):
        return []
    with open('pegawai.txt', 'r') as file:
        data = []
        for baris in file:
            data.append(eval(baris.strip()))  # ubah dari string ke dict
    return data

def simpanPegawai():
    with open('pegawai.txt', 'w') as file:
        for pegawai in dataPegawai:
            file.write(str(pegawai) + '\n')

def generateID():
    return f"PGW{len(dataPegawai)+1:04}"

def tampilkanData(pegawai):
    print(f"ID          : {pegawai['id']}")
    print(f"Nama        : {pegawai['nama']}")
    print(f"Umur        : {pegawai['umur']}")
    print(f"Kelamin     : {pegawai['gender']}")
    print(f"Alamat      : {pegawai['alamat']}")
    print(f"Telepon     : {pegawai['telepon']}")
    print(f"Email       : {pegawai['email']}")
    print(f"Status      : {pegawai['status']}")
    print(f"Detail Gaji : {pegawai['gaji']}")
    print(f"Waktu Masuk : {pegawai['waktu_masuk']}")
    if 'durasi' in pegawai:
        print(f"Durasi      : {pegawai['durasi']}")
    print('-'*30)

dataPegawai = bacaPegawai()

while True:
    print('===============================')
    print(Back.BLUE + '1. Lihat Data Pegawai          ')
    print(Back.BLUE + '2. Cari Pegawai                ')
    print(Back.BLUE + '3. Tambah Pegawai Baru         ')
    print(Back.BLUE + '4. Pecat Pegawai               ')
    print(Back.BLUE + '5. Update Pegawai              ')
    print(Back.BLUE + '6. Keluar                      ')
    print('===============================')

    pilihan = input('Pilihan: ')

    if pilihan == '1':
        if dataPegawai:
            for pegawai in dataPegawai:
                tampilkanData(pegawai)
        else:
            print('Data pegawai kosong.')

    elif pilihan == '2':
        print('1. Berdasarkan ID')
        print('2. Berdasarkan Status')
        print('3. Berdasarkan Nama')
        sub = input('Pilih sub pencarian: ')
        if sub == '1':
            idcari = input('Masukkan ID: ').strip()
            ditemukan = False
            for p in dataPegawai:
                if p['id'] == idcari:
                    tampilkanData(p)
                    ditemukan = True
            if not ditemukan:
                print('Pegawai tidak ditemukan.')
        elif sub == '2':
            status = input('Masukkan status (Tetap/Kontrak/Magang): ').title()
            for p in dataPegawai:
                if p['status'] == status:
                    tampilkanData(p)
        elif sub == '3':
            nama = input('Masukkan nama: ').title().strip()
            for p in dataPegawai:
                if p['nama'] == nama:
                    tampilkanData(p)

    elif pilihan == '3':
        nama = input('Nama: ').title().strip()
        umur = input('Umur: ')
        gender = input('Jenis kelamin (L/P): ').upper()
        alamat = input('Alamat: ')
        telepon = input('Nomor telepon: ')
        email = input('Email: ')
        status = input('Status (Tetap/Kontrak/Magang): ').title()
        gaji = ''
        durasi = ''
        if status == 'Tetap':
            gaji = input('Gaji bulanan (perkiraan): ')
        elif status == 'Kontrak':
            gaji = input('Gaji bulanan: ')
            durasi = input('Durasi kontrak (max 1 tahun): ')
        elif status == 'Magang':
            gaji = input('Uang saku per bulan: ')
            durasi = input('Durasi magang (max 6 bulan): ')
        else:
            print('Status tidak valid.')
            continue
        waktu_masuk = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        idpegawai = generateID()
        pegawai = {
            'id': idpegawai,
            'nama': nama,
            'umur': umur,
            'gender': gender,
            'alamat': alamat,
            'telepon': telepon,
            'email': email,
            'status': status,
            'gaji': gaji,
            'waktu_masuk': waktu_masuk
        }
        if durasi:
            pegawai['durasi'] = durasi

        dataPegawai.append(pegawai)
        simpanPegawai()
        print(f"Pegawai {nama} berhasil ditambahkan!")

    elif pilihan == '4':
        idhapus = input('Masukkan ID pegawai yang akan dihapus: ')
        ditemukan = False
        for pegawai in dataPegawai:
            if pegawai['id'] == idhapus:
                dataPegawai.remove(pegawai)
                simpanPegawai()
                print(f'Pegawai {idhapus} berhasil dihapus!')
                ditemukan = True
                break
        if not ditemukan:
            print('ID tidak ditemukan.')

    elif pilihan == '5':
        idupdate = input('Masukkan ID pegawai yang ingin diupdate: ')
        for pegawai in dataPegawai:
            if pegawai['id'] == idupdate:
                print("Masukkan status baru pegawai (Tetap/Kontrak/Magang)")
                status = input('Status baru: ').title()
                pegawai['status'] = status
                pegawai['gaji'] = input('Gaji/Uang saku baru: ')
                if status in ['Kontrak', 'Magang']:
                    pegawai['durasi'] = input('Durasi baru: ')
                else:
                    pegawai.pop('durasi', None)
                simpanPegawai()
                print('Data pegawai berhasil diupdate!')
                break
        else:
            print('ID tidak ditemukan.')

    elif pilihan == '6':
        konfirmasi = input('Yakin ingin keluar? (Y/T): ').lower()
        if konfirmasi in ['y', 'ya']:
            print("Keluar dari program.")
            break
    else:
        print('Pilihan tidak valid!')

    lanjut = input("Lanjutkan program? (Y/T): ").lower()
    if lanjut not in ['y', 'ya']:
        print("Program dihentikan.")
        break
