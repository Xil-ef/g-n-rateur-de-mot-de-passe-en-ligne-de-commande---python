# generateur-de-mot-de-passe-en-ligne-de-commande---python
Ce projet est un générateur de mots de passe en ligne de commande, écrit en Python. **Il génère des mots de passe sécurisés en utilisant des caractères aléatoires pour renforcer la sécurité de vos comptes en ligne.**

## Utilité
1- Générer des mots de passe robustes pour sécuriser vos comptes en ligne.
2- Faciliter la création de mots de passe complexes sans avoir à les inventer manuellement.
3- Outil pratique pour les développeurs et les administrateurs système.

## Installation
1. Assurez vous d'avoir installer python 3
2. Clonez ce depot git ```bash
    git clone (https://github.com/Xil-ef/generateur-de-mot-de-passe-en-ligne-de-commande---python)
    ```
3. Naviguez jusqu'au répertoire: ```bash
    cd generateur-de-mot-de-passe
    ```
4. Excecutez le script python: ```bash
    python generateur_de-mot-de-passe.py
    ```

## Utilisation

Le script vous demandera les informations suivantes :

* **Longueur du mot de passe (par défaut 12) :** Entrez la longueur souhaitée ou appuyez sur Entrée pour utiliser la valeur par défaut.
* **Inclure majuscules ? (o/n, par défaut o) :** Répondez 'o' (oui) ou 'n' (non).
* **Inclure minuscules ? (o/n, par défaut o) :** Répondez 'o' (oui) ou 'n' (non).
* **Inclure nombres ? (o/n, par défaut o) :** Répondez 'o' (oui) ou 'n' (non).
* **Inclure symboles ? (o/n, par défaut o) :** Répondez 'o' (oui) ou 'n' (non).

Le mot de passe généré sera affiché dans la console.

## Exemple
1. un mot de passe de 16 caractères avec tous les types de caractères :
![Mot de passe 16 carac](https://github.com/user-attachments/assets/dc43c6e9-03d6-473a-ab0b-e2dbf40c47d5)

   
2. un mot de passe de 8 caractères avec des lettres et des nombres :
![Mot de passe 8 caract](https://github.com/user-attachments/assets/87af4e51-03d1-4cba-b46b-644ed4ba126c)



## Dépendances

Ce projet utilise les modules standard de Python :

* `random`
* `string`

Aucune dépendance externe n'est requise.

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1.  Forkez ce dépôt.
2.  Créez une branche pour votre fonctionnalité ou correction de bug :

    ```bash
    git checkout -b ma-fonctionnalite
    ```

3.  Effectuez vos modifications et commitez-les :

    ```bash
    git commit -m "Ajout d'une nouvelle fonctionnalité"
    ```

4.  Poussez les modifications vers votre fork :

    ```bash
    git push origin ma-fonctionnalite
    ```

5.  Créez une pull request.

## Licence

Ce projet est sous licence [MIT](LICENSE).

## Auteur

* [Félix: Xil-ef](https://github.com/Xile-ef), veritaf.13@gmail.com

## Remerciements

* Merci à la communauté Python pour son soutien et ses ressources.
* Merci à tous les contributeurs qui ont aidé à améliorer ce projet.
