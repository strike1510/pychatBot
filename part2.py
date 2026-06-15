# Auteurs : Hugo Thouraud de Lavignére et Cheikh Tidiane Fall | My First Chat Bot 
# Ce fichier contient le code qui permet à l'utilisateur de poser des questions
import os, math
import TF
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
MotPoubelle = ["comment","quoi","pourquoi","dire","porte"]

def token(sentence):
    ''' Permet de tokenizer une phrase. La rendre utilisable par  code'''
    L = []
    n = ""
    for o in sentence.split(" "):
        if all(z not in punc for z in o):
            n += o + " "
    n = n.lower()
    L = n.split(" ")
    return L


def identify(sentence , repertoire):
    ''' Permet d'identify une phrase ou des mots de celles-ci au sein d'un repertoire contenant des fichiers texte '''
    listu = token(sentence)
    keep = []
    for fichier in os.listdir(repertoire):
        with open(os.path.join(repertoire, fichier), 'r') as f:
            contenu = f.read()
            mots = contenu.split()

    for word in listu:
        if word in mots and word not in keep:
            keep.append(word)
    return keep

def questtfidf(question):
    ''' Permet de trouver le score tfidf d'une question (Chaîne de caractères )'''

    quest = ""
    for e in token(question):
        quest += e + " "
    occMots = TF.get_occurrences(quest)
    result = TF.get_idf_score("cleaned")
    L = {}
    for i in result.keys():
        if i in occMots:
            x = result[i] * occMots[i]
            L[i] = x
        else:
            result[i] = 0
    return L

def Revelant_word(question):
    ''' Permet de trouver le mot le plus pertinent dans la question par rapport à une liste mot poubelle initialisée en dur plus tôt'''
    dicquest = questtfidf(question)
    max = 0
    word = ""
    for i in dicquest:
        if i not in MotPoubelle:
            if max <= dicquest[i]:
                max = dicquest[i]
                word = i
    return word

def Revelant_word_file(word):
    ''' Permet de trouver le mot le plus pertinent par rapport au fichiers du corpus '''
    fichiers = []
    for fichier in os.listdir("cleaned"):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    dico = TF.get_matrix_tf_idf("cleaned")
    nomfichier = ""
    max = 0
    for i in range(len(fichiers)):
        if dico[word][i] > max:
            max = dico[word][i]
            nomfichier = fichiers[i]
    return nomfichier

def reponseViaFile(word):
    ''' Constitue une partie du systéme de réponse. permet d'y intégrer le mot pertinent'''
    file = Revelant_word_file(word)
    L1 = []

    file  = open("cleaned\{}".format(file),"r",encoding="utf8")
    lines = file.readlines()
    for n, line in enumerate(lines) :
        L1.append(str(line).replace("\n", " "))
    file.close()
    reponse = ""
    for i in range(len(L1)):
        if word in L1[i]:
            reponse = L1[i]
            break
    
    reponse = reponse.replace(" l ", " l'")
    reponse = reponse.replace(" c ", " c'")
    reponse = reponse.replace(" s ", " s'")
    return reponse

def generationentry(question):
    ''' Constitue l'autre partie du systéme de réponse. Permet de choisir l'expression avec laquelle le bot va répondre'''
    question = question.replace("'", " ")
    question = question.replace(".", "")
    question = question.replace(",", "")
    question = question.replace(";", "")
    question = question.replace("!", "")
    question = question.replace("?", "")
    question = question.replace("-", " ")
    question = question.lower()
    question_starters = {
 "comment": "Après analyse,",
 "pourquoi": "Car,",
 "peux tu": "Oui, bien sûr!",
}
    for i in question_starters:
        if i in question:
            return question_starters[i]
        else:
            return "Voici une réponse qui pourrait vous aider"
            