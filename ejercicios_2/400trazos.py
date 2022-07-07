from turtle import forward, right, speed



from turtle import*

speed(0)
x = 1
while x < 400:
    forward(5+x)
    right(350)
    #cambiando el valor de right obtenemos diferentes figuras, por ejemplo:
    #right(50) nos daria un especie de hexagono
    #right(180) nos daria una estrela
    #right(120) nos daria una triangulo
    #ir aumentando o disminuyendo según se desee
    x+=1
    
mainloop()