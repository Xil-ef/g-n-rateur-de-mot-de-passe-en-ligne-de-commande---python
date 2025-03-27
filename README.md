# generateur-de-mot-de-passe-en-ligne-de-commande---python
un générateur de mot de passe qui demande la longueur du mot de passe, l'inclusion ou non de Majucule, de minuscule, de chiffre et de symbole

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
