fio = "Ivanou Ivan"

words = fio.split()
words[0], words[1] = words[1], words[0]

print(" ".join(words))