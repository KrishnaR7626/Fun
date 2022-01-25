# This is a Ceaser cipher decrypter
# It will take an encoded string and it will convert it into an array of integer values using a dictionary
# Then it shifts the values and recieves the keys from the dictionary.
# Which will decode the cipher

String = input("Enter original string to decrypt:\n")
String = String.lower()
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
              'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
dictionaryKeys = list(dictionary.keys())
valuesArray = []

for i in String:
    if i != " ":
        valuesArray.append(dictionary[i])
    else:
        valuesArray.append(" ")

for i in range(1,26):
    cipherarray = []
    for j in range(len(valuesArray)):
        if valuesArray[j]!= " ":
            cipherValue = valuesArray[j]+i
            if cipherValue>26:
                cipherValue%=26
        else:
            cipherValue = " "
        cipherarray.append((cipherValue))
    message = ""
    for j in cipherarray:
        if j != " ":
            message+=dictionaryKeys[j-1]
        else:
            message+=" "
    print(message)
    confirm = input("Is the message decrypted?\n")
    if confirm == "Y" or confirm == "y":
        break
