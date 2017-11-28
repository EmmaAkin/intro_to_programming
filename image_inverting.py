import base64

def file_encode(filename):

    original = open(filename, "rb")


    text = original.readline()
    print(text)
    print("Here we are")



    #base64_version = open("backups/"+filename+".bak", "wb")
    #base64.encode(original, base64_version)

    #original.close()
    #base64_version.close()

def file_decode(filename):

    encoded = open(filename, "rb")


    base64_version = open(filename+".bak", "wb")
    base64.decode(encoded, base64_version)

    encoded.close()
    base64_version.close()


print(file_encode("file.txt"))

#file_decode("backups/myMum.jpg.bak")
