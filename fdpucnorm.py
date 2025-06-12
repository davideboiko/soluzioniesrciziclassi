import re

def frequenza(text: str) -> dict:
    
    bo:dict = {}

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    for i in words:

        if i in bo:
            bo[i] += 1

        else:
            bo[i] = 1

    return bo
        

print(frequenza("ciao!, COME, stai?, stai stAi"))
