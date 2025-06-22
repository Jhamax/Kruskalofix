#include <iostream>
#include <fstream>
using namespace std;

int main() {
    float panjang, lebar, luas;
    char NamaArsip1[20], NamaArsip2[20];

    cout << "Nama arsip masukan: ";
    cin >> NamaArsip1;
    cout << "Nama arsip keluaran: ";
    cin >> NamaArsip2;

    ifstream Fin(NamaArsip1); 
    ofstream Fout(NamaArsip2); 

    if (Fin.is_open() && Fout.is_open()) {
        Fin >> panjang >> lebar;
        luas = panjang * lebar;

        Fout << "Luas segiempat = " << luas << " cm^2" << endl;

        Fin.close();
        Fout.close();
    } else {
        cout << "Gagal membuka file!" << endl;
    }

    return 0;
}
