import math

# Funções trigonométricas: seno, cosseno e tangente (ângulos em RADIANOS, não em graus)
print("Sen(pi2) =", math.sin(math.pi / 2)) 
print("Cos(0) =", math.cos(0))           
print("Tg(pi/4) =", math.tan(math.pi / 4))

# math.radians(graus) / math.degrees(radianos): conversão entre graus e radianos
print("180° em rad:", math.radians(180))     
print("pi em grau:", math.degrees(math.pi))

# math.hypot(x, y): calcula a hipotenusa (distância euclidiana) entre dois pontos, equivalente a sqrt(x**2 + y**2)
print("Hipotenusa (catetos de 3 e 4):", math.hypot(3, 4)) 