# Les dictionnaires

## Généralités

* Dictionnaire = Ensemble de clés/valeurs

## Déclaration

* Créer un dictionnaire vide

```python
dict = {}
```

* Créer un dictionnaire prérempli

```python
dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
```

## Accès

* Récupérer la valeur d'une clé: on utilise les [].

```python
age = dict['Tiffany']
print(age)
# affiche 22
```

* Vérifier la présence d'une clé: on utilise 'in'.
```python
key = 'Tim'
if key in dict:
    print('Valeur trouvée dans le dictionnaire pour la clé', key)
else:
    # Si la clé n'existe pas, une KeyError est levée
```

Pour éviter la KeyError quand on essaie d'accéder à une clé du dictionnaire, 
on peut utiliser la méthode get(). Celle-ci renvoit None si la clé n'existe pas.

```python
dict.get("Tim") # Renvoit 18
dict.get("Elepĥant") # Renvoit None
```

On peut ajouter une valeur de retour par défaut à la méthode get(), utilisée dans le cas
où la clé n'aurait pas été trouvée.

```python
dict.get("Elephant", 3) # Renvoit 3
```

## Ajout

Deux méthodes à notre disposition pour ajouter: 

* on peut utiliser _setdefault()_ qui insère la valeur donnée dans le cas où la clé
n'est pas présente dans le dictionnaire (si elle y est, sa valeur n'est pas modifiée).

```python
dict.setdefault('Elephant', 15) # dict contient maintenant un élément 'Elephant':15
dict.setdefault('Elephant', 18) # la valeur associée a Elephant est toujours 15
```

* Sinon on peut utiliser la méthode update (ca marche aussi avec des []):
```python
dict.update({'Jerry': 8}) # Ajoute la clé/valeur Jerry:8 dans le dictionnaire
# Ou alors
dict['Jerry'] = 8 # Meme effet
```

## Suppression

On utilise la méthode del pour supprimer une clé et sa valeur du dictionnaire :
```python
del dict['Elephant']
```

## Itérer sur les clés

On peut récupérer toutes les clés d'un dictionnaire sous forme d'un itérable.
On a pas de garantie sur l'ordre.

```python
list(dict.keys())      # ['Tim', 'Tiffany', 'Charlie', 'Jerry', 'Robert']
```

## Itérer sur les valeurs

On peut également obtenir toutes les valeurs d'un dictionnaire sous forme d'un itérable.
```python
list(dict.values()) # [18, 22, 12, 8, 25]
```