"""
# count_chars.py

frase = input("Escreva a frase: ")

dicionario = {}

for letra in frase:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1
print(dicionario)
"""
# char_intersection.py

frase1 = input("Escreva a primeira frase: ")
frase2 = input("Escreva a segunda frase: ")

palavras1 = frase1.split()
palavras2 = frase2.split()

set1 = set(palavras1)
set2 = set(palavras2)

intersecao = []
for palavra in set1:
    if palavra in set2:
        intersecao.append(palavra)

alfabeticamente = sorted(intersecao)

if "?" in alfabeticamente:
    alfabeticamente.remove("?")
    alfabeticamente.append("?")

print(frase1)
print(frase2)
print(" ".join(alfabeticamente))
