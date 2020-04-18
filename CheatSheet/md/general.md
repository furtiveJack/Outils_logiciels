# Généralités

# A ne pas oublier

* l'indentation est signifiante:
```
  if (True):
      print ("Dans le if")
      print ("Toujours dans le if")
  print ("Pas dans le if")
```

* Les chaînes peuvent être entre " ou '

* On lance le programme depuis le terminal avec `python3 helloworld.py`

* Les commentaires suivent un #


--------------------------------------------------------------------------------
# Structure
## If ... elif ... else

Syntaxe générale:
```python
  if (test):
    ...
    ...
  elif (test):
    ...
    ...
  else:
    ...
    ...
```

## Boucle `for`

> Les boucles `for` sont en fait des *pour chaque éléments*.  Ils itérerent sur
> des structures.

* Pour la boucle for classique, utiliser `range` (voir [Listes](listes.md#la-fonction-range)):
```python
  for i in range(10):   # pour i dans [0,1,...9]
    print (i)
```

* Itérer sur une liste
```python
  for element in ["Victor", "Nadime"]:
    print (element)
```

* Itérer sur une chaîne de caractère
```python
  for c in "Hello World!"       #affiche une lettre par ligne, donc 12 en tout
    print(c);
```



--------------------------------------------------------------------------------

## Accéder aux arguments d'un programme

```
import sys

print(sys.argv)
```
* Renvoit la liste des arguments
* Le premier élément est le nom du programme