def enkripsi(teks,s):
    hasil = ""
 
    for i in range(len(teks)):
        char = teks[i]
 
        if (char.isupper()):
            hasil += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            hasil += chr((ord(char) + s - 97) % 26 + 97)
 
    return hasil
 
teks = "Muhammad Imaduddin Mustofa"
s = 65
print ("teks  : " + teks)
print ("Shift : " + str(s))
print ("Cipher: " + enkripsi(teks,s))
