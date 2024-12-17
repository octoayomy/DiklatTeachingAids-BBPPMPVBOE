def segiTiga(a,t):
    luas = (a*t)/2
    print("Luas Segitiga : Alas ",a," dan Tinggi ",t,"=" ,luas)

def segiEmpat(p,l):
    ls = p*l
    return ls

segiTiga(10,20)

p= int(input("Masukkan Panjang :"))
l= int(input("Masukkan lebar : "))
print ("Luas segi Empat Panjang ",p,"dan Lebar ",l, "=", segiEmpat(p,l))