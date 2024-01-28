print("""
                                                                 ##
                                                                 ##
 ##  ##   ##  ##   ######    #####   ##  ##   ######             ##       ####     #####    ####    ######
 ##  ##   ##  ##   #  ##    ##       ##  ##   #  ##              #####   ##  ##   ##           ##    ##  ##
 ##  ##   ##  ##     ##      #####   ##  ##     ##               ##  ##  ######    #####    #####    ##  ##
  #####   ##  ##    ##  #        ##  ##  ##    ##  #             ##  ##  ##            ##  ##  ##    #####
     ##    ######  ######   ######     ###    ######             ##  ##   #####   ######    #####    ##
 #####                                                                                               ##
""")
print(f"@ixnur - Yuzsuz Hesap Makinesi")
print(f"Yazılım: Python")
print(f"--------------------------------")
import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölen sıfır olamaz!"

def karekok(x):
    return math.sqrt(x)

def us_alma(x, y):
    return math.pow(x, y)

def mod_alma(x, y):
    return x % y

def faktoriyel(x):
    return math.factorial(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def logaritma(x):
    base = input("taban seçin :")
    return math.log(x, int(base))

def mutlak_deger(x):
    return abs(x)

def kupkok(x):
    return math.pow(x, 1/3)
    
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Karekök")
print("6. Üs Alma")
print("7. Mod Alma")
print("8. Faktöriyel")
print("9. Sinüs")
print("10. Kosinüs")
print("11. Tanjant")
print("12. Logaritma")
print("13. Mutlak Değer")
print("14. Küpkök")
print("Q. Çıkış")
operator = {"1": (toplama, 2),
            "2": (cikarma, 2),
            "3": (carpma, 2),
            "4": (bolme, 2),
            "5": (karekok, 1),
            "6": (us_alma, 2),
            "7": (mod_alma, 2),
            "8": (faktoriyel, 1),
            "9": (sin, 1),
            "10": (cos, 1),
            "11": (tan, 1),
            "12": (logaritma, 1),
            "13": (mutlak_deger, 1),
            "14": (kupkok, 1),
            "Q": (exit, 1)}
while True:
    secim = input("Yapmak istediğiniz işlemi seçin (1-14): ")

    if secim.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    if secim in ('1', '2', '3', '4', '7', '8', '9', '10', '11', '12', '13', '14'):
        print(f"seçilen işlem : {operator.get(secim, None)[0].__name__}")
        x = float(input("Birinci sayıyı girin: "))
    else:
        x = int(input("Birinci sayıyı girin: "))

    op = operator.get(secim, None)  # hashmap den fonksiyon ve kaç paramtre değerini tuple şeklinde al
    if op:
        param = op[-1]  # parametre sayı(1,2) değerini al
        func = op[0]  # fonskiyonu al
        if param == 2:  # fonksiyon x ve y den oluşuyorsa
            if secim not in ('5', '15'):
                y = float(input("İkinci sayıyı girin: "))  # y yi al
                print("Sonuç : ", func(x, y))
        elif param == 1: # sonuç tek parametreli ise x al
            print("Sonuç : ", func(x))
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        # op
    # if secim == '1':
    #     print("Sonuç: ", toplama(x, y))
    # elif secim == '2':
    #     print("Sonuç: ", cikarma(x, y))
    # elif secim == '3':
    #     print("Sonuç: ", carpma(x, y))
    # elif secim == '4':
    #     print("Sonuç: ", bolme(x, y))
    # elif secim == '5':
    #     print("Sonuç: ", karekok(x))
    # elif secim == '6':
    #     print("Sonuç: ", us_alma(x, y))
    # elif secim == '7':
    #     print("Sonuç: ", mod_alma(x, y))
    # elif secim == '8':
    #     print("Sonuç: ", faktoriyel(x))
    # elif secim == '9':
    #     print("Sonuç: ", sin(x))
    # elif secim == '10':
    #     print("Sonuç: ", cos(x))
    # elif secim == '11':
    #     print("Sonuç: ", tan(x))
    # elif secim == '12':
    #     print("Sonuç: ", logaritma(x))
    # elif secim == '13':
    #     print("Sonuç: ", mutlak_deger(x))
    # elif secim == '14':
    #     print("Sonuç: ", kupkok(x))
    # else:
    #     print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
