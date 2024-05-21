class Mahasiswa:

    def __init__(self, name):
        self.name = name
        self.sks = 0

    def tambah_sks(self, jumlah_sks):
        self.sks += jumlah_sks
        print(f'{self.name} menambah {jumlah_sks} SKS.')
        return self.sks

class SIAKADU:

    def __init__(self):
        self.data_mahasiswa = {}

    def tambah_mahasiswa(self, mahasiswa):
        self.data_mahasiswa[mahasiswa.name] = mahasiswa

    def tampilkan_total_sks(self, nama_mahasiswa):
        if nama_mahasiswa in self.data_mahasiswa:
            mahasiswa = self.data_mahasiswa[nama_mahasiswa]
            print(f'Total SKS {mahasiswa.name} sekarang adalah {mahasiswa.sks}')
        else:
            print(f'Mahasiswa dengan nama {nama_mahasiswa} tidak ditemukan.')

siakadu = SIAKADU()

mahasiswa1 = Mahasiswa('Mahasiswa A')
mahasiswa2 = Mahasiswa('Mahasiswa B')

siakadu.tambah_mahasiswa(mahasiswa1)
siakadu.tambah_mahasiswa(mahasiswa2)

mahasiswa1.tambah_sks(3)
siakadu.tampilkan_total_sks('Mahasiswa A')
print("\n")
mahasiswa2.tambah_sks(4)
siakadu.tampilkan_total_sks('Mahasiswa B')
print("\n")
mahasiswa1.tambah_sks(2)
siakadu.tampilkan_total_sks('Mahasiswa A')
print("\n")
mahasiswa2.tambah_sks(3)
siakadu.tampilkan_total_sks('Mahasiswa B')
