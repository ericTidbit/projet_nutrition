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
    with open(filename, newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)

        r_ligne = [ligne for idx, ligne in enumerate(reader)if idx == nbr] #ch3ka sur stackoverflow https://stackoverflow.com/questions/26464567/csv-read-specific-row
        r_val = [valeur for idx, valeur in enumerate(r_ligne)if idx == v_nbr]

    return r_val

print(reading("data.csv", 2, 5))