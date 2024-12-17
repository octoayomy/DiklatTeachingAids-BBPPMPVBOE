while True:
    total_belanja = float (input("Total Belanja : Rp"))
    bayar = total_belanja

    if total_belanja > 100000:
        print ("Kamu mendapatkan bonus minuman dingin")
        print ("dan diskon 5%")
        diskon = total_belanja * 5/100
        bayar = total_belanja - diskon
        
    print ("Total yang harus dibayar : Rp. ", bayar)
    print ("Terimakasih sudah berbelanja")
    print ("Datang lagi ya...")
