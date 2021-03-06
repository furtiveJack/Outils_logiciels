# Les fichiers

## Ouverture

Ouverture d'un fichier :

```python
file = open("path", "r")
```

### Modes d'ouverture

* `r` : lecture
* `w` : écriture (fichier créé s'il n'existe pas, tronqué s'il existe)
* `a` : append

Rajouter un `+` au mode permet de créer le fichier s'il n'existe pas


### Types d'ouverture

Rajouter au mode un :

- `t` permet d'indiquer que l'on manipule du texte

- `b` permet d'indiquer que l'on manipule des bits

## Fermeture

__IMPORTANT__ : Penser à fermer le fichier:

`file.close()`

Ou alors, fermeture automatique avec la syntaxe :

```python
with open("path", "r") as file:
    # Iterer sur le fichier
```

## Itération

```python
import sys
file = open("test.txt", "w")            # On ouvre le fichier "test.txt" en écriture
for x in [2**i for i in range(11)]:     # On écrit quelquechose dedans
  file.write(str(x)+"\n")
file.close()                            # Puis, on ferme le fichier
file = open("test.txt","r")             # Et on le réouvre en lecture
for line in file:                       # Pour chaque ligne dans `file`
  print (line, end='')                  # la clause `end=''` indique de ne pas revenir à
                                        # ligne à la fin.
                                        # En effet, chaque ligne termine déjà par un `\n`
```


## Changement d'extension

```python
import os
absolutePath = "file.txt"
base = os.path.splitext(absolutePath)[0]
os.rename(absolutePath, base + ".py")
```
