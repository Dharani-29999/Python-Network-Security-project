import hashlib;

def Text_MD5(Text):
    hash_text=hashlib.md5(Text.encode())
    hash_convert=hash_text.hexdigest()
    print(hash_convert)
Text="Hello World"
Text_MD5(Text)
