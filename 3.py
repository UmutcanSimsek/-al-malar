
seçim_ekrani = """

1 - Spiderman
2 - İronMan
3 - Superman

"""

print(seçim_ekrani)

anahtar = 20

while anahtar ==20:
    soru = input("Oynamak istediğiniz kahramanı seçiniz (çıkış yapmak için u)")

    if soru == "u":
        print("çıkış yapılıyor....")
        anahtar = 0
    
    elif soru =="1":
        print("""
        _____Spiderman kahramanını seçtiniz_____
       
        Yetenekleri:
       
        Q : Ağ perdesi  
        Ağ perdesi düşmanların görüşünü bir süreliğine daraltır  
        
        C : Ağ tuzağı 
        Ağ tuzağı yakalanan düşmanlarının yerini gösterir  
       
        R : Ağ bombası
        Ağ bombası menzilinde olan bütün düşmanlarını katleder
        
        """)

    elif soru =="2":
        print("""
        _____İron Man kahramanını seçtiniz_____
        
        yetenekleri:

        Q : El Lazaeri
        El lazeri isabet halinde düşmanlara belli miktarda hasar verir

        C : Kör edici ışın
        Kör edici ışın'ın görüşünde olan düşmanlar geçici süreliğine kör olurlar

        R : Sinyal kesici
        Sinyal kesici aktifleştiğinde düşmanların iletişimini 40 sn liğine keser
    
        """)

    elif soru =="3":
        print("""
        _____Spuerman kahramanını seçtiniz_____

        Yetenekeri:

        Q : Göz lazeri 
        Göz lazeri isabet halinde düşmanlara belli miktarda hasar verir

        C : Uçma
        Bir pelerin takar ve belli bir süre havada süzülür

        R : Hasar görmeme
        Belli bir süre hasar almazsın fakat ateşde edemezsin 
        
        """)
    else:
        print("Oyuna başlamak için bir Kahraman seiçiniz")
        print(seçim_ekrani)











