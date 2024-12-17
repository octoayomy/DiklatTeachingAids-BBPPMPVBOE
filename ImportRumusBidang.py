import Rumusbidang as rb

rb.segiTiga(10,20)

p = int(input("Masukkan panjang: "))
l = int(input("Masukkan luas: "))
print("Luas segi Empat : panjang ",p, "dan lebar",l,"=", rb.segiEmpat(p,l))

r = float(input("Masukkan jari-jari: "))
print("Luas Lingkaran dengan jari-jari",r,"=", rb.lingkaran(r))