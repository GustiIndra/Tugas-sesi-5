class penjualan:
    id = None
    nama_barang = None
    harga = None
    Jumlah = None

    def TOKO_ABAH(self):
        print(f'TOKO_ABAH')
        print(f'ID :{self.id}')
        print(f'Nama Barang: {self.nama_barang}')
        print(f'Harga: {self.harga}')
        print(f'Jumlah: {self.Jumlah}')
         

gusti = penjualan()
gusti.id = "12"
gusti.nama_barang = "OREO"
gusti.harga = "RP.2500"
gusti.Jumlah = "1"

gusti.TOKO_ABAH()

