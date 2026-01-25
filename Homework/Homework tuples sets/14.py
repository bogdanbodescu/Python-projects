#5) Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

culori1 = {'roșu', 'albastru', 'verde', 'galben', 'mov'}
culori2 = {'portocaliu', 'verde', 'roz', 'albastru'}
culori_comune = culori1.intersection(culori2)
print("Culorile comune sunt:", culori_comune)

#sau
#culori_comune = culori1 & culori2
#print("Culorile comune sunt:", culori_comune)

#sau

#culori_comune = set()
#for culoare in culori1:
#    if culoare in culori2:
#        culori_comune.add(culoare)
#print("Culorile comune sunt:", culori_comune)