import hashlib

print('''
 ____   _      _____  _     _    _   _  _____  _____  _   _    _   _  _____   ____  _   _ 
|  _ \ | |    |  _  |\ \   / /  | | | ||_   _||_   _|| | | |  | | | ||  _  | / ___|| | | |
| |_| || |    | | | | \ \_/ /   | |_| |  | |    | |  | | | |  | | | || | | || |__  | | | |
|  __/ | |    | |_| |  \   /    | / \ |  | |    | |  | |_| |  | |_| || |_| | \__ \ | |_| |
| |    | |    |  _  |   | |     |  _  |  | |    | |  |  _  |  |  _  ||  _  |    | ||  _  |
| |    | |___ | | | |   | |     | / \ | _| |_   | |  | | | |  | | | || | | | ___| || | | |
|_|    |_____||_| |_|   |_|     |/   \||_____|  |_|  |_| |_|  |_| |_||_| |_||____/ |_| |_|
                                                                     Decrypted Hash Format
01. Decode With MD5
02. Decode With SHA 1
03. Decode With SHA 224 
04. Decode With SHA 256 
05. Decode With SHA 384 
06. Decode With SHA 512

''')

select = int(input("Choose A Option :"))

if(select==1): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password in passfile:
            encPass = password.encode("utf-8")
            digest = hashlib.md5(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password)
           
    if __name__ == "__main__":
        hash(hashcode)


elif(select==2): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password1 in passfile:
            encPass = password1.encode("utf-8")
            digest = hashlib.sha1(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password1)
           
    if __name__ == "__main__":
        hash(hashcode)

elif(select==3): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password in passfile:
            encPass = password.encode("utf-8")
            digest = hashlib.sha224(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password)
           
    if __name__ == "__main__":
        hash(hashcode)


elif(select==4): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password in passfile:
            encPass = password.encode("utf-8")
            digest = hashlib.sha256(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password)
           
    if __name__ == "__main__":
        hash(hashcode)



elif(select==5): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password in passfile:
            encPass = password.encode("utf-8")
            digest = hashlib.sha384(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password)
           
    if __name__ == "__main__":
        hash(hashcode)


elif(select==6): 
    hashcode = str(input("Enter your hash::"))
    filepath = str(input("Enter the File Path :"))

    def hash(inputhash):

        try:
            passfile = open(filepath, "r")  
        except:
            print("Could not Find File.")


        for password in passfile:
            encPass = password.encode("utf-8")
            digest = hashlib.sha512(encPass.strip()).hexdigest()
            if digest == inputhash:
                print("Password Found :",password)
           
    if __name__ == "__main__":
        hash(hashcode)

else:
    print("Invalid Error")