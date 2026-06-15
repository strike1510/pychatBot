# Auteurs : Hugo Thouraud de Lavignére et Cheikh Tidiane Fall | My First Chat Bot 
# Ce fichier contient le code de l'interface utilisateur
import base_fonctions, TF, part2
repertoire = "speeches"
def main_menu():
    ''' Constitue le Menu.'''
    part = int(input("Nous utiliserons la partie (1/2) "))
    while part < 1 or part > 2:
        part = int(input("Nous utiliserons la partie (1/2) "))

    if part == 1:

        print("== Menu Principal ==|\n")
        print("Que souhaitez vous faire ? (Saisir le nombre entre parenthèse)") 
        print("- Pour clean le speeches (0)")
        print("- Voir le TF (1)")
        print("- Voir l'IDF (2)")
        print("- Voir le TF-IDF (3)")
        print("- Afficher la liste des mots les moins importants dans le corpus de documents (4)")
        print("- Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé (5)")
        print("- Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac (6)")
        print("- Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois (7)")
        print("- Indiquer le premier président à parler du climat et/ou de l’écologie (8)")
        print("- Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués (9)")
        print("- Pour afficher la liste des noms et prénoms des présidents (10)")
        print("- Pour extraire les noms des présidents à partir des noms des fichiers texte fournis (11)")
        print("généralement il faut écrire 'cleaned' pour les répértoires *")

        ask = int(input("Saisie : "))
        while ask > 11 or ask < 0:
            ask = int(input("Saisie : "))

        if ask == 0:
            x = str(input("Saisir le nom du répértoire à copier : "))
            y = str(input("Saisir le nom du répértoire à coller : "))
            base_fonctions.transition(x,y)
            base_fonctions.cleaner(y)
            print("Les speeches sont nétoyés !")
        elif ask == 1:
            x = str(input("Saisir le nom du fichier (avec le .txt) "))
            print(TF.tf("speeches",x))
        elif ask == 2:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.get_idf_score(x))
        elif ask == 3:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.get_matrix_tf_idf(x))
        elif ask == 4:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.less_important_word(x))
        elif ask == 5:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.most_important_word(x))
        elif ask == 6:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.most_repeated_word(x))
        elif ask == 7:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.president_says_word(x))
        elif ask == 8:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.first_president_says_word(x))
        elif ask == 9:
            x = str(input("Saisir le nom du répértoire "))
            print(TF.globally_used_words(x))
        elif ask == 10:
            x = str(input("Saisir le nom du répértoire "))
            base_fonctions.names_f(x)
        elif ask == 11:
            x = str(input("Saisir le nom du répértoire "))
            base_fonctions.extract_names(x)
        
        else:
            print("erreur, veuillez relancer le programme..")

    elif part == 2:
        question = str(input("Quelle est votre question ? "))
        word = part2.Revelant_word(question)
        print("Document pertinent retourné :",part2.Revelant_word_file(word))
        print("Mot ayant le TF-IDF le plus élevé :",word)
        print("La réponse générée :",part2.reponseViaFile(word))
        print("\n\nRéponse final:\n","{} {}.".format(part2.generationentry(question),part2.reponseViaFile(word)))

    o = str(input("Voulez-vous effectuer une autre opération ? Oui ou Non : "))
    if o == "Oui":
        main_menu()
    elif o == "Non":
        print("Trés bien.")

main_menu()