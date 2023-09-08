with open('texto.txt','r') as arquivo1, open('texto2.txt','a') as arquivo2: 
      
    
    for line in arquivo1: 
                     arquivo2.write(line)