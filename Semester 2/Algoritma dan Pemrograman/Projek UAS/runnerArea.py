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
            konfirmasiKeluar = input(Style.BRIGHT + 'Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['tidak', 't']:
                print(Back.RED + Style.BRIGHT + "Anda keluar dari program!")
                return False
            elif konfirmasiKeluar.lower() in ['ya', 'y']:
                print(Back.GREEN + Style.BRIGHT + 'Program dijalankan!')
                return True
            else:
                print(Back.RED + Style.BRIGHT + 'Input tidak valid!')
                print(Back.RED + Style.BRIGHT + 'Otomatis keluar dari program!')
                return False

def inputKosong(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + 'Input tidak boleh kosong! Silakan ulangi.')
            continue
        return userInput


def inputKosong_bknAngka(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif any(char.isdigit() for char in userInput):
            print(Back.RED + Style.BRIGHT + "Input tidak boleh mengandung angka! Silakan ulangi.")
        return userInput

def inputKosong_Angka(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan ulangi.")
        elif not userInput.isdigit():
            print(Back.RED + Style.BRIGHT + "Input hanya mengandung angka! Silakan ulangi.")
        return userInput

def inputJenisKelamin(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput not in ['l', 'p', 'lelaki', 'perempuan']:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
        return userInput
        
def inputAlamat(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif any(char.isdigit() for char in userInput):
            print(Back.RED + Style.BRIGHT + "Input tidak boleh mengandung angka! Silakan ulangi.")
        return userInput

def inputNoHp(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif not userInput.isdigit():
            print(Back.RED + Style.BRIGHT + "Input hanya mengandung angka! Silakan ulangi.")
        elif len(userInput) > 13 or len(userInput) < 12:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh lebih dan kurang dari 13 digit! Silakan ulangi.")
        elif not userInput.startswith("08"):
            print(Back.RED + Style.BRIGHT + "Input harus diawali dengan '08'! Silakan ulangi.")
        return userInput

def inputEmail(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        if " " in userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh mengandung spasi! Silakan ulangi.")
            continue
        if userInput.count('@') != 1:
            print(Back.RED + Style.BRIGHT + "Input hanya mengandung satu simbol '@'! Silakan ulangi.")
            continue

        nama, domain = userInput.split('@')
        if not nama or not domain:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
            continue
        if '.' not in domain:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
            continue
        if domain.startswith(".") or domain.endswith("."):
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
            continue

        return userInput

def inputStatus(inputan):
    while True:
        userInput = input(inputan)
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput not in ['tetap', 'kontrak', 'magang']:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
            continue
        return userInput
    
def inputPecatPegawai(inputan):
    while True:
        userInput = input(inputan).upper()
        if not userInput: 
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        if not re.fullmatch(r'P\d{3}', userInput):
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi (PXXX).")
            continue
        return userInput

def inputKonfirmasi(inputan):
    while True:
        userInput = input(inputan).lower()
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
        elif userInput.lower() not in ['ya', 'y', 'tidak', 't']:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
        return userInput.lower()
    
def inputKonfirmasiKeluar(inputan):
    while True:
        userInput = input(inputan).lower()
        if not userInput:
            print(Back.RED + Style.BRIGHT + "Input tidak boleh kosong! Silakan ulangi.")
            continue
        elif userInput.lower() not in ['ya', 'y', 'tidak', 't']:
            print(Back.RED + Style.BRIGHT + "Input tidak valid! Silakan ulangi.")
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
    print(Style.BRIGHT + '=====================================')
    print(Back.BLUE + Style.BRIGHT + '1. Lihat Data Pegawai                ')
    print(Back.BLUE + Style.BRIGHT + '2. Cari Pegawai Berdasarkan ID       ')
    print(Back.BLUE + Style.BRIGHT + '3. Tambahkan Pegawai Baru            ')
    print(Back.BLUE + Style.BRIGHT + '4. Pecat Pegawai                     ')
    print(Back.BLUE + Style.BRIGHT + '5. Promosi Pegawai                   ')
    print(Back.BLUE + Style.BRIGHT + '6. Keluar                            ')
    print(Style.BRIGHT + '=====================================')
    pilihan = inputKosong(Style.BRIGHT + 'Pilihan: ').strip()

    match pilihan:
        case '1':
            print(Style.BRIGHT + '1. Lihat semua data pegawai.')
            print(Style.BRIGHT + '2. Lihat data berdasarkan status pegawai (Tetap/Kontrak/Magang).')
            pilihanKedua = inputKosong('Pilihan: ').strip()
            match pilihanKedua:
                case '1':
                    if dataPegawai:
                        for pegawai in dataPegawai:
                            lihatData(pegawai)
                    else:
                        print(Back.RED + Style.BRIGHT + 'Data pegawai kosong!')

                case '2':
                    pilihStatus = inputStatus(Style.BRIGHT + 'Lihat data pegawai berdasarkan status (Tetap/Kontrak/Magang): ').title()
                    ditemukan = False
                    for pegawai in dataPegawai:
                        if pegawai['statusPegawai'] == pilihStatus:
                            ditemukan = True
                            lihatData(pegawai)
                    if not ditemukan:
                        print(Back.RED + Style.BRIGHT + 'Data pegawai tidak ditemukan!')
 
                case _:
                    print(Back.RED + Style.BRIGHT + 'Masukkan opsi yang sesuai! (1/2)')

            if not konfirmasiKeluar():
                break

        case '2':
            cariIdPegawai = inputPecatPegawai(Style.BRIGHT + 'Masukkan ID pegawai: ').upper()
            ditemukan = False

            for pegawai in dataPegawai:
                if pegawai['idPegawai'].upper() == cariIdPegawai:
                    print(Back.GREEN + Style.BRIGHT + 'Pegawai ditemukan!')
                    lihatData(pegawai)
                    ditemukan = True

            if ditemukan == False:
                print(Back.RED + Style.BRIGHT + 'ID pegawai tidak ditemukan!')

            if not konfirmasiKeluar():
                break

        case '3':
            # Nama
            namaPegawaiBaru = inputKosong_bknAngka(Style.BRIGHT + 'Nama pegawai baru: ').title().strip()
            # NAMA END

            # UMUR
            umur = inputKosong_Angka(Style.BRIGHT + 'Umur (Angka): ')
            umur = str(umur) + ' Tahun'
            #UMUR END
    
            #JENIS KELAMIN
            jenisKelamin = inputJenisKelamin(Style.BRIGHT + 'Jenis Kelamin (L/P): ').lower()
            if jenisKelamin in ['l', 'lelaki']:
                jenisKelamin = 'Laki-laki'
            elif jenisKelamin in ['p', 'perempuan']:
                jenisKelamin = 'Perempuan'
            #JENIS KELAMIN END

            #ALAMAT
            print(Style.BRIGHT + 'Masukkan alamat pegawai baru!')
            negara = inputKosong_bknAngka(Style.BRIGHT + 'Negara: ').title().strip()
            provinsi = inputKosong_bknAngka(Style.BRIGHT + 'Provinsi: ').title().strip()
            kota = inputKosong_bknAngka(Style.BRIGHT + 'Kota: ').title().strip()
            alamat = negara + ', ' + provinsi + ', ' + kota
            #ALAMAT END
        
            #NO HP
            noHP = inputNoHp(Style.BRIGHT + 'Nomor Telepon (diawali dengan 08): ')
            #NO HP END

            #EMAIL
            email = inputEmail(Style.BRIGHT + 'Email (contoh: username@gmail.com): ')
            # EMAIL END

            # STATUS PEGAWAI
            statusPegawai = inputStatus(Style.BRIGHT + 'Status Pegawai (Tetap/Kontrak/Magang): ').title()
            waktuKontrak = ''
            uangSaku = ''
            waktuMagang = ''
            gajiPegawai = ''

            if statusPegawai.lower() in ['tetap']:
                statusPegawai = 'Tetap'
                gajiPegawai = inputKosong_Angka(Style.BRIGHT + 'Masukkan Gaji (Rp): ').replace('.','')

            elif statusPegawai.lower() in ['kontrak']:
                statusPegawai = 'Kontrak'
                waktuKontrak = inputKosong_Angka(Style.BRIGHT + 'Waktu Kontrak (bulan): ')
                waktuKontrak = waktuKontrak + ' Bulan'
                gajiPegawai = inputKosong_Angka(Style.BRIGHT + 'Masukkan Gaji (Rp): ').replace('.','')


            elif statusPegawai.lower() in ['magang']:
                statusPegawai = 'Magang'
                waktuMagang = inputKosong_Angka(Style.BRIGHT + 'Waktu Magang (bulan): ')
                waktuMagang = waktuMagang + ' Bulan'
                uangSaku = inputKosong_Angka(Style.BRIGHT + 'Masukkan Uang Saku (Rp): ').replace('.','')
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
            print(Back.GREEN + Style.BRIGHT + f'{namaPegawaiBaru} berhasil ditambahkan, dengan ID {idPegawai}')
            # MENYIMPAN DATA PEGAWAI BARU END
            
            if not konfirmasiKeluar():
                break

        case '4':
            pecatPegawai = inputPecatPegawai(Style.BRIGHT + 'ID pegawai yang akan dipecat (PXXX): ').upper()
            ditemukan = False
            for id in dataPegawai:
                if id['idPegawai'] == pecatPegawai:
                    ditemukan = True
                    print(Back.GREEN + Style.BRIGHT + 'Pegawai ditemukan!')
                    lihatData(id)

                    konfirmasiPecat = inputKonfirmasi(Style.BRIGHT + 'Konfirmasi pemecatan (Ya/Tidak): ')
                    if konfirmasiPecat.lower() in ['ya', 'y']:
                        print(Back.RED + Style.BRIGHT + 'Pegawai telah dipecat!')
                        dataPegawai.remove(id)
                        simpanPegawai()
                    elif konfirmasiPecat.lower() in ['tidak', 't']:
                        print(Back.RED + Style.BRIGHT + 'Pemecatan dibatalkan!')

            if not ditemukan:
                print(Back.RED + Style.BRIGHT + 'Pegawai tidak ditemukan!')
                
            if not konfirmasiKeluar():
                break

        case '5':
            idPegawaiPromosi = inputPecatPegawai(Style.BRIGHT + 'Masukkan ID Pegawai yang akan dipromosikan (PXXX): ').upper()
            ditemukan = False
            for id in dataPegawai:
                if id['idPegawai'] == idPegawaiPromosi:
                    ditemukan = True
                    print(Back.GREEN + Style.BRIGHT + 'Pegawai ditemukan!')
                    lihatData(id)
                    konfirmasiPromosi = inputKonfirmasi(Style.BRIGHT + 'Konfirmasi promosi (Ya/Tidak): ')
                    if konfirmasiPromosi.lower() in ['ya', 'y']:
                        if id['statusPegawai'] == 'Tetap':
                            print(Back.RED + Style.BRIGHT + 'Status pegawai sekarang adalah pegawai tetap!')
                            print(Back.RED + Style.BRIGHT + 'Pegawai tidak dapat dipromosikan!            ')
                        elif id['statusPegawai'] == 'Magang':
                            id['statusPegawai'] = 'Kontrak'
                            print(Back.GREEN + Style.BRIGHT + 'Pegawai telah dipromosikan!')
                            simpanPegawai()

                            konfirmasiNaikGaji = inputKonfirmasi(Style.BRIGHT + 'Naikkan gaji (Ya/Tidak): ')
                            if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                naikGaji = inputKosong_Angka(Style.BRIGHT + 'Nominal Gaji (bukan ditambah): ').replace('.','')
                                id['gajiPegawai'] = naikGaji
                                simpanPegawai()
                            elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                print(Back.RED + Style.BRIGHT + 'Gaji tidak dinaikkan!')

                        elif id['statusPegawai'] == 'Kontrak':
                            id['statusPegawai'] = 'Tetap'
                            print(Back.GREEN + Style.BRIGHT + 'Pegawai telah dipromosikan!')
                            simpanPegawai()
                            konfirmasiNaikGaji = inputKonfirmasi(Style.BRIGHT + 'Naikkan gaji (Ya/Tidak): ')
                            if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                naikGaji = input(Style.BRIGHT + 'Nominal Gaji (bukan ditambah): ').replace('.','')
                                id['gajiPegawai'] = naikGaji
                                simpanPegawai()
                            elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                print(Back.RED + Style.BRIGHT + 'Gaji tidak dinaikkan!')

                        elif konfirmasiPromosi.lower() in ['tidak', 't']:
                            print(Back.RED + Style.BRIGHT + 'Opsi naik jabatan dibatalkan!')
            if not ditemukan:
                print(Back.RED + Style.BRIGHT + 'Pegawai tidak ditemukan!')
                                                                     
            if not konfirmasiKeluar():
                break

        case '6':
            konfirmasiKeluarProgram = inputKonfirmasiKeluar('Anda akan keluar program!, konfirmasi (Ya/Tidak): ')
            if konfirmasiKeluarProgram.lower() in ['ya', 'y']:
                print(Back.MAGENTA + Style.BRIGHT + 'Terima kasih telah menggunakan program ini!')
                break
            elif konfirmasiKeluarProgram.lower() in ['tidak', 't']:
                print(Back.GREEN + 'Anda kembali ke menu utama!')
                
        case _:
            print(Back.RED + Style.BRIGHT + 'Pilihan tidak tersedia!     ')
            print(Back.RED + Style.BRIGHT + 'Masukkan opsi yang tersedia!')