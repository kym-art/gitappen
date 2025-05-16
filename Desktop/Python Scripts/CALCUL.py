from tkinter import * 
from random import randrange
# === Définition de quelques gestionnaires d'événements ========: 

#fonction definissant l'apparition aleatoire des boules
    
#fonction definissant le debut du jeux!!!§§
def eat( a,b):
    return can.create_oval(a,b,a+10,b+10,width=1,fill='red')
def start_it(): 
    "Démarrage de l'animation" 
    global flag 
    if flag ==0: 
        flag =1 
        move() 
#fonction definissant l'arret du jeux         
def stop_it(): 
    "Arrêt de l'animation" 
    global flag 
    flag =0

    # definition de la fontion qui surveille la collision carre de tete et ovale cible 
def collision( ):
  
    global flag, aleax,aleay, cc, xmove, ymove
    # Vérifie si la tête du serpent est dans la zone de l'ovale
    if aleax-(cc-4)<=xmove and aleay -(cc-4)<= ymove :
         if xmove<=aleax+8 and ymove<=aleay+8:
    # if a==xmove and b==ymove:
      #  flag = 0 # Arrête le jeu
        #eat()  # Crée un nouvel ovale
            return 0
    
    return 1 
#*************************************************************************************
#definition de la fonction qui surveille la collision du serpent avec lui meme
#*************************************************************************************
def collision_b():
    global serp 
    for i in serp:
        serp 









# ************************************************************************************
# Defnition de la fonction qui gere les niveau du jeu : facile , intermediare ,difficile
# ***************************************************************************************
def niveau():  
    global niv,vitesse  
    if niv==1:
            vitesse=80
            niv=2
            
    elif niv ==2:
        vitesse=40
        niv=3

    elif niv==3:
        niv=1
        vitesse=200
    else :
        niv =1
        vitesse=200
    return niv ,vitesse            
    

    # ****************************************************
#definition des fonction regissant les deplacement en general
    # ***************************************************** 
    # *****************************************************
def go_left(event =None): 
    "délacement vers la gauche" 
 
    global dx, dy 
    dx, dy = -1, 0 
def go_right(event =None): 
    global dx, dy 
    dx, dy = 1, 0 
def go_up(event =None): 
    "déplacement vers le haut" 
    global dx, dy 
    dx, dy = 0, -1 
    
def go_down(event =None): 
    global dx, dy 
    dx, dy = 0, 1 
    
def move(): 
    "Animation du serpent par récursivité" 
    global flag ,serp, xmove, ymove,vitesse
    
    # Principe du mouvement opéré : on déplace le carré de queue, dont les 
    # caractéristiques sont mémorisées dans le premier élément de la liste 
    # <serp>, de manière à l'amener en avant du carré de tête, dont les 
    # caractéristiques sont mémorisées dans le dernier élément de la liste. 
    # On définit ainsi un nouveau carré de tête pour le serpent, dont on 
    # mémorise les caractéristiques en les ajoutant à la liste. 
    # Il ne reste plus qu'à effacer alors le premier élément de la liste, 
    # et ainsi de suite ... : 
    c = serp[0]             # extraction des infos concernant le carré de queue 
    cq = c[0]               # réf. de ce carré (coordonnées inutiles ici) 
    l =len(serp)            # longueur actuelle du serpent (= n. de carrés) 
    c = serp[l-1]           # extraction des infos concernant le carré de tête 
    a1,a2= c[1], c[2]     # coordonnées de ce carré 
    
    
    # Préparation du déplacement proprement dit. 
    # (cc est la taille du carré. dx & dy indiquent le sens du déplacement) : 
    xq, yq = a1+dx*cc, a2+dy*cc             # coord. du nouveau carré de tête 

    
    # Mise à jour des coordonnées pour collision
    xmove, ymove = xq, yq

    # Vérification : a-t-on atteint les limites du canevas ? : 
    if xq<0 or xq>canX-cc or yq<0 or yq>canY-cc: 
        flag =0             # => arrêt de l'animation 
        can.create_text(canX/2, 200, anchor =CENTER, text ="GAME OVER!!!", 
      
                      fill ="red", font="italic 50 bold") 

  

    # Déplacement du carré de queue :
    can.coords(cq, xq, yq, xq+cc, yq+cc)  # déplacement effectif     
    serp.append([cq, xq, yq])     # mémorisation du nouveau carré de tête 
    del(serp[0])                  # effacement (retrait de la liste) 
    # Appel récursif (notion fondamentale ici )de la fonction par elle-même (=> boucle d'animation) : 
    if flag >0: 
        fen.after(vitesse, move) 
  


    # Vérification de la collision avec l'ovale cible
    if collision() == False:  # Si collision détectée
        global oval ,aleax,aleay,score,n
        
        can.delete(oval)  # Efface l'ovale
        aleax=randrange(1,490)
        aleay=randrange(1,490)
        oval=eat(aleax,aleay)
        score+=1
        can.delete("score")
        # On augmente la taille du serpent
        # On ajoute un nouveau carré à la fin du serpent   
        can.create_text (canX/20, 40, anchor =SW, text =f"score! {score}", tag="score" ,fill ="white", font="italic 20 bold") 
        n= n+1
        new = can.create_rectangle(xq, yq, xq + cc, yq + cc, fill="yellow")
        serp.append([new ,xq, yq])  # Mémorisation du nouveau carré de tête
      #on efface l"ancien ovale
       
       

        return 

    can.coords(cq, xq, yq, xq + cc, yq + cc)  # déplacement effectif 
    return
    
    


#condition ou le serpent avale la boule

# === Programme principal : ======== 
# Variables globales modifiables par certaines fonctions : 
flag =0                # commutateur pour l'animation 
dx, dy = 1, 0           # indicateurs pour le sens du déplacement 
#variables gestionnaire des evenements aleatoire
aleax=150
aleay=250
score=0

#  
# Autres variables globales : 
canX, canY = 500, 500   # dimensions du canevas 
x, y, cc,niv,vitesse = 100, 100, 12,1 ,200
x1,y1,n=10,10,4         # coordonnées et coté du premier carré 
# Création de l'espace de jeu (fenêtre, canevas, boutons ...) : 


fen =Tk() 
can =Canvas(fen, bg ='#41B77F', height =canX, width =canY) 
can.pack(padx =10, pady =10)
fen.title("Snake Game")
fen.config(background='#41B77F')

   
# #AFFICHAGE DES OVALs DE FACON ALEARTTOIRE

oval=can.create_oval(aleax,aleay,aleax+10,aleay+10,width=1,fill='red')


bou1 =Button(fen, text="Start", width =10, command =start_it) 
bou1.pack(side =LEFT) 
bou2 =Button(fen, text="Stop", width =10, command =stop_it) 
bou2.pack(side =LEFT) 
bou3 =Button(fen, text=f"niveau {niv},", width =10, command =niveau) 
bou3.pack(side =RIGHT) 
# Association de gestionnaires d'événements aux touches fléchées du clavier : 
fen.bind("<Left>", go_left)         # Attention : les événements clavier 
fen.bind("<Right>", go_right)       # doivent toujours être associés à la 
fen.bind("<Up>", go_up)             # fenêtre principale, et non au canevas 
fen.bind("<Down>", go_down)         # ou à un autre widget. 
# Création du serpent initial (= ligne de 5 carrés). 
# On mémorisera les infos concernant les carrés créés dans une liste de listes : 
serp =[]  # liste vide
    #variables memorisant les cordonnes du carre de tete
         
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête. 
i =0 
while i <5: 
    carre =can.create_rectangle(x, y, x+cc, y+cc, fill="RED") 
    # Pour chaque carré, on mémorise une petite sous-liste contenant 
    # 3 éléments : la référence du carré et ses coordonnées de base : 
    serp.append([carre, x, y]) 
    x =x+cc                 # le carré suivant sera un peu plus à droite 
    i =i+1 

        # Initialisation des coordonnées de la tête du serpent
xmove, ymove = serp[-1][1], serp[-1][2]  # Coordonnées de la tête (dernier carré)   
fen.mainloop()  
# fen.destroy()
