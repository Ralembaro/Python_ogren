print("""********************
Kullanıcı Girişi

1. İşlem : Bakiye Sorgula

2. İşlem : Para yatır

3. İşlem : Para çek
********************""")

sys_kullanıcı_adı = "Emin"
sys_parola = "12345"

Deneme = 3

bakiye = 1000
artı_para = 500
kullanılabilir_limit = bakiye + artı_para

while True:
    kullanıcı_adı = input("Kullanıcı Adınızı girin: ")
    parola = input("Parolanızı girin: ")

    if Deneme < 1:
        print("Giriş hakkınız bitti.")
        break

    elif kullanıcı_adı == "q" or parola == "q":
        print("Yine bekleriz...")
        break

    if sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola:
        print("Parolayı yanlış girdiniz...")
        Deneme -= 1

    elif sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola:
        print("Kullanıcı adını yanlış girdiniz...")
        Deneme -= 1

    elif sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola:
        print("Kullanıcı adını ve parolayı yanlış girdiniz...")
        Deneme -= 1

    else:
        print("Hoşgeldiniz!")
        while True:
            işlem = input("Yapmak istediğiniz işlemi girin: ")

            if işlem == "q":
                break
            elif işlem == "1":
                print("Hesabınızda {} liranız var.".format(bakiye))
            elif işlem == "2":
                miktar = int(input("Yatırmak istediğiniz tutarı girin: "))
                if artı_para < 500:
                    artı_para += miktar
                    if artı_para >= 500:
                        bakiye = artı_para - 500
                        artı_para = 500
                    else:
                        continue
                else:
                    bakiye += miktar
                print("Yeni bakiyeniz {} liradır.".format(bakiye))
            elif işlem == "3":
                miktar = int(input("Çekmek istediğiniz tutarı girin: "))
                kullanılabilir_limit = bakiye + artı_para
                if miktar > kullanılabilir_limit:
                    print("Bakiye yetersiz...")
                elif miktar > bakiye and miktar <= kullanılabilir_limit:
                    print("Artı paranızdan kullanmak ister misiniz?")
                    cevap = input("Evet: E - Hayır: H")
                    if cevap == "E":
                        bakiye = 0
                        kullanılabilir_limit -= miktar
                        artı_para = kullanılabilir_limit
                        print("Bakiyeniz: 0\nKullanılabilir Limitiniz: {}".format(kullanılabilir_limit))
                    else:
                        continue
                elif miktar <= bakiye:
                    bakiye -= miktar
                    print("Yeni bakiyeniz: {}".format(bakiye))
            else:
                print("Geçersiz işlem")