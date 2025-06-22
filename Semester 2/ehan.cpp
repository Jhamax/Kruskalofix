#include <iostream>
using namespace std;

struct Mahasiswa {
    int NIM;
    string nama, bukuDipinjam;
    Mahasiswa* next;
};

struct Buku {
    string kode, judul, penulis;
    bool tersedia;
    Buku* next;
};

Buku* headBuku = nullptr;
Mahasiswa* headMahasiswa = nullptr;

// ADMIN
void inputBuku(string kode, string judul, string penulis) {
    Buku* newNode = new Buku{kode, judul, penulis, true, nullptr};
    if (headBuku == nullptr) {
        headBuku = newNode;
    } else {
        Buku* temp = headBuku;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    cout << "Data berhasil ditambahkan." << endl;
}

void hapusBuku(string kode){
    Buku* temp = headBuku;
    Buku* prev = nullptr;
    while(temp != nullptr && temp->kode != kode){
        prev = temp;
        temp = temp->next;
    }
    if(temp == nullptr){
        cout << "Buku tidak ditemukan." << endl;
        return;
    }
    if(prev == nullptr){
        headBuku = temp->next;
    } else {
        prev->next = temp->next;
    }
    delete temp;
    cout << "Buku berhasil dihapus." << endl;
}

void listMahasiswa() {
    if (headMahasiswa == nullptr) {
        cout << "Tidak ada mahasiswa yang login" << endl;
        return;
    }   
    Mahasiswa* temp = headMahasiswa;
    int index = 1;
    while (temp != nullptr) {
        cout << "\nData Mahasiswa Ke-: " << index << endl;
        cout << "NIM : " << temp->NIM << endl;
        cout << "Nama : " << temp->nama << endl;
        if (temp->bukuDipinjam == "") {
            cout << "Belum meminjam buku.\n";
        } else {
            cout << "Buku Dipinjam : " << temp->bukuDipinjam << endl;
        }
        temp = temp->next;
        index++;
    }
}

// MAHASISWA
Mahasiswa* loginMahasiswa(int nim, string nama){
    Mahasiswa* newNode = new Mahasiswa{nim, nama, "", nullptr};
    if(headMahasiswa == nullptr){
        headMahasiswa = newNode;
    }
    else {
        Mahasiswa* temp = headMahasiswa;
        while (temp != nullptr) {
            temp = temp->next;
        }
        temp -> next = newNode;
    }
    cout << "Data berhasil ditambahkan." << endl; 
    return newNode;
}

void listBuku() {
    if (headBuku == nullptr) {
        cout << "Tidak ada data buku." << endl;
        return;
    }

    cout << "\nDaftar Buku\n";
    Buku* temp = headBuku;
    int index = 1;

    while (temp != nullptr) {
        cout << "Buku ke-" << index << ": " << endl;
        cout << "Kode: " << temp->kode << endl;
        cout << "Judul: " << temp->judul << endl;
        cout << "Penulis: " << temp->penulis << endl;
        if (temp->tersedia) {
            cout << "Status : Tersedia" << endl;
        } else {
            cout << "Status : Dipinjam" << endl;
        }
        cout << endl;
        temp = temp->next;
        index++;
    }
}

void pinjamBuku(Mahasiswa* mhs, string kode){
    if(mhs->bukuDipinjam != ""){
        cout << "Anda masih memiliki buku yang belum dikembalikan." << endl;
        return;
    }
    Buku* temp = headBuku;
    while(temp != nullptr){
        if(temp->kode == kode && temp->tersedia){
            temp->tersedia = false;
            mhs->bukuDipinjam = kode;
            cout << "Buku berhasil dipinjam." << endl;
            return;
        }
        temp = temp->next;
    }
    cout << "Buku tidak tersedia atau tidak ditemukan." << endl;
}

void kembalikanBuku(Mahasiswa* mhs){
    if(mhs->bukuDipinjam == ""){
        cout << "Anda tidak sedang meminjam buku." << endl;
        return;
    }
    Buku* temp = headBuku;
    while(temp != nullptr){
        if(temp->kode == mhs->bukuDipinjam){
            temp->tersedia = true;
            mhs->bukuDipinjam = "";
            cout << "Buku berhasil dikembalikan." << endl;
            return;
        }
        temp = temp->next;
    }
    cout << "Kesalahan sistem: buku tidak ditemukan." << endl;
}

// MENU
void menuAdmin() {
    int pilihan;
    string kode, judul, penulis;

    do {
        cout << "\n-- MENU ADMIN --\n"; 
        cout << "1. Input Buku" << endl;
        cout << "2. Hapus Buku" << endl;
        cout << "3. Daftar Mahasiswa" << endl;
        cout << "4. Daftar Buku" << endl;
        cout << "5. Logout" << endl; 
        cout << "Pilih menu: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                cout << "Masukan Kode Buku: ";cin >> kode;
                cin.ignore();
                cout << "Masukan Judul Buku: ";getline(cin, judul);
                cout << "Masukan Penulis Buku: ";getline(cin, penulis);
                inputBuku(kode, judul, penulis);
                break;
            case 2:
                cout << "Masukkan Kode Buku yang ingin dihapus: ";
                cin >> kode;
                hapusBuku(kode);
                break;
            case 3:
                listMahasiswa();
                break;
            case 4:
                listBuku();
                break;
            case 5:
                cout << "Anda berhasil Logout." << endl;
                break;
            default:
                cout << "Pilihan tidak ada. Coba lagi." << endl;
        }
    } while (pilihan != 5);
}

void menuMahasiswa(Mahasiswa* mhs) {
    int pilihan;
    string kode;

    do {
        cout << "\n-- MENU MAHASISWA --\n"; 
        cout << "1. List Buku" << endl;
        cout << "2. Peminjaman Buku" << endl;
        cout << "3. Pengembalian Buku" << endl;
        cout << "4. Logout" << endl;
        cout << "Pilih menu: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                listBuku();
                break;
            case 2:
                cout << "Masukan kode buku yang ingin dipinjam: ";
                cin >> kode;
                pinjamBuku(mhs, kode);
                break;
            case 3:
                kembalikanBuku(mhs);
                break;
            case 4:
                cout << "Anda berhasil Logout." << endl;
                break;
            default:
                cout << "Pilihan tidak ada. Coba lagi." << endl;
        }
    } while (pilihan != 4);
}

// MAIN
int main() {
    int pilihan, nim;
    string nama, user, pass;

    do {
        cout << endl;
        cout << "===== SISTEM PERPUSTAKAAN ===== " << endl;
        cout << "1. Login Sebagai Admin" << endl;
        cout << "2. Login Sebagai Mahasiswa" << endl;
        cout << "3. Keluar " << endl;
        cout << "Pilih menu: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                cout << "Masukan Username: ";
                cin >> user;
                cout << "Masukan Password: ";
                cin >> pass;
                if (user != "admin" && pass != "admin123") {
                    cout << "Username dan Password yang anda masukkan salah." << endl;
                } else if (user != "admin") {
                    cout << "Username yang anda masukkan salah." << endl;
                } else if (pass != "admin123") {
                    cout << "Password yang anda masukkan salah." << endl;
                } else {
                    cout << "Login berhasil." << endl;
                    menuAdmin();
                }
                break;
            case 2:
                cout << "Masukan NIM: ";cin >> nim;
                cin.ignore();
                cout << "Masukan Nama: ";getline(cin, nama);
                menuMahasiswa(loginMahasiswa(nim,nama));
                break;
            case 3:
                cout << "Keluar dari program." << endl;
                break;
            default:
                cout << "Pilihan tidak ada. Coba lagi." << endl;
        }
    } while (pilihan != 3);

    return 0;
}