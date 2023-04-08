import os

# Membaca input dari pengguna
filename = input("Masukkan nama file yang ingin diproses: ")
output_filename = input("Masukkan nama file hasil proses: ")

# Memastikan file input benar-benar ada
if not os.path.isfile(filename):
    print("File tidak ditemukan")
    exit()

# Membuka file dan membaca baris-barisnya
lines = []
with open(filename, "r") as f:
    lines = f.readlines()

# Menghitung jumlah baris duplikat
unique_lines = set(lines)
num_duplicates = len(lines) - len(unique_lines)

# Menghapus baris duplikat
lines = list(unique_lines)

# Menulis hasil ke file output
with open(output_filename, "w") as f:
    f.writelines(lines)

# Menampilkan pesan ke konsol
file_size = os.path.getsize(filename) / (1024 * 1024)
print(f"Load File Your File {filename} {file_size:.2f} MB")
print(f"Found Duplicate {num_duplicates} lines")
output_file_size = os.path.getsize(output_filename) / (1024 * 1024)
print(f"Success Remove Duplicate {num_duplicates} lines File saved {output_file_size:.2f} MB")
