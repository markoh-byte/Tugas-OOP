from abc import ABC, abstractmethod

# 1. ABSTRAKSI (Class induk abstrak sebagai template)
class Produk(ABC):
    def __init__(self, nama, harga_asli):
        self.nama = nama
        # 2. ENKAPSULASI (Atribut private '__harga_asli' agar tidak bisa diubah langsung dari luar)
        self.__harga_asli = harga_asli

    # Getter untuk mengakses data private secara aman
    def get_harga_asli(self):
        return self.__harga_asli

    # Method abstrak yang wajib diisi oleh setiap jenis produk
    @abstractmethod
    def hitung_total_harga(self):
        pass


# 3. INHERITANCE (Pewarisan) & 4. POLIMORFISME
class Elektronik(Produk):
    def __init__(self, nama, harga_asli, pajak_persen):
        super().__init__(nama, harga_asli)
        self.pajak_persen = pajak_persen

    # Polimorfisme: Menghitung harga akhir elektronik (Harga + Pajak)
    def hitung_total_harga(self):
        pajak = self.get_harga_asli() * (self.pajak_persen / 100)
        return self.get_harga_asli() + pajak


# 3. INHERITANCE (Pewarisan) & 4. POLIMORFISME
class Pakaian(Produk):
    def __init__(self, nama, harga_asli, diskon_persen):
        super().__init__(nama, harga_asli)
        self.diskon_persen = diskon_persen

    # Polimorfisme: Menghitung harga akhir pakaian (Harga - Diskon)
    def hitung_total_harga(self):
        potongan = self.get_harga_asli() * (self.diskon_persen / 100)
        return self.get_harga_asli() - potongan


# ==========================================
# RUNNING PROGRAM / EXECUTION
# ==========================================
if __name__ == "__main__":
    # Membuat objek dari class turunan
    laptop = Elektronik(nama="Laptop ASUS", harga_asli=10000000, pajak_persen=11)
    kemeja = Pakaian(nama="Kemeja Batik", harga_asli=200000, diskon_persen=20)

    print("=== NOTA PEMBELIAN TOKO ONLINE ===")
    
    # Menampilkan hasil Polimorfisme
    print(f"Produk: {laptop.nama}")
    print(f"Harga Akhir (setelah pajak): Rp{laptop.hitung_total_harga():,}")
    print("-" * 30)
    
    print(f"Produk: {kemeja.nama}")
    print(f"Harga Akhir (setelah diskon): Rp{kemeja.hitung_total_harga():,}")
    print("-" * 30)

    # Membuktikan Enkapsulasi bekerja
    # print(laptop.__harga_asli) # Ini akan ERROR jika diaktifkan karena datanya di-protect
    print(f"Akses Harga Asli Laptop via Getter: Rp{laptop.get_harga_asli():,}")
