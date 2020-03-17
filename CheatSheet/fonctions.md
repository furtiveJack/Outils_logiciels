# Les fonctions

Syntaxe générale :
```
  def function():
      return
```

On peut renvoyer des tuples :
```
  def tuples(a, b):
      return a, b
```

Condition ternaire :

```
    def min(a, b):
        return a if (a < b) else b
```

## Documentation de fonctions

```
def function(param1: type1, param2: type2) -> return_type

# Exemple:
def is_greater(a: int, b: int) -> bool
```