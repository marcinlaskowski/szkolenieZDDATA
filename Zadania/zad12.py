"""12. Napisy. Utwórz zmienną title zawierającą zdanie:
"Przepis na muffinki czekoladowe".
Wyświetl pierwszą literę zdania
Wyświetl znak o indeksie 5
Wyświetl znak o indeksie -2
Wyświetl słowo "muffinki"
 (podpowiedz użyj przedziału, dla słowa "Przepis" - title[:7]
Policz znaki w napisie
Wyświetl podany napis
 (modyfikacja - cały skladajacy się z dużych liter)
"""

sentence = "Przepis na muffinki czekoladowe"

# Wyświetl pierwszą literę zdania
print(sentence[0])

# Wyświetl znak o indeksie 5
print(sentence[5])

# Wyświetl znak o indeksie -2
print(sentence[-2])

# Wyświetl słowo "muffinki"
#  (podpowiedz użyj przedziału, dla słowa "Przepis" - title[:7]
print(sentence[11:19])

# LUB
splited_sentence = sentence.split()
print(splited_sentence[2])

# LUB
print(sentence.split()[2])

# Policz znaki w napisie
print(len(sentence))
# Wyświetl podany napis (modyfikacja - cały skladajacy się z dużych liter)
print(sentence.upper())
