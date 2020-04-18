# Les fonctions

# Syntaxe

> Syntaxe générale :
```python
  def function():
      return
```

> On peut renvoyer des tuples :
```python
  def tuples(a, b):
      return a, b
```

> Condition ternaire :

```python
    def min(a, b):
        return a if (a < b) else b
```

# Arguments optionnels

> Si l'on spécifie une valeur "par défaut" à l'un des arguments, alors celui-ci devient
optionnel : s'il n'est pas spécifié, il prendra la valeur par défaut.

```python
def func(a, b, optional="rien"):
    print(a + ' ' + b + optional)

func(5, 2, "coucou")        # affiche : 5 2 coucou
func(5, 2)                  # affiche : 5 2 rien
```



# Documentation de fonctions

```python
def function(param1: type1, param2: type2) -> return_type

# Exemple:
def is_greater(a: int, b: int) -> bool:
```