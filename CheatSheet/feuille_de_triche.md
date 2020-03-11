Feuille de triche Python
=========================
Dernière mise à jour: 03/03/2020


# A ne pas oublier

1. l'indentation est signifiante:
```
  if (True):
      print ("Dans le if")
      print ("Toujours dans le if")
  print ("Pas dans le if")
```

2. Les chaînes peuvent être entre " ou '

3. On lance le programme depuis le terminal avec `python3 helloworld.py`

4. Les commentaires suivent un #


--------------------------------------------------------------------------------
# Structure
## If then else

Syntaxe générale:
```
  if (test):
    ...
    ...
  else:
    ...
    ...
```

## Boucle `for`

> Les boucles `for` sont en fait des *pour chaque éléments*.  Ils itérerent sur
> des structures.

1. Pour la boucle for classique, utiliser `range` (plus loin):
```
  for i in range(10):   # pour i dans [0,1,...9]
    print (i)
```

2. Itérer sur une liste
```
  for element in ["Victor", "Nadime"]:
    print (element)
```

3. Itérer sur une chaîne de caractère
```
  for c in "Hello World!"       #affiche une lettre par ligne, donc 12 en tout
    print(c);
```



--------------------------------------------------------------------------------
