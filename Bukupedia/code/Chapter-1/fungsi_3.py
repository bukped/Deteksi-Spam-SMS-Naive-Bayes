def cetak_biodata( nama, kota, umur=21):
    print("Nama : ", nama)
    print("Umur : ", umur)
    print("Kota : ", kota)
    return;
# kalau parameter diisi semua
print("Tanpa memakai default argument : ")
cetak_biodata( nama="zaky", umur=22, kota="bandung" )
print("\n")
# kalau parameter tidak diisi semua
print("Memakai default argument : ")
cetak_biodata(kota="bandung", nama="zaky")


