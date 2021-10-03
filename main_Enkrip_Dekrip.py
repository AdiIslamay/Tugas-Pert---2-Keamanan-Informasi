# Program Kriptografi Untuk Enkripsi dan Deskripsi
# By Adi Islamay V M

def header():
    print("WELCOME TO PROGRAM ENKRIPSI DAN DESKRIPSI")
    print("=========================================")


def menu_kripto():
    while True:
        print()
        print("======================================")
        print("    MARI BERMAIN KRIPTOGRAFI  ")
        print("======================================")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print()

        input_menu_kripto = int(
            input("Silahkan Pilih Menu, contoh [1] ? "))
        if input_menu_kripto == 1:
            hasil_enkripsi = enkripsi()
            print()
            print("Hasil enkripsi: " + hasil_enkripsi)
        elif input_menu_kripto == 2:
            dekripsi()
            print()


def enkripsi():
    text_input = str(
        input("Silahkan Masukkan Text yang akan di enkrpsi, contoh [aku mencoba] ? "))
    key_input = int(
        input("Masukan key yang akan anda pakai, ex [number] ? "))
    result = ""

    for i in range(len(text_input)):
        char = text_input[i]

        if char.isupper():
            result += chr((ord(char) + key_input - 65) % 26 + 65)

        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + key_input - 97) % 26 + 97)

    return result


def dekripsi():
    Abjad = "abcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(
        input("Silahkan Masukkan Pesan yang akan di dekripsi, ex [gqa ygegtm jog] ?"))

    for key in range(len(Abjad)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in Abjad:
                num = Abjad.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(Abjad)
                translated = translated + Abjad[num]
            else:
                translated = translated + symbol
            print('Hacking key #%s: %s' % (key, translated))


def main():
    header()
    menu_kripto()


if __name__ == '__main__':
    main()
