# Membuat sistem data nama siswa

# import modul
import crud

# tampung data
daftar_kontak = []
daftar_kontak.append({
    "nama": "asraf",
    "no": "089765765345",
    "cita": "developer"

})

while True:
    print("""
Menu Sistem MyContact:
    1. Tampilkan Data
    2. Tambah Data
    3. Cari Data
    4. Hapus Data
    0. Exit For Sistem
    """)
    inputMenu = int(input("Menu Pilihan [Number]: "))

    if inputMenu == 0:
        break
    elif inputMenu == 1:
        crud.tampilkanData(daftar_kontak)
    elif inputMenu == 2:
        newDict = crud.tambahData()
        daftar_kontak.append(newDict)
    elif inputMenu == 3:
        crud.cariData(daftar_kontak)
    elif inputMenu == 4:
        crud.hapusData(daftar_kontak)

print("Timaksih User Selsai")
