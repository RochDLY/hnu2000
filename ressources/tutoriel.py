import re
from collections import Counter


# Apprendre à utiliser les variables et les fonctions
## Définir la fonction

def separer_en_mots(un_morceau_de_texte):
    bas_de_casse = un_morceau_de_texte.lower()
    separer_mots = re.split("\W", bas_de_casse)
    return separer_mots

## Définir le chemins du texte et affecter une valeur à une variable

chemin_du_texte = "ressources/dracula.txt"
nombre_de_mots_souhaite = 40

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers','herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 've', 'll', 'amp', '', 'gutenberg', 'project', '_', 'us', 'could', '1']

## Lire le fichier

texte_entier = open(chemin_du_texte, encoding="utf-8").read()

## Manipuler et analyser le fichier

tous_les_mots = separer_en_mots(texte_entier)
mots_significatifs = [mot for mot in tous_les_mots if mot not in stopwords]
compter_mots_significatifs = Counter(mots_significatifs)
mots_significatifs_plus_frequent = compter_mots_significatifs.most_common(nombre_de_mots_souhaite)

## Afficher le résultat

print(mots_significatifs_plus_frequent)

''' 
Attention ! La valeur affectée à une variable peut être réattribuée ! 
Un script est exécuté de haut en bas : si j'affecte une valeur à une variable à la ligne 1,
et que j'en affecte une autre à la ligne 50, nous pourrons travailler avec la première valeur
de la ligne 2 à 49 et avec la deuxième après la ligne 50.

Les variables peuvent contenir : 
- des lettres majuscules ou minuscules (A-Z)
- des chiffres (de 0 à 9)
- des tirets du bas (_)

Les variables ne peuvent pas contenir : 
- des ponctuations (.?!-@)
- des espaces ( )
- des mots réservés à Python (print, True, etc...)
'''










