# codé par Julien



import csv


def reading(filename, nbr, v_nbr):

    """
    Prend un numero de ligne et retoure la ligne dans un fichier csv

    :param filename: le nom du file
    :param nbr: le numero de ligne du fichier
    :param v_nbr: le numero de l'element dans la ligne du fichier
    :return: la valeur de l'élément cherché
    """
    try:
        with open(filename, newline='', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)

            for idx, ligne in enumerate(reader):
                if idx == nbr:
                    if 0 <= v_nbr < len(ligne):
                        return ligne[v_nbr], ligne
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
    truc = reading("data.csv", index_aliment, 1)

    print(f"{truc[0]}")

affichage_tout(1)