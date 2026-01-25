#6) Afișează toate culorile din primul set care nu sunt în al doilea set.


set1 = {'roșu', 'albastru', 'verde', 'galben', 'mov'}
set2 = {'portocaliu', 'verde', 'roz', 'albastru'}
culori_diferite = set1.difference(set2)
print("Culorile din set1 care nu sunt în set2 sunt:", culori_diferite)

#sau
#culori_diferite = set1 - set2
#print("Culorile din set1 care nu sunt în set2 sunt:", culori_diferite)


#sau
#culori_diferite = set()
#for culoare in set1:
#    if culoare not in set2:
#        culori_diferite.add(culoare)
#print("Culorile din set1 care nu sunt în set2 sunt:", culori_diferite)