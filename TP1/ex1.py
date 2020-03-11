from upemtk import *


def fibonacci1(n):
    print(n)
    if n <= 1:
        return n
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


def fibonacci2(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci2(n - 1)
        (c, d) = fibonacci2(n - 2)
        return (a + c, b + d + 1)


def fibonacci3(n):
    if n == 1:
        return (0, 1)
    (a, b) = fibonacci3(n - 1)
    return (b, a + b)


def fibonacci4(n):
    if n == 1:
        return ((0, 1), 1)
    ((a, b), c) = fibonacci4(n - 1)
    return ((b, a + b), c + 1)


fibonacci5_memory = [-1 for _ in range(0, 30)]


def fibonacci5(n):
    value = fibonacci5_memory[n]
    if value != -1:
        return value
    else:
        fibonacci5_memory[n] = fibonacci1(n)
        return fibonacci5_memory[n]


def g(n):
    return (n, n)


def h(n):
    return (n, n ** 2)


def i(n):
    return (n, 2 ** n)


print(fibonacci2(6))
print(fibonacci3(6))
print(fibonacci4(6))
print(fibonacci5(6))
# for i in range(10, 50, 10):
# 	print(fibonacci1(i))

HEIGHT = 900
WIDTH = 900
SCALE_X = 20
SCALE_Y = 0.1
cree_fenetre(HEIGHT, WIDTH)


def display_scale(step):
    for i in range(step, HEIGHT, step):
        ligne(0, i, 5, i, couleur='black')
    for i in range(step, WIDTH, step):
        ligne(i, WIDTH, i, WIDTH - 5, couleur='black')


def display_fibo():
    display_function([(n, fibonacci2(n)[1]) for n in range(20)], "red")


def display_quick_fibo():
    display_function([(n, fibonacci4(n)[1]) for n in range(20)], "purple")


def display_g_n():
    display_function([(n, g(n)[1]) for n in range(20)], 'green')


def display_h_n():
    display_function([(n, h(n)[1]) for n in range(20)], 'blue')


def display_i_n():
    display_function([(n, i(n)[1]) for n in range(20)], 'yellow')


def display_function(func_values, color):
    prev = (0, 0)
    for val in func_values:
        ligne(prev[0] * SCALE_X, HEIGHT - (prev[1] * SCALE_Y), val[0] * SCALE_X, HEIGHT - (val[1] * SCALE_Y),
              couleur=color, epaisseur=2)
        cercle(val[0] * SCALE_X, HEIGHT - (val[1] * SCALE_Y), 4, couleur='black', remplissage='black')
        prev = val


# display_scale(SCALE)
display_fibo()
display_g_n()
display_h_n()
display_i_n()
display_quick_fibo()
mise_a_jour()
attente_clic()

ferme_fenetre()

'''
Liste des valeurs de prises par n pour calculer fibonacci1(4):
4
3
2
1
0
1
2
1
0
3

La fonction est lente car on recalcule plusieurs fois les memes
valeurs de fibonacci1, ce qui n'est pas efficace

'''
