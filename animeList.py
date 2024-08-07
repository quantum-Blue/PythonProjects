def listeOlustur(sayi):
    animeler_listesi = []  
    for _ in range(sayi):
        anime = {
            'name': input('Anime Adı: '),  
            'Skor': int(input('Anime Skoru: ')),  
            'Type': input('Anime Türü (Action, Comedy, Psychologic, Horror, Fantastic, Spor): ')  
        }
        animeler_listesi.append(anime)  
    return animeler_listesi  

def turuneAyir(animeler):
    turler = ['Action', 'Comedy', 'Psychologic', 'Horror', 'Fantastic','Spor']
    siralanmis_animeler = {}
    for tur in turler:
        tur_animeleri = sorted([(anime['name'], anime['Skor']) for anime in animeler if anime['Type'] == tur])
        siralanmis_animeler[tur] = tur_animeleri
    return siralanmis_animeler

animeler = []  
sayi = int(input("Kaç tane anime girmek istersiniz: "))  
animeler = listeOlustur(sayi)  

siralanmis_animeler = turuneAyir(animeler)  

print("Sıralanmış Anime Listesi:")
for tur, animeler in siralanmis_animeler.items():
    print(f"{tur} Animes:")
    for anime, skor in animeler:
        print(f"{anime} - Skor: {skor}")

