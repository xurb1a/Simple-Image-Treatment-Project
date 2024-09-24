from numpy import *
from matplotlib import pyplot as plt
import random as r

# Fonction pour afficher une image
def AfficherImg(img):
    # Désactiver l'affichage des axes sur le graphique
    plt.axis("off")
    # Afficher l'image avec une interpolation "nearest"
    plt.imshow(img, interpolation="nearest")
    # Afficher l'image en utilisant la colormap "gray" pour représenter les niveaux de gris
    plt.imshow(img, cmap="gray", interpolation="nearest", vmin=0, vmax=1)
    plt.show()# Affichage le graphique

# Fonction pour ouvrir une image à partir d'un chemin
def ouvrirImage(chemin):
    img = plt.imread(chemin)# Utiliser la fonction imread de la bibliothèque Matplotlib pour lire l'image à partir du chemin spécifié
    return img

# Fonction pour sauvegarder une image
def saveImage(img):
    plt.imsave("test.png", img)# Utiliser la fonction imsave de la bibliothèque Matplotlib pour sauvegarder l'image au chemin spécifié

# Partie II

# Fonction pour créer une image noire de dimensions h x l
def image_noire(h, l):
    # Initialiser une liste de listes avec des valeurs 0 pour créer une image entièrement noire
    img = [[0 for i in range(h)] for j in range(l)]
    return img

# Fonction pour créer une image blanche de dimensions h x l
def image_blanche(h, l):
    # Initialiser une liste de listes avec des valeurs 1 pour créer une image entièrement blanche
    img = [[1 for i in range(h)] for j in range(l)]
    return img

# Fonction pour créer une image en damier noir et blanc de dimensions h x l
def creerImgBlancNoir(h, l):
    # Initialiser une liste de listes avec des valeurs 0 et 1 pour créer un damier noir et blanc
    img = [[(i + j) % 2 for j in range(l)] for i in range(h)]
    return array(img)

# Fonction pour obtenir le négatif d'une image
def negatif(img):
    img = ouvrirImage(img)# Ouvrir l'image spécifiée et calcule le négatif en soustrayant chaque pixel de 1
    img2 = [[1 - j for j in i] for i in img]
    return array(img2)

# Partie III

# Fonction pour calculer la luminance moyenne d'une image
def luminance(img):
    img = ouvrirImage(img)# Ouvrir l'image spécifiée
    # Initialisation les variables pour la somme et le nombre de pixels
    somme = 0
    pixels = 0
    # Parcourir chaque pixel de l'image
    for i in img:
         for j in i:
             # Ajoute la valeur du pixel à la somme
             somme += j
             # Incrémente le nombre de pixels
             pixels += 1
    moy = somme / pixels # Calcule la luminance moyenne en divisant la somme par le nombre de pixels
    return moy

# Fonction pour calculer le contraste d'une image
def contrast(Img):
    img = ouvrirImage(Img) # Ouvrir l'image spécifiée
    # Obtenir les dimensions de l'image
    l=len(img)
    c=len(img[0])
    # Calculer le nombre total de pixels
    N = l*c
    # Calculer la luminance moyenne de l'image
    Moy = luminance(Img)
    # Initialiser la variable pour le calcul du contraste
    t=0
    # Parcourir chaque pixel de l'image
    for i in range(l):
            for j in range(c):
                # Ajouter la contribution du pixel au contraste
                t+=(img[i][j][0]-Moy)**2
    t=t/N # Diviser la somme par le nombre total de pixels pour obtenir le contraste
    return t

# Fonction pour trouver la valeur maximale d'une image
def profondeur(img):
    # Ouvrir l'image spécifiée
    img = ouvrirImage(img)
    # Initialiser la valeur maximale avec le premier pixel de l'image
    maxp = img[0][0][0]  # Assuming a 3-channel image (RGB)
    # Parcourir chaque ligne de pixels dans l'image
    for row in img:
        for pixel in row:
            # Parcourir chaque canal de couleur dans le pixel
            for v in pixel:
                # Mettre à jour la valeur maximale si le canal actuel est plus grand
                if v > maxp:
                    maxp = v
    return maxp

# Partie IV

# Fonction pour obtenir l'inverse des couleurs d'une image
def inverser(img):
    # Ouvrir l'image spécifiée et inverse chaque valeur de pixel
    img = ouvrirImage(img)
    inverse = [[255 - pixel for pixel in ligne] for ligne in img]
    return inverse

# Fonction pour effectuer une symétrie horizontale d'une image
def flipH(img):
    # Ouvrir l'image spécifiée et inverse l'ordre des pixels horizontalement
    img = ouvrirImage(img)
    flipped = [l[::-1] for l in img]
    return array(flipped)

# Fonction pour superposer deux images verticalement
def poserV(img1,img2):
    """retourne une image sous-forme d'une tableau composée de 2 images l'une sur l'autre"""
    img1=plt.imread(img1).tolist()
    img2=plt.imread(img2).tolist() #on va travailler par la version 'liste' de l'image
    width1= len(img1[0])
    width2 = len(img2[0])
    if width1==width2: #il faut que les 2 possédent le meme nombre de colonnes
        img3=img1+img2
        return array(img3)
    else: 
        if width1>width2: #réparer la liste qui ne satisfait pas cette condition
            for row in img2:
                for i in range(width1-width2):
                    row.append([255,255,255])
        else: #la réparation se fait l'ajout des pixels blancs
            for row in img1:
                for i in range(width2-width1):
                    row.append([255,255,255])
        img3=img1+img2 #on s'appuie sur le pouvoir de la concatenation des matrices ,déclarés sous forme de listes, l'une sur l'autre 
        return array(img3)

# Fonction pour superposer deux images horizontalement
def poserH(img1, img2):
    """retourne une image sous-forme d'une tableau composée de 2 images l'une á cote de l'autre"""
    img1 = plt.imread(img1).tolist() #obtenir et convertir le tableaux de chaque image en une liste
    img2 = plt.imread(img2).tolist()
    height1 = len(img1)
    height2 = len(img2)
    if height1>height2: #tester si les dimensions de ces listes sont convenables pour la concatenatios dans une liste globale
        width = len(img2[0])
        for i in range(height1-height2):             #changer le format de la liste qui ne satisfait pas la condition de la concatenation
            li = array([[255,255,255] for k in range(width)],dtype=int).tolist() #compléter chaque ligne avec des pixels blancs
            img2.append(li)                          
    else:
        width = len(img1[0])
        for i in range(height2-height1):
            li = array([[255,255,255] for k in range(width)],dtype=int).tolist()
            img1.append(li)
    img3=[[0] for i in range (height1)]
    img3=concatenate((array(img1), array(img2)), axis=1) #appeler la fonction concaternate() du module numpy pour faire la concatenation 
    return img3                                          #de ces listes aprés la réparition et la conversion en tableaux

# Fonction pour afficher la taille d'une image en octets
def sizeofimage(img):
    img = ouvrirImage(img)# Ouvrir l'image spécifiée et calcule la taille en octets
    size = len(img) * len(img[0]) * 3
    print(size)

# Fonction pour initialiser une image RGB avec des valeurs aléatoires
def initImageRGB():
    # Initialiser une image RGB avec des valeurs de pixels aléatoires
    return array([[[r.randrange(256) for _ in range(3)] for _ in range(6)] for _ in range(3)])

# Fonction pour effectuer une symétrie horizontale ou verticale d'une image
def symetrie(img):
    # Ouvrir l'image spécifiée et demande à l'utilisateur de choisir la symétrie
    img = ouvrirImage(img)
    largeur = len(img[0])
    hauteur = len(img)
    c = int(input("1- pour faire la symétrie horizontale. 2- pour le symétrie verticale : "))
    if c == 1:
        # Effectuer la symétrie horizontale en inversant l'ordre des pixels
        img = [[img[i][j] if j < largeur // 2 else img[i][largeur - 1 - j] for j in range(largeur)] for i in range(hauteur)]
    elif c == 2:
        # Effectuer la symétrie verticale en inversant l'ordre des lignes de pixels
        img = [[img[i][j] if i < hauteur // 2 else img[hauteur - 1 - i][j] for j in range(largeur)] for i in range(hauteur)]
    AfficherImg(array(img))

# Fonction pour convertir une image RGB en niveaux de gris
def grayscale(imageRGB):
    imageRGB = plt.imread(imageRGB)  # Open the specified image
    # Separate the color channels (red, green, blue)
    r, g, b = imageRGB[:, :, 0], imageRGB[:, :, 1], imageRGB[:, :, 2]
    # Convert the channels to lists
    r, g, b = r.tolist(), g.tolist(), b.tolist()
    img = []  # Initialize an empty list for the grayscale image
    for i in range(len(imageRGB)):
        row = []
        # Iterate over each pixel of the image
        for j in range(len(imageRGB[0])):
            # Calculate the average value of the channels to obtain the grayscale level
            gray_value = (r[i][j] + g[i][j] + b[i][j]) / 3
            row.append(gray_value)
        img.append(row)  # Add the row to the grayscale image
    return array(img)
