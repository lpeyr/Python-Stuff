nb: dict = {0: "zéro", 1: "un", 2: "deux",
            3: "trois", 4: "quatre", 5: "cinq", 6: "six",
            7: "sept", 8: "huit", 9: "neuf"}  # dictionnaire pour transformer


def transformer(texte: str) -> str:
    """
    Description:
        Transforme les chiffres présents dans une chaîne de caractère (ex: 1, 2, 3...) en lettre (ex: un, deux, trois...).

    Argument:
        texte (str): Le texte à transformer.

    Renvoie:
        str: La chaîne de caractère sans chiffres, uniquement avec les nombres écris en lettre.
    """
    final: str = ""  # texte final
    for lettre in texte:  # pour chaque lettre
        if est_nbr(lettre):  # si la lettre est un nombre, alors on transforme le chiffre en lettre
            final += nb[int(lettre)]
        else:  # si la lettre n'est pas un nombre, on ajoute cette lettre à la chaîne finale.
            final += lettre
    return final  # Renvoie le texte transformée


def est_nbr(lettre: str) -> bool:
    """
    Description
        Vérifie si un caractère est un chiffre contenu (en tant que clé) dans le dictionnaire nb.

    Argument:
        lettre (str): La lettre à vérifier.

    Renvoie:
        bool: True si la lettre est un chiffre, False si la lettre n'est pas un chiffre.
    """
    return lettre in [str(c) for c in nb]  # obtient un tableau contenant les clés du dictionnaire nb sous forme de chaîne de caractère (1 devient "1") et vérifie si la lettre en question est à l'intérieur


# Tests
print(transformer("j'ai 3 pommes, 4 poires, 8 tomates"))
# Résultat : j'ai trois pommes, quatre poires, huit tomates
