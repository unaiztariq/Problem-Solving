letters = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def vigenere_cipher_encryption(letters,raw_text,keyword):
    def addcut_key(raw_text,key):
        if len(raw_text)== len(key):
            return key
        
        elif len(raw_text)< len(key):
            key = key[0:len(raw_text)]
    
        else:
            diff = len(raw_text)- len(key)
            if diff >= len(key):
                key= key+(diff//len(key)*key)+(key[0:diff%len(key)])
            else:
                key= key+key[0:diff]
        return key
        

    def logic_num(text,letters):
        key_points = []
        for t in text:
            for index,letter in enumerate(letters):
                if t== letter:
                    key_points.append(index)
                    break
        
        return key_points
    
    
    def enc_txt(raw_num,key_num):
        encrypt_num = []
        for i in range(0,len(raw_num)):
            temp = raw_num[i]+key_num[i]
            if raw_num[i]+key_num[i] >= len(letters):
                temp = raw_num[i]+key_num[i] - (len(letters)-1)
            
            if temp == key_num and raw_num!=0:
                temp = temp -25
                
            encrypt_num.append(temp)
            
        return encrypt_num


    def text_back(enc_num,letters):
        encrypt_text =""
        for i in enc_num:
            
            letter = letters[i]
            
            encrypt_text += letter
        return encrypt_text

    pure_key= addcut_key(raw_text,keyword)
    raw_num=  logic_num(raw_text,letters)      
    key_num=  logic_num(pure_key,letters)      
    enc_num = enc_txt(raw_num,key_num)
    return text_back(enc_num,letters)


def vigenere_cipher_decryption(letters,vig_text,keyword):
    
    def addcut_key(vig_text,key):
        if len(vig_text)== len(key):
            return key
        
        elif len(vig_text)< len(key):
            key = key[0:len(vig_text)]
    
        else:
            diff = len(vig_text)- len(key)
            if diff >= len(key):
                key= key+(diff//len(key)*key)+(key[0:diff%len(key)])
            else:
                key= key+key[0:diff]
        return key
    
    def logic_num(text,letters):
        key_points = []
        for t in text:
            for index,letter in enumerate(letters):
                if t== letter:
                    key_points.append(index)
                    break
        
        return key_points
    

    def enc_txt(raw_num,key_num):
        encrypt_num = []
        for i in range(0,len(raw_num)):
            temp = raw_num[i]-key_num[i]
            if raw_num[i]-key_num[i] < 0:
                temp = raw_num[i]-key_num[i] + (len(letters)-1)
            encrypt_num.append(temp)
        return encrypt_num
    
    def text_back(enc_num,letters):
        encrypt_text =""
        for i in enc_num:
            letter = letters[i]
            encrypt_text += letter
        return encrypt_text
    
    pure_key= addcut_key(vig_text,keyword)
    raw_num=  logic_num(vig_text,letters)      
    key_num=  logic_num(pure_key,letters)      
    enc_num = enc_txt(raw_num,key_num)
    return text_back(enc_num,letters)


raw_text = "hello"
keyword = "key"
vigenere_text = vigenere_cipher_encryption(letters,raw_text.lower(),keyword.lower())
print("Encrypted form:",vigenere_text)

vigenere_raw_text = vigenere_cipher_decryption(letters,vigenere_text.lower(),keyword.lower())
print("Decrypted form:",vigenere_raw_text)
