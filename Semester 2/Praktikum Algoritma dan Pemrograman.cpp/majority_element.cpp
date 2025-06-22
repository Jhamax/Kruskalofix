#include <iostream>
#include <vector>
using namespace std;

// Fungsi untuk menghitung berapa kali elemen 'num(nilai tertentu)' muncul di subarray dari index 'kiri' sampai 'kanan'
int hitungKemunculan(const vector<int>& A, int num, int kiri, int kanan) {
    int jumlah = 0;
    for (int i = kiri; i <= kanan; i++) {
        if (A[i] == num) jumlah++;
    }
    return jumlah;
}

// Fungsi rekursif untuk mencari elemen mayoritas dengan Divide and Conquer
int cariMayoritas(const vector<int>& A, int kiri, int kanan) {
    // dianggap mayoritas jika 1 elemen (sementara)
    if (kiri == kanan) return A[kiri];

    // DIVIDE
    int tengah = (kiri + kanan) / 2;
    // DIVIDE AKHIR

    // CONQUER
    int kiriMayor = cariMayoritas(A, kiri, tengah);       //kiri
    int kananMayor = cariMayoritas(A, tengah + 1, kanan);  //kanan
    // CONQUER AKHIR

    // COMBINE
    if (kiriMayor == kananMayor) return kiriMayor; //jika kiri dan kanan sama berarti mayoritasnya kiriMayor
    // COMBINE AKHIR

    // jika berbeda, hitung jumlah kemunculan keduanya dan ambil yang lebih banyak
    int jumlahKiri = hitungKemunculan(A, kiriMayor, kiri, kanan);
    int jumlahKanan = hitungKemunculan(A, kananMayor, kiri, kanan);

    return (jumlahKiri > jumlahKanan) ? kiriMayor : kananMayor;
}

int main() {
    // Contoh input
    vector<int> A = {3, 3, 4, 2, 3, 3, 3};
    int n = A.size();

    // Panggil fungsi utama Divide and Conquer
    int calonMayor = cariMayoritas(A, 0, n - 1);

    // Hitung apakah benar-benar mayoritas (> n/2)
    int jumlah = hitungKemunculan(A, calonMayor, 0, n - 1);

    if (jumlah > n / 2)
        cout << "Elemen mayoritas adalah: " << calonMayor << endl;
    else
        cout << "Tidak ada elemen mayoritas." << endl;

    return 0;
}
