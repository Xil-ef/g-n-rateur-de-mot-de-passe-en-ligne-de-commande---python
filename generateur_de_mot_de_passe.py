import random
import string

def generer_mot_de_passe(longueur=12, inclure_majuscules=True, inclure_minuscules=True, inclure_nombres=True, inclure_symboles=True):
    """Génère un mot de passe aléatoire.

    Args:
        longueur (int): La longueur du mot de passe.
        inclure_majuscules (bool): Inclure des lettres majuscules.
        inclure_minuscules (bool): Inclure des lettres minuscules.
        inclure_nombres (bool): Inclure des nombres.
        inclure_symboles (bool): Inclure des symboles.

    Returns:
        str: Le mot de passe généré.
    """

    caracteres = ""
    if inclure_majuscules:
        caracteres += string.ascii_uppercase
    if inclure_minuscules:
        caracteres += string.ascii_lowercase
    if inclure_nombres:
        caracteres += string.digits
    if inclure_symboles:
        caracteres += string.punctuation

    if not caracteres:
        return "Veuillez sélectionner au moins un type de caractères."

    mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))
    return mot_de_passe

if __name__ == "__main__":
    longueur = int(input("Longueur du mot de passe (par défaut 12) : ") or 12)
    inclure_majuscules = input("Inclure majuscules ? (o/n, par défaut o) : ").lower() != 'n'
    inclure_minuscules = input("Inclure minuscules ? (o/n, par défaut o) : ").lower() != 'n'
    inclure_nombres = input("Inclure nombres ? (o/n, par défaut o) : ").lower() != 'n'
    inclure_symboles = input("Inclure symboles ? (o/n, par défaut o) : ").lower() != 'n'

    mot_de_passe = generer_mot_de_passe(longueur, inclure_majuscules, inclure_minuscules, inclure_nombres, inclure_symboles)
    print("Mot de passe généré :", mot_de_passe)
