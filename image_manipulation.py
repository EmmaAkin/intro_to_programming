import base64

def file_encode(filename):

    original = open(filename, "rb")


    base64_version = open("backups/"+original+".bak", "wb")
    base64.encode(original, base64_version)

    original.close()
    base64_version.close()

def file_decode(filename):

    encoded = open(filename, "rb")


    base64_version = open("backups/"+encoded+".bak", "wb")
    base64.decode(encoded, base64_version)





file_encode("myMum.jpg")
