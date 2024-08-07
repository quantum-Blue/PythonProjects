def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir")

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranizi alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı? (e/h) ').lower()
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranizi alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            print("Bakiye yetersiz")

sadikHesap = {
    'ad': 'Sadik Turan',
    'hesapNo': '123456',
    'sifre': '123',
    'bakiye': 2000,
    'ekHesap': 1500
}

paraCek(sadikHesap, 3000)

print("* " * 20)

paraCek(sadikHesap, 2000)



