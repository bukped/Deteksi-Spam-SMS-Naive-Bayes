#buat file dengan nama fungsi_3.py
def cetak_perolehan_nilai( nama, instagram, *scores):
    print("Nama : ", nama)
    print("Instagram : ", instagram)
    print("Score yang diperoleh : ")
    i = 1
    for score in scores:
        print("nilai ke - %d : %d" % (i, score))
        i= i + 1
    return;
# kalau parameter diisi semua
print("Dengan adanya variable-length variabel sisa akan menjadi tuple : ")
cetak_perolehan_nilai("Zaky Muhammad Yusuf", "@zaky.yusuff", 90, 80, 95, 96, 97)
