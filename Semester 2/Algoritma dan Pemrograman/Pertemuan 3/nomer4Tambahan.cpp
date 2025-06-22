#include <iostream>
#include <fstream>
using namespace std;

int main() {
    float panjang, lebar, luas;
    ifstream Fin("data.txt"); 
    ofstream Fout("hasil.txt"); 

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
