#   Exercicio media

N1 = float(input(" Qual a nota no primeiro bimestre?"))
N2 = float(input(" Qual a nota no segundo bimestre?"))
N3 = float(input(" Qual a nota no terceiro bimestre?"))
N4 = float(input(" Qual a nota no quarto bimestre?"))

Media = (N1+N2+N3+N4)/4
print(f" A media é {Media}")
if Media >= 6:
  print(f"O aluno foi aprovado")
else:
 print(f"O aluno não foi aprovado ")