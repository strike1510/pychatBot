# Auteurs : Hugo Thouraud de Lavignére et Cheikh Tidiane Fall | My First Chat Bot 
# Ce fichier contient majoritairement le code pour la matrix TFIDF ainsi que des certaines fonctions qui y ont recours.
import os
import math
def tf(place,repertoire):
    ''' Calcul du Term-Frequency score avec place qui est le fichier et repertoire'''
    L1 = []

    file  = open("{}\\{}".format(place,repertoire),"r",encoding="utf8")
    lines = file.readlines()
    for n, line in enumerate(lines) :
        L1.append(str(line))
    file.close()

    L2 = []
    for i in range(len(L1)):
        L3 = L1[i].split()
        for j in range(len(L3)):
            L2.append(L3[j])
    
    words = L2
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts




def get_occurrences(chaine):
    ''' Permet d'avoir l'occurence d'un mot dans une chaine de caractères'''
    mots = chaine.split()
    occurrences = {}
    for mot in mots:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return occurrences


def get_idf_score(repertoire):
    ''' Permet d'obtenir le score idf d'un répertoire'''
    nb_documents = 0
    mots_documents = {}
    score_idf = {}
    
    for fichier in os.listdir(repertoire):
        nb_documents += 1
        with open(os.path.join(repertoire, fichier), 'r') as f:
            contenu = f.read()
            mots = contenu.split()
            for mot in set(mots):
                if mot in mots_documents:
                    mots_documents[mot] += 1
                else:
                    mots_documents[mot] = 1
    
    for mot, nb_occurrences in mots_documents.items():
        score_idf[mot] = math.log(nb_documents / nb_occurrences)
    
    return score_idf

def get_matrix_tf_idf(repertoire):
    ''' Calcul le score TF * IDF d'un répertoire'''
    matrice_tf_idf = []
    mots_uniques = set()
    nbfichier = 0
    for fichier in os.listdir(repertoire):
        nbfichier += 1
        with open(os.path.join(repertoire, fichier), 'r',encoding="utf8") as f:
            contenu = f.read()
            occurrences = get_occurrences(contenu)
            mots_uniques.update(occurrences.keys())
            matrice_tf_idf.append(occurrences)
    
    mots_uniques = sorted(list(mots_uniques))
    
    L2 = []
    for fichier in os.listdir(repertoire):
        L2.append(fichier)
    result = {}
    idfscore = get_idf_score(repertoire)
    for i in range(len(mots_uniques)):
        L20 = []
        for j in range(len(L2)):
            
            
            
            tfscore = tf(str(repertoire),str(L2[j]))
            
            if mots_uniques[i] in tfscore and mots_uniques[i] in idfscore.keys():
                L20.append(idfscore[mots_uniques[i]] * tfscore[mots_uniques[i]])
            else:
                L20.append(0.0)
        
        result[mots_uniques[i]] = L20
    return result







def less_important_word(repertoire):
    ''' Permet de trouver les mots les moins important du corpus'''
    fichiers = []
    motused = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    res = get_matrix_tf_idf(repertoire)
    for i in range(len(res)):
        for mot in res[i]:
            if res[i][mot] == 0:
                motused.append(mot)

    textoutput = "Les mots les moins important sont : {}".format(motused)
    return textoutput







def most_important_word(repertoire):
    ''' Permet de trouver les mots les plus important du corpus'''
    fichiers = []
    motused = "les"
    _y = 0
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    res = get_matrix_tf_idf(repertoire)
    for i in range(len(res)):
        for mot in res[i]:
            if res[i][mot] > res[_y][motused]:
                motused = mot
                _y = i

    textoutput = "Le mot le plus important est : {}".format(motused)
    return textoutput











def most_repeated_word(repertoire):
    ''' Permet de trouver les mots les plus répétés dans le corpus'''
    fichiers_chirac = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt") and "Chirac" in fichier:
            fichiers_chirac.append(fichier)
    for i in range(len(fichiers_chirac)):
        endroit = fichiers_chirac[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        L1.append(contenux)   
    
    max = 0
    for i in range(len(L1)):
        res = get_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if max <= res[mot]:
                max = res[mot]
                motofficiel = mot
    textoutput = "Le mot '{}' est répété {} fois chez Chirac".format(motofficiel,max)
    return textoutput
    




    


    

def president_says_word(repertoire):
    ''' Permet de trouver le président qui évoque le mot "nation" '''
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        contenux = contenux.replace("nations", "nation")
        L1.append(contenux)   
    
    max = 0
    savepres = 0
    for i in range(len(L1)):
        res = get_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if mot == "nation":
                if max <= res[mot]:
                    max = res[mot]
                    savepres = i 
        
    
    presi = fichiers[savepres]
    presi = presi.removeprefix("Nomination_").removesuffix(".txt")
    textoutput = "Le président '{}' est celui qui a cité le plus de fois le mot 'Nation' , il l'a répété {} fois".format(presi,max)
    return textoutput

def first_president_says_word(repertoire):
    ''' Permet de savoir quel président fu le premier à parler d'un sujet '''
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        contenux = contenux.replace("climats", "climat")
        contenux = contenux.replace("écologies", "écologie")
        contenux = contenux.replace("écologie", "climat")
        L1.append(contenux)   
    
    max = 0
    savepres = 0
    for i in range(len(L1)):
        res = get_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if mot == "climat":
                if max <= res[mot]:
                    max = res[mot]
                    savepres = i 
        
    
    presi = fichiers[savepres]
    presi = presi.removeprefix("Nomination_").removesuffix(".txt")
    textoutput = "Le président '{}' est celui qui parle le plus du climat / écologie , il l'a répété {} fois".format(presi,max)
    return textoutput

def globally_used_words(repertoire):
    ''' Permet de trouver les mots utilisées par tout les présidents '''
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        L1.append(contenux)   
    
    motscheck = True
    motsdit = []
    for i in range(len(L1)):
        res = get_occurrences(L1[i])
        
        for mot1 in res:
            for j in range(len(L1)):
                if j != len(L1)-1:
                    res = get_occurrences(L1[j+1])
                    
                    for mot2 in res:
                        if mot1 != mot2:
                            motscheck = False
                        else:
                            motscheck = True
                            break
                    if motscheck == False:
                        break
                    else:
                        if mot1 not in motsdit:
                            motsdit.append(mot1)
            if j == len(L1):
                if motscheck == True:
                    break

            #print(mot, res[mot])
        
    
    textoutput = "Tout les présidents on au moins cité 1 fois ces mots : {}".format(motsdit)
    return textoutput
