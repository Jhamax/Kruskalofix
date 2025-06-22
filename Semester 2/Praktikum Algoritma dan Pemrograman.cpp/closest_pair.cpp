#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

struct Titik
{
    int x, y;
};

// Fungsi untuk menghitung jarak Euclidean antara dua titik
double hitungJarak(Titik a, Titik b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

// Fungsi untuk mengecek jarak terkecil dengan metode brute force pada subarray titik dari index mulai ke akhir
double cekSemuaPasang(const vector<Titik> &titik, int mulai, int akhir)
{
    double jarakTerkecil = 1e9; // Inisialisasi jarak dengan nilai sangat besar
    for (int i = mulai; i < akhir; i++)
    {
        for (int j = i + 1; j <= akhir; j++)
        {
            double jarak = hitungJarak(titik[i], titik[j]); // Hitung jarak tiap pasangan
            if (jarak < jarakTerkecil)
                jarakTerkecil = jarak; // Update jarak terkecil jika ditemukan jarak lebih kecil
        }
    }
    return jarakTerkecil;
}

// Fungsi utama untuk mencari jarak terkecil menggunakan pendekatan Divide and Conquer
double cariJarakTerkecil(vector<Titik> &titik, int mulai, int akhir)
{
    // Jika jumlah titik sedikit (3 atau kurang), gunakan metode brute force
    if (akhir - mulai <= 2)
    {
        return cekSemuaPasang(titik, mulai, akhir);
    }

    // DIVIDE
    int tengah = (mulai + akhir) / 2;   // titik tengah
    int xTengah = titik[tengah].x;      // simpan titik tengah    
    // DIVIDE AKHIR

    // CONQUER
    double jarakKiri = cariJarakTerkecil(titik, mulai, tengah);       // Rekursif cari jarak terkecil di kiri
    double jarakKanan = cariJarakTerkecil(titik, tengah + 1, akhir);  // Rekursif cari jarak terkecil di kanan
    double jarakMin = min(jarakKiri, jarakKanan);                     // Ambil jarak terkecil dari kiri dan kanan
    // CONQUER AKHIR

    // COMBINE
    vector<Titik> strip; // Kumpulan titik yang dekat dengan garis tengah (jarak x < jarakMin)
    for (int i = mulai; i <= akhir; i++)
    {
        if (abs(titik[i].x - xTengah) < jarakMin)
        {
            strip.push_back(titik[i]);
        }
    }

    // Urutkan strip berdasarkan koordinat y
    sort(strip.begin(), strip.end(), [](Titik a, Titik b)
         { return a.y < b.y; });

    // Cek jarak antar titik di strip yang mungkin lebih kecil dari jarakMin
    for (int i = 0; i < (int)strip.size(); i++)
    {
        // Bandingkan dengan titik-titik berikutnya selama jarak y kurang dari jarakMin
        for (int j = i + 1; j < (int)strip.size() && (strip[j].y - strip[i].y) < jarakMin; j++)
        {
            double jarakStrip = hitungJarak(strip[i], strip[j]);
            if (jarakStrip < jarakMin)
                jarakMin = jarakStrip; // Update jarakMin jika ditemukan jarak yang lebih kecil
        }
    }
    // COMBINE AKHIR

    return jarakMin; // Kembalikan jarak terkecil yang ditemukan
}

int main()
{
    vector<Titik> titik = {{1, 1}, {3, 4}, {7, 8}, {4, 3}, {2, 2}};
    
    // Urutkan titik berdasarkan koordinat x sebagai persiapan algoritma Divide and Conquer
    sort(titik.begin(), titik.end(), [](Titik a, Titik b)
         { return a.x < b.x; });

    // Panggil fungsi utama untuk mencari jarak terkecil antar titik
    double hasil = cariJarakTerkecil(titik, 0, titik.size() - 1);

    cout << "Jarak terkecil adalah: " << hasil << endl;

    return 0;
}

/*
Divide: Membagi titik menjadi dua bagian berdasarkan posisi tengah pada koordinat x.
Conquer: Cari jarak terkecil secara rekursif di bagian kiri dan kanan.
Combine: Gabungkan hasil dengan mencari jarak terkecil di sekitar garis tengah.
*/
