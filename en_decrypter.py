import os

#Read_file reads the file and return a text
def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close
    return text

#Function write a file
def write_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()

#Help create a backups folder in your system if you dont have one
if not os.path.exists("backups"):
    os.makedirs("backups")

#Take a file and save it in a backup folder
def backup(filename):
    text = read_file(filename)
    write_file("backups/"+filename+".bak", text)

#Function that encrypt the text accroding to the key given, and return ciphertext
def encrypt_algo(text, key):
    text_encrypt = ""
    for c in text:
        #With the modulus % the user can enter any number of keys.
        text_encrypt = text_encrypt+str((ord(c)+(key%256))) + " "

    return text_encrypt

#Function that decrypt the ciphertext given, according to the key and return text
def decrypt_algo(text, key):
    text = text.split()
    text_decrypt = ""
    for c in text:
        text_decrypt = text_decrypt+chr((int(c)-(key%256)))
    return text_decrypt

def encrypt_decrypt(filename, key=8, choice="encrypt"):
    # Get the content of file and return text
    text = read_file(filename)

    if choice == "encrypt":
        #Create a backup of the original file in a same location
        backup(filename)

        # Encrypt the file accrording to the key given ( You can encrypt a number of times but
        #make sure that the number correspond for the decrytion)
        new_text = encrypt_algo(text,key)
        new_text = encrypt_algo(new_text, key)
    else:
        #Decrypt the file with the given key
        new_text = decrypt_algo(text, key)
        new_text = decrypt_algo(new_text,key)


    #Write the encrypted file to the original file
    write_file(filename, new_text)

if __name__ == '__main__':
    encrypt_decrypt("file.txt",7,"decrypt")