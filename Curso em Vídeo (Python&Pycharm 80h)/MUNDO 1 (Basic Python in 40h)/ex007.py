metros = float(input('Digite o comprimento do objeto em METROS: '))

cm = float(metros*100)
mm = float(metros*1000)

print(f'Boa! Vamos converter {metros}m para Centímetros e Milímetros!')
print(f'Em centímetros este objeto mede {cm:.1f}cm!')
print(f'Em milímetros este objeto mede {mm:.0f}mm!')
