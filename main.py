import klasa

kolejka = klasa.Fifo()
print("\nFIFO:")
for i in range(6):
    kolejka.put("asd" + str(i))  # pobierz do kolejki
for i in range(6):
    print(kolejka.get())  # Wyciągnij z kolejki

del kolejka

kolejka = klasa.Lifo()
print("\nLIFO:")
for i in range(6):
    kolejka.put("asd" + str(i))
for i in range(8):
    print(kolejka.get())
