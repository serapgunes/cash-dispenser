print("""---İSTİNYE BANKA HOŞGELDİNİZ---
\t----------------------
\t\tİSTANBUL\t""")
import time
zaman = time.ctime()
print(zaman)
print("""\t----------------------""")
print(
"""1-Giriş Yap
2-Çıkış Yap
>>""")

baslangic= int(input())

def geri_kismi():
    print(
"""1-Giriş Yap
2-Çıkış Yap
>>""")
    tekrar_sec = int(input("Seçiniz:"))
    if (tekrar_sec == 1):
        return ana_menu()
    if (tekrar_sec == 2):
        print("Görüşmek Üzere!")
def ana_menu():
    print("""
    1-Yönetici Girişi
    2-Kullanıcı Girişi
    3-Geri Git
    """)
    istek = int(input("Bir seçeneği seçiniz!"))
    if(istek==1):
        print("yönetici girişi")
    if(istek==2):
        return kullanici_bilgileri(0)
    if(istek==3):
        return geri_kismi()
def menu2(kullanici_ad):
    print(""" 
                   Hoşgeldin %s!

                   Lütfen Yapmak İstediğin Bir İşlem Seç!
                   1. Para çekmek
                   2. Para Transferi
                   3. Para Yatırma
                   4. Hesap Bilgilerim
                   5. Çıkış Yap

                          """ % kullanici_ad)
    secim = int(input('Yapmak istediğiniz işlemi seçiniz'))
    if (secim > 5 or secim < 1):
        secim = menu2(kullanici_ad)
    return (secim)
def kullanici_bilgileri(secim):
    sozluk = {"Ahmed": ['1234'], "Zeynep": ['4321'], "Alberto": ['4422']}
    kullanici_ad = input("kullanıcı adı:")
    password = input("password:")
    while (kullanici_ad not in list(sozluk.keys())):
        print("kullanıcı adı yanlış")
        kullanici_ad = input("kullanıcı adı:")
        password = input("password:")
    while (sozluk[kullanici_ad][0] != password):
        print("şifre yanlış")
        password = input("password:")
    kullanici_bakiyeleri = {"Ahmed": {"Bakiye": 5000, "para çekme": [], "para yatırma": [],"transfer":[]},"Zeynep":{"Bakiye": 5000, "para çekme": [], "para yatırma": [], "transfer":[]}, "Alberto":{"Bakiye": 5000, "para çekme": [], "para yatırma": [], "transfer":[]}}
    while (secim > 5 or secim < 1):
      secim = menu2(kullanici_ad)
    while(secim > 0 or secim < 6):
        if (secim == 1):
            miktar = int(input('çekmek istediğiniz miktarı giriniz'))
            bakiye = kullanici_bakiyeleri[kullanici_ad]['Bakiye']
            if (miktar < bakiye):
                bakiye -= miktar
                metin = f"Bu tarihte {zaman} {miktar} TL Çekildi!"
                kullanici_bakiyeleri[kullanici_ad]['Bakiye'] = bakiye
                kullanici_bakiyeleri[kullanici_ad]['para çekme'] = miktar
                kullanici_bakiyeleri[kullanici_ad]['para çekme'] = f"Bu tarihte {zaman} {miktar} TL Para Çekildi!"
                print(metin)
                print("Yeni bakiye:",bakiye)
                secim =  menu2(kullanici_ad)
            else:
                print('Yetersiz bakiye!')
                secim = menu2(kullanici_ad)
        elif (secim == 3):
            miktar2 = int(input('Yatırmak istediğiniz miktarı giriniz'))
            bakiye = kullanici_bakiyeleri[kullanici_ad]['Bakiye']
            bakiye += miktar2
            kullanici_bakiyeleri[kullanici_ad]['Bakiye'] = bakiye
            metin2 = f"Bu tarihte {zaman} {miktar2} TL Yatırıldı!"
            kullanici_bakiyeleri[kullanici_ad]['para yatırma'] = miktar2
            kullanici_bakiyeleri[kullanici_ad]['para yatırma'] = f"Bu tarihte {zaman} {miktar2} TL Para Yatırıldı!"
            print(metin2)
            print("Yeni bakiye:",bakiye)
            secim = menu2(kullanici_ad)
        elif (secim == 2):
            print("Transfer edilecek kullanıcı adını giriniz:")
            transfer = str(input(""))
            while (transfer == kullanici_ad or transfer != kullanici_ad not in list(sozluk.keys())):
                print("""Kullanıcı bulunmamaktadır!
                              1-Menüye Dön
                              2-Tekrar transfer yap
                              """)
                secim = int(input("İşlem seçiniz:"))
                if (secim == 1):
                    secim = menu2(kullanici_ad)
                elif (secim == 2):
                    transfer = str(input("Transfer edilicek kullanıcı adını giriniz:"))
                islem = int(input("Transfer etmek istediğiniz miktarı giriniz:"))
                if (islem <= kullanici_bakiyeleri[kullanici_ad]['Bakiye']):
                    _transfer = kullanici_bakiyeleri[transfer]['Bakiye']
                    _transfer += islem
                    kullanici_bakiyeleri[transfer]['Bakiye'] = _transfer
                    kullanici_bakiyeleri[transfer]['transfer'] = islem
                    bakiyesi = kullanici_bakiyeleri[kullanici_ad]['Bakiye']
                    bakiyesi -= islem
                    kullanici_bakiyeleri[kullanici_ad]['Bakiye'] = bakiyesi
                    kullanici_bakiyeleri[kullanici_ad]['transfer']= f"Bu tarihte {zaman} {islem} TL Transfer Edildi!"
                    metin3 = f"Bu tarihte {zaman} {islem} TL Transfer Edildi!"
                    print(metin3)
                    print(bakiyesi)
                    secim = menu2(kullanici_ad)
                else:
                    print("""Yetersiz bakiye!
                            1-Menüye Dön
                            2-Tekrar transfer yap""")
                secenek = int(input("İşlem seçiniz:"))
                if (secenek == 1):
                    secim = menu2(kullanici_ad)
                elif(secenek ==2):
                    transfer = str(input("Transfer edilicek kullanıcı adını giriniz:"))
            else:
                islem = int(input("Transfer etmek istediğiniz miktarı giriniz:"))
                if (islem <= kullanici_bakiyeleri[kullanici_ad]['Bakiye']):
                    _transfer = kullanici_bakiyeleri[transfer]['Bakiye']
                    _transfer += islem
                    kullanici_bakiyeleri[transfer]['Bakiye'] = _transfer
                    kullanici_bakiyeleri[transfer]['transfer'] = islem
                    bakiyesi = kullanici_bakiyeleri[kullanici_ad]['Bakiye']
                    bakiyesi -= islem
                    kullanici_bakiyeleri[kullanici_ad]['Bakiye'] = bakiyesi
                    metin3 = f"Bu tarihte {zaman} {islem} TL Transfer Edildi!"
                    kullanici_bakiyeleri[kullanici_ad]['transfer']= f"Bu tarihte {zaman} {islem} TL Transfer Edildi!"
                    print(metin3)
                    print(bakiyesi)
                    secim = menu2(kullanici_ad)
        elif (secim == 4):
            print(f"İSTİNYE BANK \n {zaman}")
            print("Kullanıcı Adı:", kullanici_ad)
            print("Şifre:", sozluk[kullanici_ad][0])
            print("Bakiye:",kullanici_bakiyeleri[kullanici_ad]["Bakiye"])
            print("Çekilen Miktar:",kullanici_bakiyeleri[kullanici_ad]["para çekme"])
            print("Para Yatırma Miktarı:",kullanici_bakiyeleri[kullanici_ad]["para yatırma"])
            print("Transfer İşlemi Miktar:",kullanici_bakiyeleri[kullanici_ad]["transfer"])
            secim = menu2(kullanici_ad)
        elif (secim == 5):
            print("Görüşmek Üzere!")
            break
def bankaya_giris():
    if (baslangic == 1):
        return ana_menu()
    else:
        print("Görüşmek Üzere!")

bankaya_giris()


