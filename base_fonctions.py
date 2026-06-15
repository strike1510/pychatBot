# Auteurs : Hugo Thouraud de Lavignére et Cheikh Tidiane Fall | My First Chat Bot 
# Ce fichier contient les fonctions de base du projet qui permettrons au corpus d'être exploitable par le reste des fonctions


import os
def show_files(repertoire):
    """
        Cette fonction qui prend en paramétre un répertoire , permet d'afficher tout les fichiers de celui-ci.
    """
    
    if not os.path.exists(repertoire):# Vérifier si le répertoire existe
        print("Le répertoire spécifié n'existe pas.")
        return

    # Parcourir tous les fichiers du répertoire
    for fichier in os.listdir(repertoire):
        # Vérifier si c'est un fichier
        if os.path.isfile(os.path.join(repertoire, fichier)):
            print(fichier)


def extract_names(repertoire):
    """
        Cette fonction permet d'extraire les nom des documents texte contenant les nominations de présidents. Ceux-ci sont dans le répertoire.
    """
    L2 = []
    for fichier in os.listdir(repertoire):
        L2.append(fichier)
    for i in range(len(L2)): #Notre boucle permet de remplacer les éléments qui ne constituent pas le nom des présidents
        L2[i] = L2[i].replace(".txt","")
        L2[i] = L2[i].replace("0","")
        L2[i] = L2[i].replace("1","")
        L2[i] = L2[i].replace("2","")
        L2[i] = L2[i].replace("3","")
        L2[i] = L2[i].replace("4","")
        L2[i] = L2[i].replace("5","")
        L2[i] = L2[i].replace("6","")
        L2[i] = L2[i].replace("7","")
        L2[i] = L2[i].replace("8","")
        L2[i] = L2[i].replace("9","")
        L2[i] = L2[i].replace("Nomination_","")
    
    L3 = []
    for nom in L2:
        if nom not in L3:
            L3.append(nom)
            print(nom)

def names_f(repertoire):
    '''
        Cette fonction à le même but que la précédente mais juste une approche différente
    '''
    
    L1 = ["Valéry Giscard dEstaing","Jacques Chirac","Nicolas Sarkozy","François Mitterrand","François Hollande","Emanuelle Macron"]
    L2 = []
    for fichier in os.listdir(repertoire):
        L2.append(fichier)
    for i in range(len(L2)):
        L2[i] = L2[i].replace(".txt","")
        L2[i] = L2[i].replace("0","")
        L2[i] = L2[i].replace("1","")
        L2[i] = L2[i].replace("2","")
        L2[i] = L2[i].replace("3","")
        L2[i] = L2[i].replace("4","")
        L2[i] = L2[i].replace("5","")
        L2[i] = L2[i].replace("6","")
        L2[i] = L2[i].replace("7","")
        L2[i] = L2[i].replace("8","")
        L2[i] = L2[i].replace("9","")
        L2[i] = L2[i].replace("Nomination_","")
    
    L3 = []
    for nom in L2:
        if nom not in L3:
            L3.append(nom)
            for prenom in L1:
                if nom in prenom:
                    print(prenom)
        


def transition(drepertoire,frepertoire):
    ''' Cette fonction nous permet de déplacer des fichiers d'un répertoire A vers un répertoire B'''
    fichiers = []
    for fichier in os.listdir(drepertoire): # Boucle pour récuperer chaque fichiers dans le répertoire
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for i in fichiers:
        source_file = '{}/{}'.format(drepertoire,i)         # Nous permet de donner un nom au nouveau dossier  ainsi que de repérer le premier dossier 
        destination_file = '{}/{}'.format(frepertoire,i)

        with open(source_file, 'r') as f_source:
            with open(destination_file, 'w') as f_dest:     # Réecrit le contenu dans les nouveaux fichiers
                for line in f_source:
                    f_dest.write(line)

        


def cleaner(repertoire):
    ''' Permet de rendre les fichiers du répertoire exploitables. '''
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for j in range(len(fichiers)):
    
        L1 = []

        file  = open("{}\\{}".format(repertoire,fichiers[j]),"r",encoding="utf8")
        lines = file.readlines()
        for n, line in enumerate(lines) :
            L1.append(str(line).replace("\n", " "))
        file.close()
        for i in range(len(L1)):
            L1[i] = L1[i].replace("'", " ")
            L1[i] = L1[i].replace(".", "")
            L1[i] = L1[i].replace(",", "")
            L1[i] = L1[i].replace(";", "")
            L1[i] = L1[i].replace("!", "")
            L1[i] = L1[i].replace("?", "")
            L1[i] = L1[i].replace("-", " ")
            L1[i] = L1[i].lower()
        
        f = open("{}\\{}".format(repertoire,fichiers[j]),"w")
        for n, line in enumerate(lines) :
            f.write("{}\n".format(L1[n]))

        f.close() 
                    

        

