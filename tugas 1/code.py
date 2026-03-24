nilai = []
print("masukkan 10 nilai:")
for i in range(10):
  n = int(input("nilai ke-" + str(i+1) + ":"))
  nilai.append(n)

max_nilai = max(nilai)
min_nilai = min(nilai)
rata = sum(nilai)/len(nilai)
lulus = sum(1 for n in nilai if n >= 60)
tidak_lulus = len(nilai) - lulus

print("\n=== HASIL PENGOLAHAN ===")
print("semua nilai:", nilai)
print("nilai terbesar:", max_nilai)
print("nilai terkecil:", min_nilai)
print("nilai rata-rata:", rata)
print("jumlah lulus:", lulus)
print("jumlah tidak lulus:", tidak_lulus)
