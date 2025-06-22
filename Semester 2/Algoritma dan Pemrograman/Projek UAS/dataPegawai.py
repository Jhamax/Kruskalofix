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

    pilihan = input('Pilihan: ').strip()

    match pilihan:
        case '1':
            print('1. Lihat semua data pegawai.')
            print('2. Lihat data berdasarkan status pegawai (Tetap/Kontrak/Magang).')
            pilihanKedua = input('Pilihan: ')
            match pilihanKedua:
                case '1':
                    if dataPegawai:
                        for pegawai in dataPegawai:
                            lihatData(pegawai)
                    else:
                        print('Data pegawai kosong!')

                case '2':
                    pilihStatus = input('Lihat data pegawai berdasarkan status (Tetap/Kontrak/Magang): ').title()
                    if pilihStatus not in ['Tetap', 'Kontrak', 'Magang']:
                        print('Masukkan opsi yang sesuai! (Tetap/Kontrak/Magang)')
                    elif pilihStatus in ['Tetap', 'Kontrak', 'Magang']:
                        for pegawai in dataPegawai:
                            if pegawai['statusPegawai'] == pilihStatus:
                                lihatData(pegawai)
                            else:
                                print('Data pegawai tidak ditemukan!')
                                break
                    else:
                        print('Error!')
                        break
                case _:
                    print('Masukkan opsi yang sesuai! (1/2)')

            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['tidak', 't']:
                print("Anda keluar dari program!")
                break
            elif konfirmasiKeluar.lower() in ['ya', 'y']:
                print('Program dijalankan!')
            else:
                print('Input tidak valid!')
                break

        case '2':
            cariIdPegawai = input('Masukkan ID pegawai: ').upper()
            if not cariIdPegawai:
                print('ID pegawai tidak boleh kosong!')
            elif cariIdPegawai:
                ditemukan = False

                for pegawai in dataPegawai:
                    if pegawai['idPegawai'].upper() == cariIdPegawai:
                        print('Pegawai ditemukan!')
                        lihatData(pegawai)
                        ditemukan = True

                if ditemukan == False:
                    print('ID pegawai tidak ditemukan!')

            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['ya', 'y']:
                print("Program dijalankan!")
                continue
            elif konfirmasiKeluar.lower() in ['tidak', 't']:
                print('Anda keluar dari program!')
                break
            else:
                print('Pilihan tidak ada!')
                break

        case '3':
            namaPegawaiBaru = input('Nama pegawai baru: ').title().strip()
            if not namaPegawaiBaru:
                print('Nama pegawai tidak boleh kosong!')
                if not namaPegawaiBaru:
                    print('Nama tidak boleh kosong!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break

            umur = input('Umur (Angka): ').strip()
            if not umur:
                print('Umur tidak boleh kosong')
                umut = input('Umur (Angka): ').strip()
                if not umur:
                    print('Umur tidak boleh kosong!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ').strip()
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            elif not umur.isdigit():
                print('Umur harus berupa angka!')
                umur = input('Umur (Angka): ').strip()
                if not umur.isdigit():
                    print('Umur harus berupa angka!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            elif umur.isdigit():
                umur = umur + ' Tahun'
                
            jenisKelamin = input('Jenis Kelamin (L/P): ').lower()
            if jenisKelamin not in ['l', 'p', 'lelaki', 'perempuan']:
                print('Pilihan tidak sesuai!')
                jenisKelamin = input('Jenis Kelamin (L/P): ').lower()
                if jenisKelamin not in ['l', 'p', 'lelaki', 'perempuan'] or not jenisKelamin:
                    print('Pilihan tidak sesuai! atau jenis kelamin tidak boleh kosong!')
                    print('Otomatis keluar dari program!')
                    break
                elif jenisKelamin in ['l', 'lelaki']:
                    jenisKelamin = 'Laki-Laki'
                elif jenisKelamin in ['p', 'perempuan']:
                    jenisKelamin = 'Perempuan'
            elif not jenisKelamin:
                print('Jenis Kelamin tidak boleh kosong!')
                jenisKelamin = input('Jenis Kelamin (L/P): ').lower()
                if not jenisKelamin or jenisKelamin not in ['l', 'p', 'lelaki', 'perempuan']:
                    print('Jenis Kelamin tidak boleh kosong! atau pilihan tidak sesuai!')
                    print('Otomatis keluar dari program!')
                    break
                elif jenisKelamin in ['l', 'lelaki']:
                    jenisKelamin = 'Laki-Laki'
                elif jenisKelamin in ['p', 'perempuan']:
                    jenisKelamin = 'Perempuan'
            else:
                if jenisKelamin in ['l', 'lelaki']:
                    jenisKelamin = 'Laki-Laki'
                elif jenisKelamin in ['p', 'perempuan']:
                    jenisKelamin = 'Perempuan'

            alamat = input('Alamat (Negara, Kota): ').title()
            if not alamat:
                print('Alamat tidak boleh kosong!')
                alamat = input('Alamat (Negara, Kota): ').title()
                if not alamat:
                    print('Alamat tidak boleh kosong!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            elif any(char.isdigit() for char in alamat):
                print('Alamat tidak boleh mengandung angka!')
                alamat = input('Silahkan masukkan negara dan kota (Negara, Kota): ').title()
                if alamat.isdigit():
                    print('Alamat tidak boleh angka!')
                    print('Otomatis keluar program!')
                    break
            elif ',' not in alamat:
                print('Format alamat salah! Gunakan format: Negara, Kota')
                alamat = input('Silahkan masukkan negara dan kota (Negara, Kota): ').title()
                if ',' not in alamat:
                    print('Alamat tidak sesuai format!')
                    print('Otomatis keluar program!')
                    break

            noHP = input('Nomor Telepon: ')
            if not noHP:
                print('Nomor telepon tidak boleh kosong!')
                noHp = input('Nomor Telepon: ')
                if not noHP:
                    print('Nomor telepon tidak boleh kosong!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            elif not noHP.isdigit():
                print('Nomor telepon harus berupa angka!')
                noHp = input('Nomor Telepon: ')
                if not noHP.isdigit():
                    print('Nomor telepon harus berupa angka!')
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break

            email = input('Email: ')
            if not email:
                print('Email tidak boleh kosong!')
                email = input('Email: ')    
                if not email:
                    print('Email tidak boleh kosong!')            
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            elif '@' not in email or '.' not in email:
                print('Email tidak valid!')
                email = input('Email: ')
                if '@' not in email or '.' not in email:
                    konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
                    if konfirmasiKeluar.lower() in ['ya','y']:
                        print('Program kembali ke awal!')
                        continue
                    if konfirmasiKeluar.lower() in ['tidak', 't']:
                        print("Anda keluar dari program!")
                        break
                    else:
                        print('Pilihan tidak ada!')
                        print('Otomatis keluar program!')
                        break
            
            statusPegawai = input('Status Pegawai (Tetap/Kontrak/Magang): ').title()
            waktuKontrak = ''
            uangSaku = ''
            waktuMagang = ''
            gajiPegawai = ''

            if statusPegawai.lower() in ['tetap']:
                statusPegawai = 'Tetap'
                gajiPegawai = input('Masukkan Gaji (Rp): ').replace('.','')
                if not gajiPegawai or not gajiPegawai.isdigit():
                    print('Gaji tidak boleh kosong! atau gaji harus berupa angka!')
                    gajiPegawai = input('Masukkan Gaji (Rp): ').replace('.','')
                    if not gajiPegawai or not gajiPegawai.isdigit():
                        print('Gaji tidak boleh kosong! atau gaji harus berupa angka!')
                        print('Otomatis keluar program!!')
                        break
            elif statusPegawai.lower() in ['kontrak']:
                statusPegawai = 'Kontrak'
                gajiPegawai = input('Masukkan Gaji (Rp): ').replace('.','')
                if not gajiPegawai or not gajiPegawai.isdigit():
                    print('Gaji tidak boleh kosong! atau gaji harus berupa angka!')
                    gajiPegawai = input('Masukkan Gaji (Rp): ').replace('.','')
                    if not gajiPegawai or not gajiPegawai.isdigit():
                        print('Gaji tidak boleh kosong! atau gaji harus berupa angka!')
                        print('Otomatis keluar program!!')
                        break
                waktuKontrak = input('Waktu Kontrak (bulan): ')
                if not waktuKontrak or not waktuKontrak.isdigit():
                    print('Waktu Kontrak tidak boleh kosong atau harus berupa angka!')
                    waktuKontrak = input('Waktu Kontrak: ')
                    if not waktuKontrak or not waktuKontrak.isdigit():
                        print('Waktu Kontrak tidak boleh kosong atau harus berupa angka!')
                        print('Otomatis keluar program!!')
                        break
                    if waktuKontrak or waktuKontrak.isdigit():
                        waktuKontrak = waktuKontrak + ' Bulan'
                elif waktuKontrak or waktuKontrak.isdigit():
                    waktuKontrak = waktuKontrak + ' Bulan'

            elif statusPegawai.lower() in ['magang']:
                statusPegawai = 'Magang'
                uangSaku = input('Masukkan Uang Saku (Rp): ').replace('.','')
                if not uangSaku or not uangSaku.isdigit():
                    print('Isian tidak boleh kosong! atau harus berupa angka!')
                    uangSaku = input('Masukkan Gaji (Rp): ').replace('.','')
                    if not uangSaku or not uangSaku.isdigit():
                        print('Isian tidak boleh kosong! atau harus berupa angka!')
                        print('Otomatis keluar program!!')
                        break
                waktuMagang = input('Waktu Magang (bulan): ')
                if not waktuMagang or not waktuMagang.isdigit():
                    print('Waktu Magang tidak boleh kosong! atau harus berupa angka!')
                    waktuMagang = input('Waktu Magang: ')
                    if not waktuMagang:
                        print('Waktu Magang tidak boleh kosong!')
                        print('Otomatis keluar program!!')
                        break
                else:
                    waktuMagang = waktuMagang + ' Bulan'

            waktuMasuk = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            idPegawai = tambahID()

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
            print(f'{namaPegawaiBaru} berhasil ditambahkan, dengan ID {idPegawai}')
            
            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['tidak']:
               print("Anda keluar dari program!")
               break
            elif konfirmasiKeluar.lower() in ['ya', 'y']:  
                print('Program dijalankan!')
            else:
                print('Pilihan tidak ada!')
                print('Otomatis keluar program!')
                break

        case '4':
            pecatPegawai = input('ID pegawai yang akan dipecat: ').upper()
            if not pecatPegawai or not re.fullmatch(r'P\d{3}', pecatPegawai):
                print('ID tidak boleh kosong atau tidak sesuai format!')
                konfirmasiInputId = input('Masukkan ulang id? (Ya/Tidak): ')
                if konfirmasiInputId.lower() in ['ya', 'y']:
                    pecatPegawai = input('ID pegawai yang akan dipecat: ').upper()
                    if not pecatPegawai or not re.fullmatch(r'P\d{3}', pecatPegawai):
                        print('ID tidak boleh kosong atau harus berupa PXXX!')
                        print('Otomatis keluar dari opsi pemecatan!')
                    elif pecatPegawai or re.fullmatch(r'P\d{3}', pecatPegawai):
                        for id in dataPegawai:
                            if id['idPegawai'] == pecatPegawai:
                                print('Pegawai ditemukan!')
                                lihatData(id)
                                konfirmasiPecat = input('Konfirmasi pemecatan (Ya/Tidak): ')
                                if konfirmasiPecat.lower() in ['ya', 'y']:
                                    print('Pegawai telah dipecat!')
                                    dataPegawai.remove(id)
                                    simpanPegawai()
                                elif konfirmasiPecat.lower() in ['tidak', 't']:
                                    print('Pemecatan dibatalkan!')
                            elif id['idPegawai'] != pecatPegawai:
                                konfirmasiInputId = input('ID pegawai tidak ditemukan!, masukkan ulang id? (Ya/Tidak): ')
                                if konfirmasiInputId.lower() in ['ya', 'y']:
                                    pecatPegawai = input('ID pegawai yang akan dipecat: ').upper()
                                    for id in dataPegawai:
                                        if id['idPegawai'] == pecatPegawai:
                                            print('Pegawai ditemukan!')
                                            lihatData(id)
                                            konfirmasiPecat = input('Konfirmasi pemecatan (Ya/Tidak): ')
                                            if konfirmasiPecat.lower() in ['ya', 'y']:
                                                print('Pegawai telah dipecat!')
                                                dataPegawai.remove(id)
                                                simpanPegawai()
                                            elif konfirmasiPecat.lower() in ['tidak', 't']:
                                                print('Pemecatan dibatalkan!')
                                elif konfirmasiInputId.lower() in ['tidak', 't']:
                                    print('Opsi pemecatan batal!')
                elif konfirmasiInputId.lower() in ['tidak', 't']:
                    print('Opsi pemecatan batal!')
                    print('Otomatis keluar dari opsi pemecatan!')
            elif pecatPegawai or re.fullmatch(r'P\d{3}', pecatPegawai):
                for id in dataPegawai:
                    if id['idPegawai'] == pecatPegawai:
                        print('Pegawai ditemukan!')
                        lihatData(id)
                        konfirmasiPecat = input('Konfirmasi pemecatan (Ya/Tidak): ')
                        if konfirmasiPecat.lower() in ['ya', 'y']:
                            print('Pegawai telah dipecat!')
                            dataPegawai.remove(id)
                            simpanPegawai()
                        elif konfirmasiPecat.lower() in ['tidak', 't']:
                            print('Pemecatan dibatalkan!')
                    elif id['idPegawai'] != pecatPegawai:
                        konfirmasiInputId = input('ID pegawai tidak ditemukan!, masukkan ulang id? (Ya/Tidak): ')
                        if konfirmasiInputId.lower() in ['ya', 'y']:
                            pecatPegawai = input('ID pegawai yang akan dipecat: ').upper()
                            for id in dataPegawai:
                                if id['idPegawai'] == pecatPegawai:
                                    print('Pegawai ditemukan!')
                                    lihatData(id)
                                    konfirmasiPecat = input('Konfirmasi pemecatan (Ya/Tidak): ')
                                    if konfirmasiPecat.lower() in ['ya', 'y']:
                                        print('Pegawai telah dipecat!')
                                        dataPegawai.remove(id)
                                        simpanPegawai()
                                    elif konfirmasiPecat.lower() in ['tidak', 't']:
                                        print('Pemecatan dibatalkan!')
                        elif konfirmasiInputId.lower() in ['tidak', 't']:
                            print('Opsi pemecatan batal!')
               
            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['ya','y']:
               print("Program dijalankan!")
               continue
            elif konfirmasiKeluar.lower() in ['tidak', 't']:  
                print('Anda keluar dari program!')
                break
            else:
                print('Pilihan tidak ada!')
                print('Otomatis keluar program!')
                break

        case '5':
            idPegawaiPromosi = input('Masukkan ID Pegawai yang akan dipromosikan: ').upper()
            if not idPegawaiPromosi or not re.fullmatch(r'P\d{3}', idPegawaiPromosi):
                print('ID tidak boleh kosong atau tidak sesuai format!')
                konfirmasiInputId = input('Masukkan ulang id? (Ya/Tidak): ')
                if konfirmasiInputId.lower() in ['ya', 'y']:
                    idPegawaiPromosi = input('Masukkan ID Pegawai: ')
                    if not idPegawaiPromosi or not re.fullmatch(r'P\d{3}', idPegawaiPromosi):
                        print('ID tidak boleh kosong atau tidak sesuai format!')
                        print('Otomatis keluar program!')
                    elif idPegawaiPromosi or re.fullmatch(r'P\d{3}', idPegawaiPromosi):
                        for id in dataPegawai:
                            if id['idPegawai'] == idPegawaiPromosi:
                                print('Pegawai ditemukan!')
                                lihatData(id)
                                konfirmasiPromosi = input('Konfirmasi promosi (Ya/Tidak): ')
                                if konfirmasiPromosi.lower() in ['ya', 'y']:
                                    if id['statusPegawai'] == 'Tetap':
                                        print('Status pegawai sekarang adalah pegawai tetap!')
                                        print('Pegawai tidak dapat dipromosikan!')
                                    elif id['statusPegawai'] == 'Magang':
                                        id['statusPegawai'] = 'Kontrak'
                                        print('Pegawai telah dipromosikan!')
                                        simpanPegawai()
                                        konfirmasiNaikGaji = input('Naikkan gaji (Ya/Tidak): ')
                                        if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                            naikGaji = input('Nominal Gaji (bukan ditambah): ')
                                            id['gajiPegawai'] = naikGaji
                                            simpanPegawai()
                                        elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                            print('Gaji tidak dinaikkan!')
                                    elif id['statusPegawai'] == 'Kontrak':
                                        id['statusPegawai'] = 'Tetap'
                                        print('Pegawai telah dipromosikan!')
                                        simpanPegawai()
                                        konfirmasiNaikGaji = input('Naikkan gaji (Ya/Tidak): ')
                                        if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                            naikGaji = input('Nominal Gaji (bukan ditambah): ')
                                            id['gajiPegawai'] = naikGaji
                                            simpanPegawai()
                                        elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                            print('Gaji tidak dinaikkan!')
                                elif konfirmasiPromosi.lower() in ['tidak', 't']:
                                    print('Opsi naik jabatan dibatalkan!')
                            if id['idPegawai'] != idPegawaiPromosi:
                                print('Pegawai tidak ditemukan!')
                                print('Otomatis keluar dari opsi naik pangkat!')
                                                                
            elif idPegawaiPromosi or re.fullmatch(r'P\d', idPegawaiPromosi):
                for id in dataPegawai:
                    if id['idPegawai'] == idPegawaiPromosi:
                        print('Pegawai ditemukan!')
                        lihatData(id)
                        konfirmasiPromosi = input('Konfirmasi promosi (Ya/Tidak): ')
                        if konfirmasiPromosi.lower() in ['ya', 'y']:
                            if id['statusPegawai'] == 'Tetap':
                                print('Status pegawai sekarang adalah pegawai tetap!')
                                print('Pegawai tidak dapat dipromosikan!')
                            elif id['statusPegawai'] == 'Kontrak':
                                id['statusPegawai'] = 'Tetap'
                                print('Pegawai telah dipromosikan, menjadi pegawai tetap!')
                                simpanPegawai()
                                konfirmasiNaikGaji = input('Naikkan gaji (Ya/Tidak): ')
                                if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                    naikGaji = input('Nominal Gaji (bukan ditambah): ')
                                    id['gajiPegawai'] = naikGaji
                                    simpanPegawai()
                                elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                    print('Gaji tidak dinaikkan!')
                            elif id['statusPegawai'] == 'Magang':
                                id['statusPegawai'] = 'Kontrak'
                                print('Pegawai telah dipromosikan, menjadi pegawai kontrak!')
                                simpanPegawai()
                                konfirmasiNaikGaji = input('Naikkan gaji (Ya/Tidak): ')
                                if konfirmasiNaikGaji.lower() in ['ya', 'y']:
                                    naikGaji = input('Nominal Gaji (bukan ditambah): ')
                                    id['gajiPegawai'] = naikGaji
                                    simpanPegawai()
                                elif konfirmasiNaikGaji.lower() in ['tidak', 't']:
                                    print('Gaji tidak dinaikkan!')
                        elif konfirmasiPromosi.lower() in ['tidak', 't']:
                            print('Opsi naik jabatan dibatalkan!')
            else:
                print('Inputan tidak sesuai!')
                print('Otomatis keluar dari opsi naik pangkat!')

            konfirmasiKeluar = input('Apakah anda ingin mengulang program? (Ya/Tidak): ')
            if konfirmasiKeluar.lower() in ['ya','y']:
               print("Program dijalankan!")
               continue
            elif konfirmasiKeluar.lower() in ['tidak']:  
                print('Anda keluar dari program!')
                break
            else:
                print('Pilihan tidak ada!')
                print('Otomatis keluar program!')
                break

        case '6':
            konfirmasiKeluarProgram = input('Anda akan keluar program!, konfirmasi (Ya/Tidak): ')
            if konfirmasiKeluarProgram.lower() in ['ya', 'y']:
                print('Anda keluar dari program!')
                break
            elif konfirmasiKeluarProgram.lower() in ['tidak']:
                print('Anda tidak keluar dari program!')
            else:
                print('Konfirmasi tidak valid')
        case _:
            print('Pilihan tidak tersedia!')
            print('Masukkan opsi yang tersedia!')
