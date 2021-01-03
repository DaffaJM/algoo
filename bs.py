
import csv
#mengimpor modul csv

import os
#mengimpor modul os

import time
#import modul time

csv_filename = 'buku.csv'
#nama csv file

#fungsi untuk menghapus layer 
def clear():
    os.system('cls')

#fungsi untuk kembali 
def back_to_menu():
    print('\n')
    input('Tekan Enter untuk kembali')
    show()

#fungsi untuk login akun 
def login():
    clear()

    #membuat inputan untuk membuat username dan password untuk login
    username = input('Masukkan Username yang Akan dibuat: ')
    password = input('Masukkan Password yang Akan dibuat: ')

    user = input('Username: ')
    sandi = input('Password: ')
    if user == username and sandi == password:
        print('Login Berhasil')
    else:
        print('Username atau Password yang anda masukkan salah !!!')
    
    back_to_menu()

#fungsi untuk melihat daftar yg ada di file csv
def show_buku():
    clear()
    
    print('Tunggu Sebentar...')
    time.sleep(2)

    buku = []
    #untuk membuka file csv dengan mode 'r' / baca
    with open(csv_filename, mode='r') as csv_file:
        baca = csv.DictReader(csv_file)
        #untuk mengeluarkan data menggunakan perulangan
        for row in baca:
            buku.append(row)
    row_count = sum(1 for row in buku)

    print('='*70)
    print('\t\t\tDaftar Stok Buku ')
    print('='*70)

    print('Kode \t Judul \t\t Tarif \t\t Tanggal \t Kembali')
    print('='*70)

    #membuat perulangan untuk mengeluarkan data
    for data in buku:
        print(f"{data['Kode']} \t {data['Judul']} \t {data['Tarif']} \t\t {data['Tanggal']} \t {data['Kembali']}")
    print('='*70)
    print('Total Data : ',row_count)
    print('='*70)

    back_to_menu()

#fungsi menambah data baru
def tambah_buku():
    clear()
    #menggunakan mode a atau append
    with open(csv_filename, mode='a', newline='') as csv_file:

        print('==========TAMBAH BUKU===========')
        kode = input('Masukkan Kode :')
        judul = input('Masukkan Judul Buku : ')
        tarif = input('Masukkan Tarif Sewa : ')
        tanggal = input('Masukkan Tanggal saat Pinjam : ')
        kembali = input('Masukkan Tanggal Pengembalian: ')
        item = [kode, judul, tarif, tanggal, kembali]
        #nilai variable inputan tadi ditulis ke file csv
        tambah = csv.writer(csv_file, delimiter=',')
        tambah.writerow(item)
    
    print('Sedang Menambah Data Baru Tunggu Sebentar....')
    time.sleep(2)

    print('Data Buku Berhasil Ditambah')
    back_to_menu()

#fungsi menghapus data
def delete_data():
    clear()
    buku = []
    #untuk membuka file csv dengan mode 'r' / baca
    with open(csv_filename, mode='r') as csv_file:
        baca = csv.DictReader(csv_file)
        #membuat perulangan untuk memunculkan data  
        for row in baca:
            buku.append(row)

    print('Kode \t Judul \t\t Tarif \t\t Tanggal \t Kembali')
    print('='*70)

    #untuk memunculkan data sesuai keterangan
    for data in buku:
        print(f"{data['Kode']} \t {data['Judul']} \t {data['Tarif']} \t\t {data['Tanggal']} \t {data['Kembali']}")

    kode = input('Hapus Data dengan Kode Buku : ')

    #membuat perulangan untuk memunculkan data kode
    indeks = 0
    for data in buku:
        if (data['Kode'] == kode):
            buku.remove(buku[indeks])
        indeks = indeks + 1

    #menulis data baru ke file csv/menulis ulang mode write
    with open(csv_filename, mode='w') as csv_file:
        keterangan = ['Kode', 'Judul', 'Tarif', 'Tanggal', 'Kembali']
        writer = csv.DictWriter(csv_file, fieldnames=keterangan)
        writer.writeheader()
        for baru in buku:
            writer.writerow({'Kode': baru['Kode'], 'Judul': baru['Judul'], 'Tarif': baru['Tarif'], 'Tanggal': baru['Tanggal'], 'Kembali': baru['Kembali']})
    print('Data Sedang Dihapus Tunggu Sebentar...')
    time.sleep(2)
    print('Data Berhasil Dihapus')
    back_to_menu()

#fungsi untuk mengedit data
def edit_data():
    clear()
    buku = []
    #menggunakan mode read atau baca
    with open(csv_filename, mode='r',newline='') as csv_file:
        baca = csv.DictReader(csv_file)
        #membuat perulangan untuk memunculkan data
        for row in baca:
            buku.append(row)
    #untuk memunculkan jumlah info data
    row_count = sum(1 for row in buku)
    
    print('='*70)
    print('\t\t\tDaftar Stok Buku')
    print('='*70)

    print('Kode \t Judul \t\t Tarif \t\t Tanggal \t Kembali')
    print('='*70)

    #memunculkan data yg ada pada keterangan
    for data in buku:
        print(f"{data['Kode']} \t {data['Judul']} \t {data['Tarif']} \t\t {data['Tanggal']} \t {data['Kembali']}")

    print('='*70)
    print('Total Data : ',row_count)
    print('='*70)
    #membuat inputan baru
    kode = input('Masukkan Kode yang Ingin Diubah:')
    judul = input('Masukkan Judul Buku Baru : ')
    tarif = input('Masukkan Tarif Sewa Baru : ')
    tanggal = input('Masukkan Tanggal saat Pinjam Baru : ')
    kembali = input('Masukkan Tanggal Pengembalian Baru: ')

    #untuk mencari buku dan mengubah datanya dengan data yang baru menggunakan perulangan
    indeks = 0
    for data in buku:
        if (data['Kode'] == kode):
            buku[indeks]['Judul'] = judul
            buku[indeks]['Tarif'] = tarif
            buku[indeks]['Tanggal'] = tanggal
            buku[indeks]['Kembali'] = kembali 
        indeks = indeks + 1
    
    #menulis data baru dengan mode w atau write
    with open(csv_filename, mode='w') as csv_file:
        keterangan = ['Kode', 'Judul', 'Tarif', 'Tanggal', 'Kembali']
        writer = csv.DictWriter(csv_file, fieldnames=keterangan)
        writer.writeheader()
        for baru in buku:
            writer.writerow({'Kode': baru['Kode'], 'Judul': baru['Judul'], 'Tarif': baru['Tarif'], 'Tanggal': baru['Tanggal'], 'Kembali': baru['Kembali']})
    print('Data Sedang Diedit Tunggu Sebentar...')
    time.sleep(2)
    print('Data Berhasil Diedit')
    back_to_menu()

#fungsi menampilkan menu utama
def show():
    clear()
    buku = []
    #membaca file csv dengan mode 'r' / baca
    with open(csv_filename, mode='r') as csv_file:
        baca = csv.DictReader(csv_file)
    #membuat perulangan    
        for row in baca:
            buku.append(row)
    row_count = sum(1 for row in buku)

    print('===SELAMAT DATANG DI PROGRAM KAMI=== \n')
    print('=========== MENU UTAMA =============')
    print('Info Total Buku : ',row_count)
    print('============================')
    print('[1]Login')
    print('[2]Lihat Daftar Buku')
    print('[3]Tambah Buku')
    print('[4]Edit Buku')
    print('[5]Hapus Buku')
    print('[0]Keluar \n')
    inputPilihan = input('Pilih Menu : ')

    #membuat percabangan 
    if(inputPilihan == '1'):
        login()
    if(inputPilihan == '2'):
        show_buku()
    if(inputPilihan == '3'):
        tambah_buku()
    if(inputPilihan == '4'):
        edit_data()
    if(inputPilihan == '5'):
        delete_data()
    if(inputPilihan == '0'):
        exit()
    else:
        print('Pilihan yang anda pilih harus ada di menu!!!')
        back_to_menu()

#untuk memanggil fungsi menu utama
if __name__ == "__main__":
    while True:
        show()