woordenboek = {
    'hond': 'dog',
    'kat': 'cat',
    'huis': 'house',
    'boom': 'tree',
    'auto': 'car'
}

te_zoeken_woord = input("Voer een woord in om de Engelse vertaling te weten: ")

if te_zoeken_woord in woordenboek:
	print(f"De vertaling van {te_zoeken_woord} is {woordenboek[te_zoeken_woord]}.")
else:
	print("Dat woord staat niet in ons woordenboek.")