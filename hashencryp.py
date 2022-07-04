import hashlib

print('''
 ____   _      _____  _     _    _   _  _____  _____  _   _    _   _  _____   ____  _   _ 
|  _ \ | |    |  _  |\ \   / /  | | | ||_   _||_   _|| | | |  | | | ||  _  | / ___|| | | |
| |_| || |    | | | | \ \_/ /   | |_| |  | |    | |  | | | |  | | | || | | || |__  | | | |
|  __/ | |    | |_| |  \   /    | / \ |  | |    | |  | |_| |  | |_| || |_| | \__ \ | |_| |
| |    | |    |  _  |   | |     |  _  |  | |    | |  |  _  |  |  _  ||  _  |    | ||  _  |
| |    | |___ | | | |   | |     | / \ | _| |_   | |  | | | |  | | | || | | | ___| || | | |
|_|    |_____||_| |_|   |_|     |/   \||_____|  |_|  |_| |_|  |_| |_||_| |_||____/ |_| |_|
                                                                       just play with Hash

01. Encrypted with md5
02. Encrypted with sha1
03. Encrypted with sha224
04. Encrypted with sha256
05. Encrypted with sha384
06. Encrypted with sha512
''')

select = int(input("Choose A Type::"))

if(select == 1):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.md5(text.encode())
    md5hash = hashobj.hexdigest()
    print("Your MD5 Hash is :",md5hash)

elif(select == 2):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.sha1(text.encode())
    sha1hash = hashobj.hexdigest()
    print("Your Sha1 Hash is :",sha1hash)

elif(select == 3):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.sha224(text.encode())
    sha224hash = hashobj.hexdigest()
    print("Your Sha224 Hash is :",sha224hash)

elif(select == 4):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.sha256(text.encode())
    sha256hash = hashobj.hexdigest()
    print("Your Sha256 Hash is :",sha256hash)

elif(select == 5):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.sha384(text.encode())
    sha384hash = hashobj.hexdigest()
    print("Your Sha384 Hash is :",sha384hash)

elif(select == 6):
    text = str(input("Enter your Message::")) 
    hashobj = hashlib.sha512(text.encode())
    sha512hash = hashobj.hexdigest()
    print("Your Sha512 Hash is :",sha512hash)

else:
    print("Invalid Error")

