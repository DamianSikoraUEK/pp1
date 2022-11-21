file = open('filmTitles.txt','w')

film_titles = ["Morbius","Wasabi","Deadpool","Venom","Iron-Man"]

for i in film_titles:
    
    file.write(i+"\n")

file.close()