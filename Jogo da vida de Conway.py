#Jogo da Vida de Conway
from random import random
import turtle as t
 
def nova_mat(altura,largura,prob):
    mat = []
    for a in range(altura):
        mat.append([False]*largura)
 
    if prob > 0:
        for a in range(altura):
            for l in range(largura):
                mat[a][l] = random() < prob
 
    return mat
 
def des_mat(mat):
    tam_cel = 10
    dif_h = largura / 2 * tam_cel
    dif_v = altura / 2 * tam_cel
    t.tracer(0)
    t.pu()
    for a in range(altura):
        for l in range(largura):
            t.goto(l*tam_cel - dif_h,
                   a*tam_cel - dif_v)
            if mat[a][l] : t.dot(tam_cel-1)
    t.update()
 
def simula(mat):
    nova = nova_mat(altura, largura, 0)
    for a in range(altura):
        for l in range(largura):
            aa = a - 1
            ap = (a + 1) % altura
            la = l - 1
            lp = (l + 1) % largura
            soma = (mat[a][la] + mat[a][lp] +
                    mat[aa][l] + mat[ap][l] +
                    mat[aa][la] + mat[ap][lp] +
                    mat[aa][lp] + mat[ap][la])
            if mat[a][l]:
                if soma < 2: nova[a][l] = False
                elif soma > 3: nova[a][l] = False
                else: nova[a][l] = True
            else:
                if soma == 3 : nova[a][l] = True
    return nova
 
def atualiza():
    global mat
    t.reset()
    des_mat(mat)
    mat = simula(mat)
    t.ontimer(atualiza,10)
 
 
altura = 60
largura = 100
mat = nova_mat(altura,largura,0.5)
atualiza()
t.mainloop()