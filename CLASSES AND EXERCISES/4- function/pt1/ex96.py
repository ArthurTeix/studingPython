# area de terreno retangular
def linha():
    print("-=-"*10)

def area(a,b):
    mult = a*b
    print(f"A aréa de um terreno {a} x {b} é de {mult:.1f}m²")

linha()
print("     Controle de Terrenos")
linha()

area(float(input("Largura (m): ")), float(input("Comprimento (m): ")))