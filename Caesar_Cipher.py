n = input() # without spaces
a = "abcdefghijklmnopqrstuvwxyz" 
alpha = list(a)
alpha_dict = {}
for i,j in enumerate(alpha):
    alpha_dict[j] = i



def encrypt(str, n):
    str = list(str)
    
    for i in range(0,len(str)):
        num = (alpha_dict[str[i]]+3) % 26
        for j,k in alpha_dict.items():
            if num == k:
                str[i] = j
    return "".join(str)

def decrypt(str, n):
    str = list(str)
    
    for i in range(0,len(str)):
        num = (alpha_dict[str[i]]-3) % 26
        for j,k in alpha_dict.items():
            if num == k:
                str[i] = j
    return "".join(str)

print(encrypt(n,3))
en = encrypt(n,3)
print(decrypt(en,3))
