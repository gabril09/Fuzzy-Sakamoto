print("Bagaimana jika jumlah PERMINTAAN = 2500, PERSEDIAAN = 290,")
print("berapa kemasan makanan jenis ABC yang harus diproduksi ?")

print("1.Nilai keanggotan")

print("pmtTurun[2500] = ")
a=((5000-2500)/4000)
print(a)
print("pmtNaik[2500] = ")
b=((2500-1000)/4000)
print(b)
print("psdSedikit[500] = ")
c=((600-290)/500)
print(c)
print("pmtBanyak[500] = ")
d=((290-100)/500)
print(d)

print("\n2. ")

print("[A1] IF Permintaan Naik And Persediaan BANYAK \nTHEN Produksi Barang BERTAMBAH ")
if b < d :
    a1 = b
    print("hasilnya = ",a1)
else :
    a1 = d
    print("hasilnya = ",a1)    
print("[A2] IF permintaan SEDIKIT And Persediaan SEDIKIt \nTHEN produksi Barang BERKURANG")
if a < c :
    a2 = a
    print("hasilnya = ",a2)
else :
    a2 = c
    print("hasilnya = ",a2)    
print("[A3] IF permintaan SEDIKIT And Persediaan BANYAK \nTHEN produksi Barang BERKURANG")
if a < d :
    a3 = a
    print("hasilnya = ",a3)
else :
    a3 = d
    print("hasilnya = ",a3)    
print("[A4] IF permintaan NAIK And Persediaan SEDIKIT \nTHEN produksi Barang BERTAMBAH")
if b < c :
    a4 = b
    print("hasilnya = ",a4)
else :
    a4 = c
    print("hasilnya = ",a4)    

print("\nNilai @-predikat")
print("rule1")
z1 = a1*5000+7000
print("Nilai Predikatnya z1 =",z1)
print("rule2")
z2 = a2*5000+7000
print("Nilai Predikatnya z2 =",z2)
print("rule3")
z3 = a3*5000+7000
print("Nilai Predikatnya z3 =",z3)
print("rule4")
z4 = a4*5000+7000
print("Nilai Predikatnya z4 =",z4)

print("\nNilai Akhir")
na = ((a1*z1)+(a2*z2)+(a3*z3)+(a4*z4))/(a1+a2+a3+a4)
print("Jadi, Jumlah makanan jenis ABC yang harus diproduksi sebanyak = ",int(na))
