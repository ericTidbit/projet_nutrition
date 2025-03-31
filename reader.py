import csv


def reading(filename, itemname, nutriment_cherche):
    """

    :param filename: le nom du file
    :param itemname:
    :return: la valeur de l'élément cherché
    """
    with open(filename, newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            element = {}
            print(row)


reading("data.csv", "banane", "Énergie (kcal)")