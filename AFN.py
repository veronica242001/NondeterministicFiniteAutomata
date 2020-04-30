#Implementam un automat finit nedetermisnist
f = open("intrare1.txt","r")
n = int( f.readline() ) #nr de stari in automat
init = int( f.readline() ) # starea initiala
nrf = int( f.readline() ) #nr de stari finale
sir = f.readline()
starif = [ int(x) for x in sir.split() ]# vector de stari finale
nrtranz = int( f.readline() )  # nr de tranzitii
M = [[[1001]] *(n) for i in range(n)]
for i in range(nrtranz): # construim o matrice pt tranzitii
     sir2 =f .readline()
     a = int(sir2.split()[0])
     b = int(sir2.split()[1])
     M[a][b] = [ x for x in sir2.split()[2:]]
cuv = f.readline() # citim cuv care trebuie verificat
L = [ x for x in cuv[:len(cuv)-1]] #punem literele intr-un vector

l1 = [init] #vector in care retinem starile in care am putea ajunge la un anumit pas
l2 = []
for lit in L: #parcurgem cuvantul care trebuie verificat litera cu litera

    for i in l1:
        for j in range(n):
            if lit in M[i][j]: #verif daca exista tranzitie coresp literei
                l2.append(j) #punem in alt vector multimeaa de stari in care s ar putea ajunge
    l1 = l2
    l2 = []
q = 1

for x in l1:
    if x in starif:#verif daca una dintre starile posibile in care am ajuns dupa ce am parcurs tot cuvantul
        print("Cuvantul este acceptat")# se afla printre strarile finale
        q = 0
        break
if q == 1:
    print("Cuvantul nu este acceptat")



