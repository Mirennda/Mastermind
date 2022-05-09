import tkinter as tk
from tkinter import messagebox


##################
# Mensuration du canvas

LARGEUR = 1361
HAUTEUR = 700
# Il y a 10 essaies donc 10 ligne + code secret donc 11 ligne

#################
#Attribuution des couleurs
cyan = "cyan2"
blanc = "snow"


#################
#Confirmetion de l'attribution

def message001():
                messagebox.showinfo ("","Mastermind")
message001 ()



#################
#Consigne de jeu joueur 1

def message():
                messagebox.showinfo ("Resultat", "Bienvenue !!!! Vous ètes le joueur 1. Joueur 1 choisissez les couleurs de chaqu'un vos pions secrets. Les pions sont disposés de haut en bas. Attention votre choix doit s'effectué dans le plus grand SECRET jusqu'à la fin de la partie. Les couleurs doivent être écrites en anglais ! Vous pouvez choisir entre Rouge = Red, Vert = Green, Jaune = Yellow, Bleu = Blue et Rose = Pink. Fait votre choix ! ~~~~Bonne chance~~~~")
message ()

def passe():
                messagebox.showinfo ("Attention", "Ne pas oublié de fermer la fenêtre en cliant sur la croix 'X'")

passe ()


#################
#Choix des couleur pour le joueur 1 (le "#input (...)" c'est pour pas qu'on est a remplie a charque fois qu'on veux testé le code

Pion_1 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Consigne sur le fonctionnement des detecteur

def message2():
    messagebox.showinfo("Info", "Si le mot cyan s'affiche, cela signie que vous avez une couleur bien placé. Si le mot s'affiche deux fois, vous avez deux couleurs bien placé...Si le mot blanc s'affiche cela signifie que vous avez la bonne couleur mais pas le bonne emplacement. Si le mot blanc s'affiche deux fois cela signifie que vous avez deux couleurs mal placé...Si rien ne s'affiche vous n'avais pas les bonnes couleurs.")

message2 ()

def passe1():
                messagebox.showinfo ("Attention", "Ne pas oublié de fermer la fenetre en cliant sur la croix 'X'")

passe1 ()

#print ("Si la le mot cyan s'affiche cela signie que vous avez une couleur bien placé", 
#"Si le mot s'affiche deux fois vous avez deux couleurs bien placé...",
#"Si le mot blanc s'affiche cela signifie que vous avez la bonne couleur mais pas le bonne emplacement",
#"Si le mot blanc s'affiche deux fois cela signifie que vous avez deux couleurs mal placé...",
#"Si rien ne s'affiche vous n'avais pas les bonnes couleurs.")

#################
#Creation des quatres pions du joueur 1

def creer_cercles():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 32.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1)
    return [cercle, dx, dy]



def creer_cercles1():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 32.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2)
    return [cercle, dx, dy]


def creer_cercles2():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 32.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3)
    return [cercle, dx, dy]


def creer_cercles3():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 32.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4)
    return [cercle, dx, dy]


#En horizontal ils doivent etre tous sur la même colone donc x = 123; 1361//11= 123
#En vertical ils doivent avoir un place donc 700-20(diamétre cercle)= 660 ; 660//2= 330 donc la moitier
#   330(moitier)//2 = 165 donc la moitier de la moitier ; 165-20(cercle)= 145~ ; 145//2= 73~ position du premier cercle
#   330(moitier)-20(cercle)=310 ; 310-73=258 position du deuxième cercle
#   495 = 330 (moitier)+ 165 (moitier//2); 495-20(cercle)= 475; 475 -73 = 402 position du troisième cercle
#   660- 73 = 587 position du quatriéme cercle
# constantes


#################
#Consigne du joueur 2 

def message1():
            messagebox.showinfo ("Resultat", "Autour du joueur 2 ! Bienvunue ! Joueur 2 vous allez devoir touvé la combinéson de couleur et le bonne emplacement du joueur 1. Les pions sont disposés de haut en bas. Attention vous n'avais que 10 chances. Les couleurs doivent étre écrit en anglais ! Vous pouvez choisir entre Rouge = Red, Vert = Green, Jaune = Yellow, Bleu = Blue et Rose = Pink. Faite votre choix ! ~~~~Bonne chance~~~~")

message1 ()


#################
#Choix des couleur pour le joueur 2 (colonne 1)
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")

print("Pion de la colonne 1")

Pion_1_c1 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c1 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c1 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c1 = input ("Quelle est la couleur du pion 4 ? ")





#################
#Creation des quatres pions du joueur 2 (colonne 1)

def creer_cercles_c1():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 149.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c1)
    return [cercle, dx, dy]

 
def creer_cercles1_c1():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y =  149.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c1)
    return [cercle, dx, dy]


def creer_cercles2_c1():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y =  149.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c1)
    return [cercle, dx, dy]


def creer_cercles3_c1():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 149.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c1)
    return [cercle, dx, dy]




#################
#Creation des quatres detecteurs (colonne 1)

        #################
        # Fontionnement 


Position_1_c1 = []

if Pion_1 == Pion_1_c1:
    Position_1_c1.append (cyan)
    print ("Cyan")
elif Pion_1 == Pion_2_c1:
    Position_1_c1.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c1:
    Position_1_c1.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c1:
    Position_1_c1.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c1():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 140,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c1)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_2_c1 = []

if Pion_2 == Pion_2_c1:
    Position_2_c1.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c1:
    Position_2_c1.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c1:
    Position_2_c1.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c1:
    Position_2_c1.append(blanc)
    print ("Blanc")
else :
    print()
 
def detecteur2_c1():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 155,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c1)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_3_c1 = []

if Pion_3 == Pion_3_c1:
    Position_3_c1.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c1:
    Position_3_c1.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c1:
    Position_3_c1.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c1:
    Position_3_c1.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c1():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 140,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c1)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_4_c1 = []

if Pion_4 == Pion_4_c1:
    Position_4_c1.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c1:
    Position_4_c1.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c1:
    Position_4_c1.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c1:
    Position_4_c1.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur4_c1():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 155,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c1)
    return [cercle, dx, dy]


################# 
#Choix des couleur pour le joueur 2

Pion_1_c2 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c2 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c2 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c2 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 2)

print("Pion de la colonne 2")

def creer_cercles_c2():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 256.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c2)
    return [cercle, dx, dy]

 
def creer_cercles1_c2():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 256.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c2)
    return [cercle, dx, dy]


def creer_cercles2_c2():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 256.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c2)
    return [cercle, dx, dy]


def creer_cercles3_c2():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 256.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c2)
    return [cercle, dx, dy]

#################
#Creation des quatres detecteurs (colonne 2)

        #################
        # Fontionnement 


Position_1_c2 = []

if Pion_1 == Pion_1_c2:
    Position_1_c2.append (cyan)
    print ("Cyan")
elif Pion_1 == Pion_2_c2:
    Position_1_c2.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c2:
    Position_1_c2.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c2:
    Position_1_c2.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c2():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 140,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c2)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_2_c2 = []

if Pion_2 == Pion_2_c2:
    Position_2_c2.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c2:
    Position_2_c2.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c2:
    Position_2_c2.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c2:
    Position_2_c2.append(blanc)
    print ("Blanc")
else :
    print()
 
def detecteur2_c2():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 155,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c2)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_3_c2 = []

if Pion_3 == Pion_3_c2:
    Position_3_c2.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c2:
    Position_3_c2.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c2:
    Position_3_c2.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c2:
    Position_3_c2.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c2():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 140,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c2)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_4_c2 = []

if Pion_4 == Pion_4_c2:
    Position_4_c2.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c2:
    Position_4_c2.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c2:
    Position_4_c2.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c2:
    Position_4_c2.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur4_c2():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 155,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c2)
    return [cercle, dx, dy]


################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 3")

Pion_1_c3 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c3 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c3 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c3 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 3)

def creer_cercles_c3():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 363.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c3)
    return [cercle, dx, dy]

 
def creer_cercles1_c3():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 363.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c3)
    return [cercle, dx, dy]


def creer_cercles2_c3():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 363.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c3)
    return [cercle, dx, dy]


def creer_cercles3_c3():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 363.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c3)
    return [cercle, dx, dy]


#################
#Creation des quatres detecteurs (colonne 3)

        #################
        # Fontionnement 


Position_1_c3 = []

if Pion_1 == Pion_1_c3:
    Position_1_c3.append (cyan)
    print ("Cyan")
elif Pion_1 == Pion_2_c3:
    Position_1_c3.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c3:
    Position_1_c3.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c3:
    Position_1_c3.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur1_c3():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 353,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c3)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_2_c3 = []

if Pion_2 == Pion_2_c3:
    Position_2_c3.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c3:
    Position_2_c3.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c3:
    Position_2_c3.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c3:
    Position_2_c3.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur2_c3():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 367,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c3)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_3_c3 = []

if Pion_3 == Pion_3_c3:
    Position_3_c3.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c3:
    Position_3_c3.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c3:
    Position_3_c3.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c3:
    Position_3_c3.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c3():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 353,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c3)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_4_c3 = []

if Pion_4 == Pion_4_c3:
    Position_4_c3.append (cyan)
    print("Cyan")
elif Pion_4 == Pion_1_c3:
    Position_4_c3.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c3:
    Position_4_c3.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c3:
    Position_4_c3.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur4_c3():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 367,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c3)
    return [cercle, dx, dy]


################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 4")

Pion_1_c4 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c4 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c4 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c4 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 4)

def creer_cercles_c4():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 470.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c4)
    return [cercle, dx, dy]

 
def creer_cercles1_c4():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 470.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c4)
    return [cercle, dx, dy]


def creer_cercles2_c4():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 470.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c4)
    return [cercle, dx, dy]


def creer_cercles3_c4():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 470.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c4)
    return [cercle, dx, dy]


#################
#Creation des quatres detecteurs (colonne 4)

        #################
        # Fontionnement 


Position_1_c4 = []

if Pion_1 == Pion_1_c4:
    Position_1_c4.append (cyan)
    print ("Cyan")
elif Pion_1== Pion_2_c4:
    Position_1_c4.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c4:
    Position_1_c4.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c4:
    Position_1_c4.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c4():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 465,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c4)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_2_c4 = []

if Pion_2 == Pion_2_c4:
    Position_2_c4.append (cyan)
    print("Cyan")
elif Pion_2== Pion_1_c4:
    Position_2_c4.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c4:
    Position_2_c4.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c4:
    Position_2_c4.append(blanc)
    print ("Blanc")
else :
    print()

 
def detecteur2_c4():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 478,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c4)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_3_c4 = []

if Pion_3 == Pion_3_c4:
    Position_3_c4.append (cyan)
    print ("Cyan")
elif Pion_3== Pion_1_c4:
    Position_3_c4.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c4:
    Position_3_c4.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c4:
    Position_3_c4.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c4():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 465,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c4)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_4_c4 = []

if Pion_4 == Pion_4_c4:
    Position_4_c4.append (cyan)
    print("Cyan")
elif Pion_4== Pion_1_c4:
    Position_4_c4.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c4:
    Position_4_c4.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c4:
    Position_4_c4.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur4_c4():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 478,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c4)
    return [cercle, dx, dy]
    

################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 5")

Pion_1_c5 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c5 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c5 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c5 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 5)

def creer_cercles_c5():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 577.27,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c5)
    return [cercle, dx, dy]

 
def creer_cercles1_c5():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 577.27 ,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c5)
    return [cercle, dx, dy]


def creer_cercles2_c5():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 577.27,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c5)
    return [cercle, dx, dy]


def creer_cercles3_c5():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 577.27,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c5)
    return [cercle, dx, dy]


#################
#Creation des quatres detecteurs (colonne 5)

        #################
        # Fontionnement 


Position_1_c5 = []

if Pion_1 == Pion_1_c5:
    Position_1_c5.append (cyan)
    print ("Cyan")
elif Pion_1== Pion_2_c5:
    Position_1_c5.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c5:
    Position_1_c5.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c5:
    Position_1_c5.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c5():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 572,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c5)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_2_c5 = []

if Pion_2 == Pion_2_c5:
    Position_2_c5.append (cyan)
    print ("Cyan")
elif Pion_2== Pion_1_c5:
    Position_2_c5.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c5:
    Position_2_c5.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c5:
    Position_2_c5.append(blanc)
    print ("Blanc")
else :
    print()
 
def detecteur2_c5():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 585,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c5)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_3_c5 = []

if Pion_3 == Pion_3_c5:
    Position_3_c5.append (cyan)
    print ("Cyan")
elif Pion_3== Pion_1_c5:
    Position_3_c5.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c5:
    Position_3_c5.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c5:
    Position_3_c5.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c5():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 572,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c5)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_4_c5 = []

if Pion_4 == Pion_4_c5:
    Position_4_c5.append (cyan)
    print ("Cyan")
elif Pion_4== Pion_1_c5:
    Position_4_c5.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c5:
    Position_4_c5.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c5:
    Position_4_c5.append(blanc)
    print ("Blanc")
else :
    print() 

def detecteur4_c5():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 585,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c5)
    return [cercle, dx, dy]




################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 6")

Pion_1_c6 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c6 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c6 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c6 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 6)

def creer_cercles_c6():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 674.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c6)
    return [cercle, dx, dy]

 
def creer_cercles1_c6():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 674.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c6)
    return [cercle, dx, dy]


def creer_cercles2_c6():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 674.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c6)
    return [cercle, dx, dy]


def creer_cercles3_c6():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 674.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c6)
    return [cercle, dx, dy]




#################
#Creation des quatres detecteurs (colonne 6)

        #################
        # Fontionnement 


Position_1_c6 = []

if Pion_1 == Pion_1_c6:
    Position_1_c6.append (cyan)
    print ("Cyan")
elif Pion_1 == Pion_2_c6:
    Position_1_c6.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c6:
    Position_1_c6.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c6:
    Position_1_c6.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c6():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 660.25,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill= Position_1_c6)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_2_c6 = []

if Pion_2 == Pion_2_c6:
    Position_2_c6.append (cyan)
    print ("Cyan")
elif Pion_2== Pion_1_c6:
    Position_2_c6.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c6:
    Position_2_c6.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c6:
    Position_2_c6.append(blanc)
    print ("Blanc")
else :
    print()
 
def detecteur2_c6():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 673,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c6)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_3_c6 = []

if Pion_3 == Pion_3_c6:
    Position_3_c6.append (cyan)
    print ("Cyan")
elif Pion_3== Pion_1_c6:
    Position_3_c6.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c6:
    Position_3_c6.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c6:
    Position_3_c6.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur3_c6():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 660,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c6)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_4_c6 = []

if Pion_4 == Pion_4_c6:
    Position_4_c6.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c6:
    Position_4_c6.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c6:
    Position_4_c6.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c6:
    Position_4_c6.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur4_c6():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 673,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c6)
    return [cercle, dx, dy]
    

################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 7")

Pion_1_c7 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c7 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c7 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c7 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 7)

def creer_cercles_c7():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 791.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c7)
    return [cercle, dx, dy]

 
def creer_cercles1_c7():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 791.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c7)
    return [cercle, dx, dy]


def creer_cercles2_c7():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 791.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c7)
    return [cercle, dx, dy]


def creer_cercles3_c7():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 791.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c7)
    return [cercle, dx, dy]



#################
#Creation des quatres detecteurs (colonne 7)

        #################
        # Fontionnement 


Position_1_c7 = []

if Pion_1 == Pion_1_c7:
    Position_1_c7.append (cyan)
    print ("Cyan")
elif Pion_1== Pion_2_c7:
    Position_1_c7.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c7:
    Position_1_c7.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c7:
    Position_1_c7.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c7():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 786,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c7)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_2_c7= []

if Pion_2== Pion_2_c7:
    Position_2_c7.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c7:
    Position_2_c7.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c7:
    Position_2_c7.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c7:
    Position_2_c7.append(blanc)
    print ("Blanc")
else :
    print()
 
def detecteur2_c7():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 799,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c7)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_3_c7 = []

if Pion_3 == Pion_3_c7:
    Position_3_c7.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c7:
    Position_3_c7.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c7:
    Position_3_c7.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c7:
    Position_3_c7.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur3_c7():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 786,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c7)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_4_c7 = []

if Pion_4 == Pion_4_c7:
    Position_4_c7.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c7:
    Position_4_c7.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c7:
    Position_4_c7.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c7:
    Position_4_c7.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur4_c7():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 799,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c7)
    return [cercle, dx, dy]


#################
#Choix des couleur pour le joueur 2

print("Pion de la colonne 8")

Pion_1_c8 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c8 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c8 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c8 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 8)

def creer_cercles_c8():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 898.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c8)
    return [cercle, dx, dy]

 
def creer_cercles1_c8():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 898.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c8)
    return [cercle, dx, dy]


def creer_cercles2_c8():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 898.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c8)
    return [cercle, dx, dy]


def creer_cercles3_c8():

    """Dessine un disque et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = 898.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c8)
    return [cercle, dx, dy]

#################
#Creation des quatres detecteurs (colonne 8)

        #################
        # Fontionnement 


Position_1_c8 = []

if Pion_1 == Pion_1_c8:
    Position_1_c8.append (cyan)
    print ("Cyan")
elif Pion_1== Pion_2_c8:
    Position_1_c8.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c8:
    Position_1_c8.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c8:
    Position_1_c8.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur1_c8():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 893,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c8)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_2_c8 = []

if Pion_2 == Pion_2_c8:
    Position_2_c8.append (cyan)
    print ("Cyan")
elif Pion_2== Pion_1_c8:
    Position_2_c8.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c8:
    Position_2_c8.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c8:
    Position_2_c8.append(blanc)
    print ("Blanc")
else :
    print()

 
def detecteur2_c8():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 906,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c8)
    return [cercle, dx, dy]


        #################
        # Fontionnement 

Position_3_c8 = []

if Pion_3 == Pion_3_c8:
    Position_3_c8.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c8:
    Position_3_c8.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c8:
    Position_3_c8.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c8:
    Position_3_c8.append(blanc)
    print ("Blanc")

else :
    print()

def detecteur3_c8():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 893,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c8)
    return [cercle, dx, dy]

        #################
        # Fontionnement 

Position_4_c8 = []

if Pion_4 == Pion_4_c8:
    Position_4_c8.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c8:
    Position_4_c8.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c8:
    Position_4_c8.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c8:
    Position_4_c8.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur4_c8():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 906,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c8)
    return [cercle, dx, dy]
  


#################
#Choix des couleur pour le joueur 2

print("Pion de la colonne 9")

Pion_1_c9 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c9 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c9 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c9 = input ("Quelle est la couleur du pion 4 ? ")


#################
#Creation des quatres pions du joueur 2 (colonne 9)

def creer_cercles_c9():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1005.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c9)
    return [cercle, dx, dy]

 
def creer_cercles1_c9():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1005.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c9)
    return [cercle, dx, dy]


def creer_cercles2_c9():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1005.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c9)
    return [cercle, dx, dy]


def creer_cercles3_c9():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 1005.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c9)
    return [cercle, dx, dy]

#################
#Creation des quatres detecteurs (colonne 9)
   
        #################
        # Fontionnement 


Position_1_c9 = []

if Pion_1 == Pion_1_c9:
    Position_1_c9.append (cyan)
    print ("Cyan")
elif Pion_1== Pion_2_c9:
    Position_1_c9.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c9:
    Position_1_c9.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c9:
    Position_1_c9.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur1_c9():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1000,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c9)
    return [cercle, dx, dy]
   
        #################
        # Fontionnement 

Position_2_c9 = []

if Pion_2 == Pion_2_c9:
    Position_2_c9.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c9:
    Position_2_c9.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c9:
    Position_2_c9.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c9:
    Position_2_c9.append(blanc)
    print ("Blanc")
else :
    print()

def detecteur2_c9():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1013,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c9)
    return [cercle, dx, dy]
   
        #################
        # Fontionnement 

Position_3_c9 = []

if Pion_3 == Pion_3_c9:
    Position_3_c9.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c9:
    Position_3_c9.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c9:
    Position_3_c9.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c9:
    Position_3_c9.append(blanc)
    print ("Blanc")
else :
    print()

    

def detecteur3_c9():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1000,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c9)
    return [cercle, dx, dy]
   
        #################
        # Fontionnement 

Position_4_c9 = []

if Pion_4 == Pion_4_c9:
    Position_4_c9.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c9:
    Position_4_c9.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c9:
    Position_4_c9.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c9:
    Position_4_c9.append(blanc)
    print ("Blanc")
else :
    print()

    

def detecteur4_c9():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 1013,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c9)
    return [cercle, dx, dy]


################# 
#Choix des couleur pour le joueur 2

print("Pion de la colonne 10")

Pion_1_c10 = input ("Quelle est la couleur du pion 1 ? ") 
Pion_2_c10 = input ("Quelle est la couleur du pion 2 ? ")
Pion_3_c10 = input ("Quelle est la couleur du pion 3 ? ")
Pion_4_c10 = input ("Quelle est la couleur du pion 4 ? ")



#################
#Creation des quatres pions du joueur 2 (colonne 10)

def creer_cercles_c10():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1112.25,73 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_1_c10)
    return [cercle, dx, dy]

 
def creer_cercles1_c10():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1112.25,258 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_2_c10)
    return [cercle, dx, dy]


def creer_cercles2_c10():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1112.25,402 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_3_c10)
    return [cercle, dx, dy]


def creer_cercles3_c10():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 1112.25,587 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Pion_4_c10)
    return [cercle, dx, dy]


#################
#Creation des quatres detecteurs (colonne 10)
   
        #################
        # Fontionnement 


Position_1_c10 = []

if Pion_1 == Pion_1_c10:
    Position_1_c10.append (cyan)
    print ("Cyan")
elif Pion_1 == Pion_2_c10:
    Position_1_c10.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_3_c10:
    Position_1_c10.append(blanc)
    print ("Blanc")
elif Pion_1 == Pion_4_c10:
    Position_1_c10.append(blanc)
    print ("Blanc")
else :
    print()

    
def detecteur1_c10():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1107,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_1_c10)
    return [cercle, dx, dy]
   
        #################
        # Fontionnement 

Position_2_c10 = []

if Pion_2 == Pion_2_c10:
    Position_2_c10.append (cyan)
    print ("Cyan")
elif Pion_2 == Pion_1_c10:
    Position_2_c10.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_3_c10:
    Position_2_c10.append(blanc)
    print ("Blanc")
elif Pion_2 == Pion_4_c10:
    Position_2_c10.append(blanc)
    print ("Blanc")
else :
    print()

   
 
def detecteur2_c10():

    """Dessine un disque et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1120,665 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_2_c10)
    return [cercle, dx, dy]
   
        #################
        # Fontionnement 

Position_3_c10 = []

if Pion_3 == Pion_3_c10:
    Position_3_c10.append (cyan)
    print ("Cyan")
elif Pion_3 == Pion_1_c10:
    Position_3_c10.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_2_c10:
    Position_3_c10.append(blanc)
    print ("Blanc")
elif Pion_3 == Pion_4_c10:
    Position_3_c10.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur3_c10():

    """Dessine un disque bleu et retourne son identifiantet les valeurs de déplacements dans une liste"""
    x, y = 1107,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_3_c10)
    return [cercle, dx, dy]

   
        #################
        # Fontionnement 

Position_4_c10 = []

if Pion_4 == Pion_4_c10:
    Position_4_c10.append (cyan)
    print ("Cyan")
elif Pion_4 == Pion_1_c10:
    Position_4_c10.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_2_c10:
    Position_4_c10.append(blanc)
    print ("Blanc")
elif Pion_4 == Pion_3_c10:
    Position_4_c10.append(blanc)
    print ("Blanc")
else :
    print()


def detecteur4_c10():

    """Dessine un disque et retourne son identifiant et les valeurs de déplacements dans une liste"""
    x, y = 1120,680 #{"x"=horizonal(+ petit= gauche +grand = droit);"y"=vertical(+ petit= haut +grand = bas)}
    dx, dy = 3, 5
    rayon = 5
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill=Position_4_c10)
    return [cercle, dx, dy]



#distance a ne pas depacé : 1361

#nous avons 11 balles de rayon 20

#donc 11 colonnes 

#le centre de la permier balle est a 32.25
#c1 : 96.75
#c2 : 161.25
#c3 : 225.75
#c4 : 290.25
#c5 : 354.75
#c6 : 419.25
#c7 : 483.75
#c8 : 548.25
#c9 : 612.75
#c10 :677.25
#c11 :741.75
#20 (rayon d'un cercle)*11 (colonnes) + 32.25 (milieu de colonnes)*2 = 284.5
#284.5 + 97*11 (ecare) =1 351,5

#1 351,5 < 1361


#################
#Paramétre du canvas

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid() 


#################
#Listes de colonnes

liste = [Pion_1,Pion_2,Pion_3,Pion_4]
liste_c1 = [Pion_1_c1, Pion_2_c1, Pion_3_c1, Pion_4_c1]
liste_c2 = [Pion_1_c2, Pion_2_c2, Pion_3_c2, Pion_4_c2]
liste_c3 = [Pion_1_c3, Pion_2_c3, Pion_3_c3, Pion_4_c3]
liste_c4 = [Pion_1_c4, Pion_2_c4, Pion_3_c4, Pion_4_c4]
liste_c5 = [Pion_1_c5, Pion_2_c5, Pion_3_c5, Pion_4_c5]
liste_c6 = [Pion_1_c6, Pion_2_c6, Pion_3_c6, Pion_4_c6]
liste_c7 = [Pion_1_c7, Pion_2_c7, Pion_3_c7, Pion_4_c7]
liste_c8 = [Pion_1_c8, Pion_2_c8, Pion_3_c8, Pion_4_c8]
liste_c9 = [Pion_1_c9, Pion_2_c9, Pion_3_c9, Pion_4_c9]
liste_c10 = [Pion_1_c10, Pion_2_c10, Pion_3_c10, Pion_4_c10]
 

#################
#Message de felicitation

def pop():
    messagebox.showinfo("Resultat", "Bravo!")

if liste == liste_c1 :
    pop ()

elif liste == liste_c2 :
    pop ()

elif liste == liste_c3 :
    pop ()

elif liste == liste_c4 :
    pop ()

elif liste == liste_c5 :
    pop ()

elif liste == liste_c6 :
    pop ()

elif liste == liste_c7 :
    pop ()

elif liste == liste_c8 :
    pop ()

elif liste == liste_c9 :
    pop ()

elif liste == liste_c10 :
    pop ()

else :
    print ( )


#################
#liste return ( ne pas déplacé car [pas encore def])

cercle =[creer_cercles(),creer_cercles1(),creer_cercles2(),creer_cercles3(),
creer_cercles_c1(),creer_cercles1_c1(),creer_cercles2_c1(),creer_cercles3_c1(),
creer_cercles_c2(),creer_cercles1_c2(),creer_cercles2_c2(),creer_cercles3_c2(),
creer_cercles_c3(),creer_cercles1_c3(),creer_cercles2_c3(),creer_cercles3_c3(),
creer_cercles_c4(),creer_cercles1_c4(),creer_cercles2_c4(),creer_cercles3_c4(),
creer_cercles_c5(),creer_cercles1_c5(),creer_cercles2_c5(),creer_cercles3_c5(),
creer_cercles_c6(),creer_cercles1_c6(),creer_cercles2_c6(),creer_cercles3_c6(),
creer_cercles_c7(),creer_cercles1_c7(),creer_cercles2_c7(),creer_cercles3_c7(),
creer_cercles_c8(),creer_cercles1_c8(),creer_cercles2_c8(),creer_cercles3_c8(),
creer_cercles_c9(),creer_cercles1_c9(),creer_cercles2_c9(),creer_cercles3_c9(),
creer_cercles_c10(),creer_cercles1_c10(),creer_cercles2_c10(),creer_cercles3_c10(),
detecteur1_c1(), detecteur2_c1(),detecteur3_c1(),detecteur4_c1(),
detecteur1_c2(),detecteur2_c2(), detecteur3_c2(),detecteur4_c2(),
detecteur1_c3(),detecteur2_c3(), detecteur3_c3(),detecteur4_c3(),
detecteur1_c4(),detecteur2_c4(), detecteur3_c4(),detecteur4_c4(),
detecteur1_c5(),detecteur2_c5(), detecteur3_c5(),detecteur4_c5(),
detecteur1_c6(),detecteur2_c6(), detecteur3_c6(),detecteur4_c6(),
detecteur1_c7(),detecteur2_c7(), detecteur3_c7(),detecteur4_c7(),
detecteur1_c8(),detecteur2_c8(), detecteur3_c8(),detecteur4_c8(),
detecteur1_c9(),detecteur2_c9(), detecteur3_c9(),detecteur4_c9(),
detecteur1_c10(), detecteur2_c10(),detecteur3_c10(),detecteur4_c10()] 


#################
#Racine du programme

racine.mainloop() # ne pas deplacé si non plus rien ne fontionne.

#################
#Souce

# cour 07 l1-Python : graphisme
#cour 04 l1-Python : fontions
#cour 02 l1-Python : les structures conditionnelles
#cour 06 l1-Python : listes
#balle.py
#WayToLearnX.com
#google
#forum
