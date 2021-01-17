def tampilkanData(daftar_kontak):
    for kontak in daftar_kontak:
        dictkontak = kontak
        print("="*25)
        for key in dictkontak:
            value = dictkontak[key]
            print(f"{key}: {value}")


def tambahData():
    nama = input("Masukkan Nama : ")
    noHp = input("Masukkan NO.HP: ")
    cita2 = input("Masukkan Cita2: ")
    dictData = {
        "nama": nama,
        "no": noHp,
        "cita": cita2
    }
    return dictData


def cariData(daftar_kontak):
    inputKey = input("Masukkan Nama Yg D Cari: ")
    for kontak in daftar_kontak:
        # dictkontak = kontak
        # for key, value in dictkontak.items():
        #     if value == inputKey:
        #         print(f"Ditemukan key {key}:{value}")
        #     else:
        #         print("data tidak ditemukan")
        nama = kontak["nama"]
        if nama.lower().find(inputKey.lower()) != -1:
            print(f"nama: {kontak['nama']}")
            print(f"nama: {kontak['no']}")
            print(f"nama: {kontak['cita']}")
        # else:
        #     print("==Nama Terkaita Not Found!!==")


def hapusData(daftar_kontak):
    inputNama = input("Nama yang Dihapus: ")

    indexHapus = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if inputNama == kontak["nama"]:
            indexHapus = i
            break
    if indexHapus == -1:
        print("Data Tidak Ditemukan")
    else:
        del daftar_kontak[indexHapus]
        print("Data Berhasil di Hapus")
