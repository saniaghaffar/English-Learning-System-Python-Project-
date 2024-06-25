print('-----------------------------------------------------------------')
print('------------------- \033[1m ENGLISH MANAGEMENT SYSTEM \033[0m------------------')
print('-----------------------------------------------------------------')
print('------------------Welcome to English Learning System-------------')

isLogin = False
while True :
    choice = input("Do you want to:\n1_Sign-up \n2_Log-in \n3_Exit \nEnter your Input : ")
    if choice=="1":
        username=input("Enter username:")
        password=input("Enter password:")
        password1 = input("Confirm password :")
        db=open("database.txt","r")
        d=[]
        f=[]
        for i in db:
            temp=i.split(",")
            a = temp[0]
            b=temp[1]
            d.append(a)
            f.append(b)

        if username in d:
            print("Sign up failed. Username already exist.")
        elif password!=password1:
            print("Confirmation failed")
        elif len(password)<=6:
             print("Password too short.Must contain 8 characters.")
        elif username in d:
            print("Username exists.")
        else:
            def Id():
                t=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
                r=""
                import random
                for i in range(5):
                    c=random.choice(t)
                    r+=c
                return r
            userId=Id()
            print("\r",end="")

            db=open("database.txt","a")
            db.write(username+","+password+","+userId+"\n")
            print("\033[1mSigning up successfully.\033[0m")
            isLogin = True
    elif choice=="2":
         db = open("database.txt", "r")
         username=input("Enter username :")
         password=input("Enter password :")
         Password=str(password)
         if not len(username or password)<1:
             d = []
             f = []
             for i in db:
                 temp = i.split(",")
                 a = temp[0]
                 b = temp[1]
                 d.append(a)
                 f.append(b)
             if username in d:
                 index=d.index(username)
                 s=f[index]
                 if Password==f[index]:
                     print("\033[1mLogin successful\033[0m")
                     userId = temp[2]
                     isLogin = True
                 else:
                     print("Worng Password")
             else:
                 print("User don't Exist")
         else:
             print("Login error")
    elif choice == '3':
        break
    while isLogin:
        import copy

        print('-----------------------------------------------------------------')
        print('           \033[1mFEAUTURES OF ENGLISH MANAGEMENT SYSTEM \033[0m')
        print('-----------------------------------------------------------------')
        print("1_Quiz\n"
              "2_Comprehesion\n"
              "3_Search\n"
              "4_Help\n"
              "5_Logout\n"
              "______________")
        choice = input("Enter your choice :")
        if choice == "1":
            print('-----------------------------------------------------------------')
            print('           \033[1m Quiz Management System \033[0m')
            print('-----------------------------------------------------------------')
            attempt = input("1_Vocabulory Quiz\n"
                            "2_Grammar Quiz \n"
                            "3_Others\n"
                            "_________________")
            if attempt == "1":
                print('-----------------------------------------------------------------')
                print('           \033[1m VOCABULORY QUIZ \033[0m')
                print('-----------------------------------------------------------------')
                Total_marks = 5
                Marks_Obtained = 0
                Correct_answers = 0
                Wrong_answers = 0
                import random

                Question = [("Choose the word that means to make less severe or intense:",
                             "a) Aggravate b) Exacerbate c) Alleviate d) Worsen", "c"),
                            ("Select the synonym for the word pervasive:",
                             "a) Limited b) Scattered c) Widespread d) Sparse", "c"),
                            ("Identify the correct definition of the word ephemeral:",
                             " a) Lasting a long time b) Temporary or short-lived c) Essential or crucial d) Steady or consistent",
                             "b"),
                            ("Choose the word that means to express approval or praise:",
                             "a) Denounce b) Condemn c) Commend d) Criticize", "c"),
                            ("Select the antonym for the word benevolent:",
                             "a) Malevolent b) Kind c) Generous d) Compassionate", "a"),
                            ("Choose the word that means to make larger in size or quantity:",
                             "a) Diminish b) Amplify c) Reduce d) Minimize", "b"),
                            ("Select the synonym for the word adept:", " a) Inept b) Skillful c) Clumsy d) Awkward",
                             "b"),
                            ("Identify the correct definition of the word abundant:",
                             " a) Rare or scarce b)Insufficient c)Plentiful or ample d)Empty or vacant", "c"),
                            ("Choose the word that means to free from blame or guilt:",
                             "a) Accuse b) Convict c) Exonerate d) Incriminate", "c"),
                            (
                            "Select the antonym for the word diligent:", " a) Lazy b) Indifferent c) Careless d) Slack",
                            "a")]
                qes = copy.copy(Question)
                for i in range(5):
                    dex = random.randrange(0, len(qes))
                    print(qes[dex][0])
                    print(qes[dex][1])
                    ans = input("Enter the suitable option:")
                    if ans == qes[dex][2]:
                        Correct_answers += 1
                        Marks_Obtained += 1
                    else:
                        Wrong_answers += 1
                        # Marks_Obtained -= 1
                    qes.remove(qes[dex])
                print('\n\033[1m     RESULT   \033[0m ')
                print('---------------------------------------')
                print("Your Obtained Marks are : ", Marks_Obtained)
                print("Correct Answers =", Correct_answers)
                print("Wrong Answers =", Wrong_answers)
            elif attempt == "2":
                print('-----------------------------------------------------------------')
                print('           \033[1m GRAMMAR QUIZ \033[0m')
                print('-----------------------------------------------------------------')
                Total_marks = 5
                Marks_Obtained = 0
                Correct_answers = 0
                Wrong_answers = 0
                import random

                Questions = [(
                             "Identify the correct form of the verb to complete the sentence: She _______ to the party yesterday.",
                             " a) Go b) Goes c) Went d) Gone", "c"),
                             ("Choose the correct pronoun to complete the sentence:_____ is my sister.",
                              " a) He  b) She c) They d) We", "b"),
                             ("Select the correct sentence structure:",
                              "a) The cat on the mat is sleeping. b) Is sleeping on the mat the cat. c) Sleeping on the mat is the cat. d) On the mat sleeping is the cat",
                              "a"),
                             (
                             "Identify the correct form of the adjective to complete the sentence:She is a _______ girl.",
                             " a) Beautifuller b) More beautiful c) Beautifullest d) Beautifuler", "b"),
                             (
                             "Choose the correct conjunction to complete the sentence: I studied hard _____ I passed the exam.",
                             " a) But b) Or c) And d) So", "d"),
                             (
                             "Identify the correct form of the verb to complete the sentence:They _______ playing soccer in the park.",
                             "a) is b) am c) are d) be", "c"),
                             (
                             "Choose the correct pronoun to complete the sentence:_____ is going to the movies tonight.",
                             "a) He b) She c) They d) We", "a"),
                             ("Select the correct sentence structure:",
                              " a) The book read John. b) Read the book John. c) The book John read. d) John read the book",
                              "d"),
                             (
                             "Identify the correct form of the adverb to complete the sentence:She sings _______ than her sister.",
                             "a) good b) better c) best d) well", "b"),
                             (
                             "Choose the correct preposition to complete the sentence:The cat jumped _______ the table.",
                             "a) at b) on c) in d) to", "b")]
                qes = copy.copy(Questions)
                for i in range(5):
                    dex = random.randrange(0, len(qes))
                    print(qes[dex][0])
                    print(qes[dex][1])
                    ans = input("Enter the suitable option:")
                    if ans == qes[dex][2]:
                        Correct_answers += 1
                        Marks_Obtained += 1
                    else:
                        Wrong_answers += 1
                        # Marks_Obtained -= 1
                    qes.remove(qes[dex])
                print('\n\033[1m     RESULT   \033[0m ')
                print('---------------------------------------')
                print("Your Obtained Marks are : ", Marks_Obtained)
                print("Correct Answers =", Correct_answers)
                print("Wrong Answers =", Wrong_answers)
            # if choice=="3":
            else:
                print('-----------------------------------------------------------------')
                print('           \033[1m RANDOM QUIZ TEST \033[0m')
                print('-----------------------------------------------------------------')
                Total_marks = 5
                Marks_Obtained = 0
                Correct_answers = 0
                Wrong_answers = 0
                import random

                Questions = [("Choose the correct spelling:", "a) Relevent b) Relevent c) Relevant d) Relevannt", "c"),
                             ("Select the correct spelling:", "a) Begginer b) Beginer c) Beginner d) Beginnne", "c"),
                             ("Identify the correct spelling:", "a) Consensus b) Consencus c) Concensus d) Consenkus",
                              "a"),
                             ("Choose the correct spelling:",
                              "a) Embarrassment b) Embarrasment c) Embarassment d) Embarrasement", "a"),
                             ("Which of the following is a proper noun?", "a) tree b) house c) London d) car", "c"),
                             ("Select the correct homophone for the word their:",
                              "a) there b) they're c) these d) thier", "a"),
                             ("Select the correct order of adjectives:",
                              "a) big, blue, round b) blue, round, big c) round, big, blue d) blue, big, round", "a"),
                             ("Identify the correct comparative form of the adjective good:",
                              "a) gooder b) goodest c) better d) more good", "c"),
                             ("Choose the correct possessive form of the noun child:",
                              "a) childs' b) child's c) childrens' d) children's", "d"),
                             (
                             "Choose the correct conjunction to complete the sentence:I have a headache _______ I didn't get enough sleep.",
                             "a) but b) and c) or d) so", "d")]
                qes = copy.copy(Questions)
                for i in range(5):
                    dex = random.randrange(0, len(qes))
                    print(qes[dex][0])
                    print(qes[dex][1])
                    ans = input("Enter the suitable option:")
                    if ans == qes[dex][2]:
                        Correct_answers += 1
                        Marks_Obtained += 1
                    else:
                        Wrong_answers += 1
                        # Marks_Obtained -= 1
                    qes.remove(qes[dex])
                print('\n\033[1m     RESULT   \033[0m ')
                print('---------------------------------------')
                print("Your Obtained Marks are : ", Marks_Obtained)
                print("Correct Answers =", Correct_answers)
                print("Wrong Answers =", Wrong_answers)
        if choice == "2":
            import random
            import time
            print("         \033[1m COMPREHENSION TEST \033[0m          ")

            print(
                "You will be given a comprehension paragraph and you to read it properly in a given time and have to answer the questions. Each question\n"
                "carries 1 mark and wrong answer will result in negative marking.\n"
                "_________________________________________________________________________________________________________________________________")
            time.sleep(1)
            paragraphs = [
                (
                    "In a small coastal village called Seashell Bay, a curious girl named Lily loved collecting seashells\n"
                    " on the sandy shores. One day, as she wandered along the beach, she noticed a glimmer in the distance\n."
                    " Intrigued, she hurried towards it and discovered a golden key half-buried in the sand. The key had an intricate\n"
                    " design and seemed to hold a secret. Lily's heart raced with excitement as she wondered what it could unlock.\n"
                    " She decided to keep the key safe and embarked on a quest to uncover its hidden treasure\n"
                    "_______________________________________________________________________________________________________________"),
                ("In a small village surrounded by lush meadows, a young girl named Lily discovered a magical rose.\n"
                 "The village was known for its beautiful gardens, but this rose was extraordinary. Its petals shimmered in\n"
                 " vibrant hues of pink and gold, casting a mesmerizing glow.Lily was captivated by the enchanting beauty of the rose.\n"
                 " She carefully tended to it, providing it with love and care. As the days passed, the rose blossomed even more,\n"
                 " spreading its intoxicating fragrance throughout the village.Word of the magical rose quickly spread,\n"
                 " attracting visitors from far and wide. They marveled at its ethereal charm and were filled with a sense of wonder.\n"
                 " The rose became a symbol of hope, bringing joy and happiness to all who beheld it.Lily's heart swelled with pride\n"
                 " as she witnessed the impact her discovery had on the village. She realized that even the simplest things, like a\n"
                 " flower, could hold immense beauty and power. The magical rose taught Lily and the villagers to appreciate the wonders\n"
                 "______________________________________________________________________________________________________________________"),
                (
                    "In a quiet village nestled by the rolling hills, a young girl named Mia stumbled upon a mysterious key while exploring\n"
                    " the ancient forest. The key was made of gleaming silver and had intricate engravings. With curiosity fueling her, Mia\n"
                    " embarked on a quest to uncover the key's purpose. She ventured through forgotten paths, deciphered cryptic clues, and\n"
                    " faced daunting challenges. Finally, after a relentless pursuit, Mia discovered a hidden door in an ancient ruin. With\n"
                    " trembling hands, she inserted the key into the lock, and the door swung open, revealing a long-lost treasure—a diary\n"
                    " filled with tales of forgotten legends and ancient wisdom. Mia's journey taught her the power of determination\n"
                    " and the rewards of unraveling hidden secrets\n"
                    "________________________________________________________________________________________________________________________")]
            quest = [(("Question 1:What was the name of the coastal village where Lily lived?",
                       "a) Ocean Bay  b) Sandcastle Village  c) Seashell Bay  d) Coral Cove", "c"),
                      ("Question 2:What did Lily find half-buried in the sand?",
                       "a) A golden seashell b) A message in a bottle c) A buried treasure chest d) A map to a hidden cave",
                       "a"),
                      ("Question 3:What did the golden key have?",
                       "a) An intricate design b) A tag with a secret code c) A hidden compartment d) A shiny gemstone",
                       "a"),
                      ("Question 4:How did Lily feel when she found the key?",
                       " a) Curious b) Disappointed c) Afraid d) Bored", "a"),
                      ("Question 5:Why did Lily embark on a quest?",
                       "a) To find more seashells b) To solve a mystery c) To become famous in the village d) To impress her friends",
                       "b")),
                     [("Question 1:What did Lily discover in the village?",
                       " a) A hidden treasure b) A magical rose c) A secret garden d) A talking animal", "b"),
                      ("Question 2:How did the petals of the magical rose appear?",
                       " a) Shimmering in vibrant hues b) Pure white and delicate c) Deep red and velvety d) Multicolored and striped",
                       "a"),
                      ("Question 3:How did Lily care for the magical rose?",
                       " a) Watering it daily b) Singing to it c) Providing sunlight d) All of the above", "d"),
                      ("Question 4:What effect did the magical rose have on the village?",
                       " a) It attracted visitors from far and wide. b) It caused a curse on the village. c) It made the villagers fall asleep.d) It brought storms and heavy rain",
                       "a"),
                      ("Question 5:What did the magical rose symbolize for the village?",
                       "a) Love and beauty b) Hope and joy c) Mystery and secrecy d) Danger and caution", "b")],
                     [("Question 1:What did Mia find while exploring the ancient forest?",
                       " a) A lost key b) A hidden treasure chest c) An ancient ruin d) A magical creature", "a"),
                      ("Question 2:How was the key described?",
                       " a) Made of gleaming silverb) Covered in ancient writings c) Engraved with cryptic symbols d) All of the above",
                       "d"),
                      ("Question 3:What motivated Mia to embark on a quest?",
                       "a) Curiosity b) Fear of missing out c) Greed for treasure d) Boredom", "a"),
                      ("Question 4:What did Mia discover behind the hidden door?",
                       "a) A hidden treasure b) A mystical creature c) A forgotten legend d) A long-lost diary", "a"),
                      ("Question 5:How did Mia feel when she found the hidden door?",
                       " a) Excited b) Scared c) Confused d) Indifferent", "a")]]
            # import random
            # import time

            comprehension = random.choice(paragraphs)
            print(comprehension)
            time.sleep(4)
            dex = paragraphs.index(comprehension)
            Total_marks = 5
            Marks_Obtained = 0
            Correct_answers = 0
            Wrong_answers = 0
            for i in range(5):
                print(quest[dex][i][0])
                print(quest[dex][i][1])
                ans = input("Enter the suitable option:")
                if ans == quest[dex][i][2]:
                    Correct_answers += 1
                    Marks_Obtained += 1
                else:
                    Wrong_answers += 1
                    Marks_Obtained -= 1
            print('\n\033[1m     RESULT   \033[0m ')
            print('---------------------------------------')
            print("Your Obtained Marks are : ", Marks_Obtained)
            print("Correct Answers =", Correct_answers)
            print("Wrong Answers =", Wrong_answers)
        if choice == "3":
            while True:
                choice = input("What do you want to search:\n"
                               "1_Antonyms\n"
                               "2_Synonyms\n"
                               "3_Grammar\n"
                               "___________")
                if choice == "1":
                    print ("\033[1m     ANTONYMS     \033[0m  ")
                    def search_word_in_file(filename, search_word):
                        try:
                            found = False
                            with open(filename, 'r') as file:
                                for line in file:
                                    if search_word in line:
                                        print(line.rstrip())
                                        found = True

                            if not found:
                                print(f"The word '{search_word}' does not exist in the file.")

                        except FileNotFoundError:
                            print(f"File '{filename}' not found.")
                        except IOError:
                            print(f"Error reading file '{filename}'.")
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")


                    filename = "antonym.txt"
                    search_word = input("Enter a word to search: ")

                    search_word_in_file(filename, search_word)
                    ask = input("Do you want to exit Y/N :")
                    if ask == "Y":
                        break
                if choice == "2":
                    print("\033[1m     SYNONYMS     \033[0m  ")
                    def search_word_in_file(filename, search_word):
                        try:
                            found = False
                            with open(filename, 'r') as file:
                                for line in file:
                                    if search_word in line:
                                        print(line.rstrip())
                                        found = True
                            if not found:
                                print(f"The word '{search_word}' does not exist in the file.")
                        except FileNotFoundError:
                            print(f"File '{filename}' not found.")
                        except IOError:
                            print(f"Error reading file '{filename}'.")
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")


                    filename = "synonym.txt"
                    search_word = input("Enter a word to search: ")
                    search_word_in_file(filename, search_word)
                    ask = input("Do you want to search more? Y/N :")
                    if ask == "Y":
                        continue
                    else:
                        break
                if choice == "3":
                    print("\033[1m     GRAMMAR     \033[0m  ")
                    def search_data(filename, search_name, limit):
                        try:
                            with open(filename, 'r') as file:
                                lines_found = 0
                                data_found = []
                                found_start = False
                                for line in file:
                                    if search_name.lower() in line.lower():
                                        found_start = True
                                    if found_start and lines_found < limit:
                                        data_found.append(line.strip())
                                        lines_found += 1
                                    if lines_found == limit:
                                        break
                                if lines_found > 0:
                                    return "\n".join(data_found)
                                else:
                                    return f"No data found for '{search_name}' in the file."
                        except FileNotFoundError:
                            return f"File '{filename}' not found."
                        except IOError:
                            return f"Error reading file '{filename}'."
                        except Exception as e:
                            return f"An error occurred: {str(e)}"


                    filename = "grammar.txt"
                    search_name = input("Enter the data you want to search?")
                    limit = 15

                    data = search_data(filename, search_name, limit)
                    print(data)
                    ask = input("Do you want to search more? Y/N :")
                    if ask == "Y":
                        continue
                    else:
                        break
        if choice == "4":
            print('\033[1m---------------------HELP--------------------------\033[0m')
            print(
                "The purpose of the app is to provide language instruction and support to individuals to improve their English proficiency.\n"
                "It offers structured quizes based on different domains to improve users vocabulary,grammar and much more. The user can also improve\n"
                "his English reading by solving comprehension in a given time. The app's goal is to equip students with necessary linguistic tools and\n"
                "cultural to effectively communcate in English across various context.\n")
        if choice == "5":
            logout = input("Are you sure you want to logout? Y/N :")
            if logout == "Y":
                print("Logging out successfully....")
                break
            else:
                continue