ingredientes=""

tipo = int(input("Tipo de Hambuerguesa: \n Clasica 1 / Vegana 2 : "))

if tipo == 1:
    input("Ingredientes: /n Queso Idiazabal 1 \t Bacon 2 \t Huevo 3 : ")
elif tipo == 2:
    input("Ingredientes: /n Tofu 1 \t Cebolla caramelizada 2: ")
else:
    input("No Extras")