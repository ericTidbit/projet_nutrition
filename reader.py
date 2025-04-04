# codé par Julien



import csv


def dictionnaire_valeurs():
    pass



def reading(filename, nbr, v_nbr):

    """
    Prend un numero de ligne et retoure la ligne dans un fichier csv

    :param filename: le nom du file
    :param nbr: le numero de ligne du fichier
    :param v_nbr: le numero de l'element dans la ligne du fichier
    :return: la valeur de l'élément cherché
    """
    try:
        with open(filename, newline='', encoding="utf8") as csvfile: # ouvre le fichier
            reader = csv.reader(csvfile)

            for idx, ligne in enumerate(reader):
                if idx == nbr:
                    if 0 <= v_nbr < len(ligne): #validation
                        return ligne[v_nbr] #une valeur d'un element dans une ligne
                    else:
                        return "valeur introuvable"

    except FileNotFoundError:
        return "le fichier n'existe pas."




def affichage_tout(index_aliment):
    """
    prend le numero de ligne du fichier et reoure toutes les propriétés
    :param index_aliment:
    :return: str
    """
    print(reading("data.csv", index_aliment, 1),"\n")
    for charateriste in range(33):
        ligne = reading("data.csv", index_aliment, charateriste)
        if ligne == "" or ligne == "valeur introuvable" or ligne == 0 or ligne is None:
            pass
        else:
            print(f"{reading("data.csv",0, charateriste)}: {reading("data.csv", index_aliment, charateriste)}")





with open("data.csv", newline='', encoding="utf8") as csvfile: # ouvre le fichier
    reader = csv.reader(csvfile)
    for ligne in reader:
        print(f'"{ligne[1]}",')