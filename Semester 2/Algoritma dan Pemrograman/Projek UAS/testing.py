# def simpanPegawai():
#     try:
#         with open('pegawai.txt', 'r') as file:
#             return [baris.strip() for baris in file.readlines()]
#     except FileNotFoundError:
#         return []  

# def filePegawai():
#     with open('pegawai.txt', 'w') as file:
#         for pegawai in dataPegawai:
#             file.write(pegawai + '\n')
# def bacaPegawai():
#     if not os.path.exists('pegawai.txt'):
#         return []
#     with open('pegawai.txt', 'r') as file:
#         data = []
#         for baris in file:
#             try:
#                 data.append(json.loads(baris.strip()))
#             except json.JSONDecodeError:
#                 print("Baris tidak valid JSON, dilewati:", baris)
#                 continue
#     return data

# def simpanPegawai():
#     file = open('pegawai.txt','w')
#     for pegawai in dataPegawai:
#         file.write(json.dumps(pegawai) + '\n')
import re
import json
import os
import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

def bacaPegawai():
    if not os.path.exists('pegawai.txt'):
        return []
    with open('pegawai.txt', 'r') as file:
        data = []
        for baris in file:
            try:
                data.append(json.loads(baris.strip())) 
            except json.JSONDecodeError:
                print("Baris tidak valid JSON, dilewati:", baris)
                continue
    return data

dataPegawai = bacaPegawai()

def simpanPegawai():
    with open('pegawai.txt', 'w') as file:
        for pegawai in dataPegawai:
            file.write(json.dumps(pegawai) + '\n') 


def tambahID():
    return f'P{len(dataPegawai)+1:03}'

def konfirmasiKeluar():
            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['tidak', 't']:
                print(Back.RED + "Anda keluar dari program!")
                return False
            elif konfirmasiKeluar.lower() in ['ya', 'y']:
                print(Back.GREEN + 'Program dijalankan!')
                return True
            else:
                print(Back.RED + 'Input tidak valid!')
                print(Back.RED + 'Otomatis keluar dari program!')
                return False

def inputKosong(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + 'Input tidak boleh kosong! Silakan ulangi.')
            continue
        return userInput


def inputKosong_bknAngka(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif any(char.isdigit() for char in userInput):
            print(Back.RED + "Input tidak boleh mengandung angka! Silakan ulangi.")
        return userInput

def inputKosong_Angka(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong. Silakan ulangi.")
        elif not userInput.isdigit():
            print(Back.RED + "Input hanya mengandung angka! Silakan ulangi.")
        return userInput

def inputJenisKelamin(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput not in ['l', 'p', 'lelaki', 'perempuan']:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
        return userInput
        
def inputAlamat(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif any(char.isdigit() for char in userInput):
            print(Back.RED + "Input tidak boleh mengandung angka! Silakan ulangi.")
        return userInput

def inputNoHp(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif not userInput.isdigit():
            print(Back.RED + "Input hanya mengandung angka! Silakan ulangi.")
        elif len(userInput) > 13 or len(userInput) < 12:
            print(Back.RED + "Input tidak boleh lebih dan kurang dari 13 digit! Silakan ulangi.")
        elif not userInput.startswith("08"):
            print(Back.RED + "Input harus diawali dengan '08'! Silakan ulangi.")
        return userInput

def inputEmail(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        if " " in userInput:
            print(Back.RED + "Input tidak boleh mengandung spasi! Silakan ulangi.")
            continue
        if userInput.count('@') != 1:
            print(Back.RED + "Input hanya mengandung satu simbol '@'! Silakan ulangi.")
            continue

        nama, domain = userInput.split('@')
        if not nama or not domain:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
            continue
        if '.' not in domain:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
            continue
        if domain.startswith(".") or domain.endswith("."):
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
            continue

        return userInput

def inputStatus(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput not in ['tetap', 'kontrak', 'magang']:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
        return userInput
    
def inputPecatPegawai(inputan):
    while True:
        userInput = input(inputan).upper()
        if not userInput: 
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        if not re.fullmatch(r'P\d{3}', userInput):
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
            continue
        return userInput

def inputKonfirmasi(inputan):
    while True:
        userInput = input(inputan).lower()
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput.lower() not in ['ya', 'y', 'tidak', 't']:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
        return userInput.lower()
    
def inputKonfirmasiKeluar(inputan):
    while True:
        userInput = input(inputan).lower()
        if not userInput:
            print(Back.RED + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        elif userInput.lower() not in ['ya', 'y', 'tidak', 't']:
            print(Back.RED + "Input tidak valid! Silakan ulangi.")
            continue
        return userInput.lower()
        


def lihatData(pegawai):
    print(f"ID           : {pegawai['idPegawai']}")
    print(f"Status       : {pegawai['statusPegawai']}")
    print(f"Nama         : {pegawai['namaPegawai']}")
    print(f"Umur         : {pegawai['umurPegawai']}")
    print(f"Kelamin      : {pegawai['kelamin']}")
    print(f"Alamat       : {pegawai['alamat']}")
    print(f"Telepon      : {pegawai['nomorHP']}")
    print(f"Email        : {pegawai['email']}")
    if pegawai['statusPegawai'] == 'Tetap':
        print(f"Gaji         : {pegawai['gajiPegawai']}")
    elif pegawai['statusPegawai'] == 'Kontrak':
        print(f"Waktu Kontrak: {pegawai['waktuKontrak']}")
        print(f"Gaji         : {pegawai['gajiPegawai']}")
    elif pegawai['statusPegawai'] == 'Magang':
        print(f"Waktu Magang : {pegawai['waktuMagang']}")
        print(f"Uang Saku    : {pegawai['uangSaku']}")
    print(f"Waktu Masuk  : {pegawai['waktuMasuk']}")
    print('--------------------------------------')

while True:
    print('===========================')
    print(Back.BLUE + '1. Lihat Data Pegawai                ')
    print(Back.BLUE + '2. Cari Pegawai Berdasarkan ID       ')
    print(Back.BLUE + '3. Tambahkan Pegawai Baru            ')
    print(Back.BLUE + '4. Pecat Pegawai                     ')
    print(Back.BLUE + '5. Promosi Pegawai                   ')
    print(Back.BLUE + '6. Keluar                            ')
    print('===========================')
    pilihan = inputKosong('Pilihan: ').strip()

    match pilihan:
        case '1':
            print('1. Lihat semua data pegawai.')
            print('2. Lihat data berdasarkan status pegawai (Tetap/Kontrak/Magang).')
            pilihanKedua = inputKosong('Pilihan: ').strip()
            match pilihanKedua:
                case '1':
                    if dataPegawai:
                        for pegawai in dataPegawai:
                            lihatData(pegawai)
                    else:
                        print(Back.RED + 'Data pegawai kosong!')

                case '2':
                    pilihStatus = inputStatus('Lihat data pegawai berdasarkan status (Tetap/Kontrak/Magang): ').title()
                    ditemukan = False
                    for pegawai in dataPegawai:
                        if pegawai['statusPegawai'] == pilihStatus:
                            ditemukan = True
                            lihatData(pegawai)
                    if not ditemukan:
                        print(Back.RED + 'Data pegawai tidak ditemukan!')
 
                case _:
                    print(Back.RED + 'Masukkan opsi yang sesuai! (1/2)')

            if not konfirmasiKeluar():
                break

        case '2':
            cariIdPegawai = inputKosong('Masukkan ID pegawai: ').upper()
            ditemukan = False

            for pegawai in dataPegawai:
                if pegawai['idPegawai'].upper() == cariIdPegawai:
                    print(Back.GREEN + 'Pegawai ditemukan!')
                    lihatData(pegawai)
                    ditemukan = True

            if ditemukan == False:
                print(Back.RED + 'ID pegawai tidak ditemukan!')

            if not konfirmasiKeluar():
                break

        case '3':
            # Nama
            namaPegawaiBaru = inputKosong_bknAngka('Nama pegawai baru: ').title().strip()
            # NAMA END

            # UMUR
            umur = inputKosong_Angka('Umur (Angka): ')
            umur = str(umur) + ' Tahun'
            #UMUR END
    
            #JENIS KELAMIN
            jenisKelamin = inputJenisKelamin('Jenis Kelamin (L/P): ').lower()
            if jenisKelamin in ['l', 'lelaki']:
                jenisKelamin = 'Laki-laki'
            elif jenisKelamin in ['p', 'perempuan']:
                jenisKelamin = 'Perempuan'
            #JENIS KELAMIN END

            #ALAMAT
            print('Masukkan alamat pegawai baru!')
            negara = inputKosong_bknAngka('Negara: ').title().strip()
            provinsi = inputKosong_bknAngka('Provinsi: ').title().strip()
            kota = inputKosong_bknAngka('Kota: ').title().strip()
            alamat = negara + ', ' + provinsi + ', ' + kota
            #ALAMAT END
        
            #NO HP
            noHP = inputNoHp('Nomor Telepon (diawali dengan 08): ')
            #NO HP END

            #EMAIL
            email = inputEmail('Email (contoh: username@gmail.com): ')
            # EMAIL END

            # STATUS PEGAWAI
            statusPegawai = inputStatus('Status Pegawai (Tetap/Kontrak/Magang): ').title()
            waktuKontrak = ''
            uangSaku = ''
            waktuMagang = ''
            gajiPegawai = ''

            if statusPegawai.lower() in ['tetap']:
                statusPegawai = 'Tetap'
                gajiPegawai = inputKosong_Angka('Masukkan Gaji (Rp): ').replace('.','')

            elif statusPegawai.lower() in ['kontrak']:
                statusPegawai = 'Kontrak'
                waktuKontrak = inputKosong_Angka('Waktu Kontrak (bulan): ')
                waktuKontrak = waktuKontrak + ' Bulan'
                gajiPegawai = inputKosong_Angka('Masukkan Gaji (Rp): ').replace('.','')


            elif statusPegawai.lower() in ['magang']:
                statusPegawai = 'Magang'
                waktuMagang = inputKosong_Angka('Waktu Magang (bulan): ')
                waktuMagang = waktuMagang + ' Bulan'
                uangSaku = inputKosong_Angka('Masukkan Uang Saku (Rp): ').replace('.','')
            # STATUS PEGAWAI END

            # WAKTU MASUK
            waktuMasuk = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # WAKTU MASUK END

            # ID PEGAWAI
            idPegawai = tambahID()
            # ID PEGAWAI END

            # MENYIMPAN DATA PEGAWAI BARU
            pegawai = {
                'namaPegawai': namaPegawaiBaru,
                'idPegawai': idPegawai,
                'statusPegawai': statusPegawai,
                'umurPegawai': umur,
                'kelamin': jenisKelamin,
                'alamat': alamat,
                'nomorHP': noHP,
                'email': email,
                'waktuMasuk': waktuMasuk,
                'gajiPegawai': gajiPegawai,
                'waktuKontrak': waktuKontrak,
                'uangSaku': uangSaku,
                'waktuMagang': waktuMagang,
            }
            dataPegawai.append(pegawai)
            simpanPegawai()
            print(Back.GREEN + f'{namaPegawaiBaru} berhasil ditambahkan, dengan ID {idPegawai}')
            # MENYIMPAN DATA PEGAWAI BARU END
            
            if not konfirmasiKeluar():
                break

        case '4':
            pecatPegawai = inputPecatPegawai('ID pegawai yang akan dipecat (PXXX): ').upper()
            ditemukan = False
            for id in dataPegawai:
                if id['idPegawai'] == pecatPegawai:
                    ditemukan = True
                    print(Back.GREEN + 'Pegawai ditemukan!')
                    lihatData(id)

                    konfirmasiPecat = inputKonfirmasi('Konfirmasi pemecatan (Ya/Tidak): ')
                    if konfirmasiPecat.lower() in ['ya', 'y']:
                        print(Back.RED + 'Pegawai telah dipecat!')
                        dataPegawai.remove(id)
                        simpanPegawai()
                    elif konfirmasiPecat.lower() in ['tidak', 't']:
                        print(Back.RED + 'Pemecatan dibatalkan!')

            if not ditemukan:
                print(Back.RED + 'Pegawai tidak ditemukan!')
                
            if not konfirmasiKeluar():
                break

        case '5':
            idPegawaiPromosi = inputPecatPegawai('Masukkan ID Pegawai yang akan dipromosikan (PXXX): ').upper()
            ditemukan = False
            for id in dataPegawai:
                if id['idPegawai'] == idPegawaiPromosi:
                    ditemukan = True
                    print(Back.GREEN + 'Pegawai ditemukan!')
                    lihatData(id)
                    konfirmasiPromosi = inputKonfirmasi('Konfirmasi promosi (Ya/Tidak): ')
                    if konfirmasiPromosi.lower() in ['ya', 'y']:
                        if id['statusPegawai'] == 'Tetap':
                            print(Back.RED + 'Status pegawai sekarang adalah pegawai tetap!')
                            print(Back.RED + 'Pegawai tidak dapat dipromosikan!            ')
                        elif id['statusPegawai'] == 'Magang':
                            id['statusPegawai'] = 'Kontrak'
                            print(Back.GREEN + 'Pegawai telah dipromosikan!')
                            simpanPegawai()

                            konfirmasiNaikGaji = inputKonfirmasi('Naikkan gaji (Ya/Tidak): ')
                            if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                naikGaji = inputKosong_Angka('Nominal Gaji (bukan ditambah): ').replace('.','')
                                id['gajiPegawai'] = naikGaji
                                simpanPegawai()
                            elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                print(Back.RED + 'Gaji tidak dinaikkan!')

                        elif id['statusPegawai'] == 'Kontrak':
                            id['statusPegawai'] = 'Tetap'
                            print(Back.GREEN + 'Pegawai telah dipromosikan!')
                            simpanPegawai()
                            konfirmasiNaikGaji = inputKonfirmasi('Naikkan gaji (Ya/Tidak): ')
                            if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                naikGaji = input('Nominal Gaji (bukan ditambah): ').replace('.','')
                                id['gajiPegawai'] = naikGaji
                                simpanPegawai()
                            elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                print(Back.RED + 'Gaji tidak dinaikkan!')

                        elif konfirmasiPromosi.lower() in ['tidak', 't']:
                            print(Back.RED + 'Opsi naik jabatan dibatalkan!')
            if not ditemukan:
                print(Back.RED + 'Pegawai tidak ditemukan!')
                                                                     
            if not konfirmasiKeluar():
                break

        case '6':
            konfirmasiKeluarProgram = inputKonfirmasiKeluar('Anda akan keluar program!, konfirmasi (Ya/Tidak): ')
            if konfirmasiKeluarProgram.lower() in ['ya', 'y']:
                print(Back.MAGENTA + 'Terima kasih telah menggunakan program ini!')
                break
            elif konfirmasiKeluarProgram.lower() in ['tidak', 't']:
                print(Back.GREEN + 'Anda kembali ke menu utama!')
                
        case _:
            print(Back.RED + 'Pilihan tidak tersedia!     ')
            print(Back.RED + 'Masukkan opsi yang tersedia!')