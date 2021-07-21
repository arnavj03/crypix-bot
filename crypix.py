#-----------------------------------------------------(SOME IMP MODULES USED, covid and youtube_dl are third party modules not built-in)------------------------------
import sys
import os
import youtube_dl
from covid import Covid
import time
#-----------------------------------------------------(LOG IN AND UP CODE)--------------------------------------------------------------------------------------------
def signup():
    print("Let's sign up then. It's really easy! It Will take two steps")
    input("Press Enter to continue...")
    print("              ##############################")
    time.sleep(0.5)
    print("              #          SIGN UP           #")
    time.sleep(0.5)
    print("              ##############################")
    time.sleep(0.5)
    print("-")
    print("-")
    print("-")
    print('-')
    info=open("info.txt","w")
    username=input("ENTER USERNAME:")
    password=input("ENTER PASSWORD:")
    info.write(username)
    info.write(password)
    print("please wait")
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("writing database")
    time.sleep(2)
    os.system("cls")
    print('                    REGISTRATION SUCCESSFULL!                      ')
    input("Press enter to login ")
    info.close()
    os.system("cls")
    signin()
    
def signin():
    print("              ##############################")
    time.sleep(0.5)
    print("              #        LOGIN BELOW         #")
    time.sleep(0.5)
    print("              ##############################")
    print("-")
    time.sleep(0.5)
    print("-")
    print('-')
    info=open("info.txt","r")
    f=info.read()
    time.sleep(0.5)
    l=input("ENTER  USERNAME: ")
    time.sleep(0.5)
    s=input("ENTER  PASSWORD: ")
    if f==l+s:
        print("gathering user info....")
        time.sleep(0.5)
        print("connecting....")
        time.sleep(3)
        print(" ")
        print("  ")
        os.system("cls")
        print("""
                             _  __   ___       __    __ __ __ __ __ __         
                         |  / \/__    | |\|   (_ | |/  /  |_ (_ (_ |_ | ||  |  
                         |__\_/\_|   _|_| |   __)|_|\__\__|____)__)|  |_||__|__
                                   """)
        print(" ")
        input("Press enter to continue")
        os.system("cls")
        menu()
    else:
        print("The username or password you entered is wrong!")
        input("Press enter to try again...")
        os.system("cls")
        signin()
    info.close()
#-----------------------------------------------------(LOG IN AND UP CODE END)--------------------------------------------------------------------------------------------

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------(MENU CODE)-----------------------------------------------------------------------------------------       
def menu():
    print(""" 
  __  __ _____ _   _ _   _ 
 |  \/  | ____| \ | | | | |
 | |\/| |  _| |  \| | | | |
 | |  | | |___| |\  | |_| |
 |_|  |_|_____|_| \_|\___/ 
                           
             """)
    print("-")
    print("-")
    print("-")
    print('-')
    print()

    choice = input("""
                      A: COVID19 LIVE UPDATES
                      B: FORBES TOP 10
                      C: FITNESS ZONE
                      D: YOUTUBE VIDEO DOWNLOADER
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        os.system("cls")
        covidlive()
    elif choice == "B" or choice =="b":
        os.system("cls")
        print("""
  _____ ___  ____  ____  _____ ____    _____ ___  ____    _  ___  
 |  ___/ _ \|  _ \| __ )| ____/ ___|  |_   _/ _ \|  _ \  / |/ _ \ 
 | |_ | | | | |_) |  _ \|  _| \___ \    | || | | | |_) | | | | | |
 |  _|| |_| |  _ <| |_) | |___ ___) |   | || |_| |  __/  | | |_| |
 |_|   \___/|_| \_\____/|_____|____/    |_| \___/|_|     |_|\___/ 
                                                                  
""")
        forbes()
    elif choice=="C" or choice=="c":
        os.system("cls")
        fitneszone()
    elif choice == "D" or choice == "d":
        os.system("cls")
        youtube()
    elif choice=="Q" or choice=="q":
        quit()
    else:
        os.system("cls")
        print("You must only select either A,B or Q.")
        print("Please try again")
        menu()
#--------------------------------------------------------------(MENU CODE ENDS)-------------------------------------------------------------------------------------
        
#--------------------------------------------------------------(COVID PROGRAM STARTS)--------------------------------------------------------------------------------
def covidlive():
    print (""" 
   ____ _____     _____ ____        _  ___  
  / ___/ _ \ \   / /_ _|  _ \      / |/ _ \ 
 | |  | | | \ \ / / | || | | |_____| | (_) |
 | |__| |_| |\ V /  | || |_| |_____| |\__, |
  \____\___/  \_/  |___|____/      |_|  /_/ 
                                            
""")
    print("-")
    time.sleep(1)

    choice = input("""
                      A: About Corona Virus 
                      B: Symptoms
                      C: Preventions
                      D: Check if you are in danger of contracting the virus
                      E: COVID19 Live Counter
                      Q: Back to Menu

                      Please enter your choice: """)
    os.system("cls")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

    if choice == "A" or choice =="a":
        print("                    ##############################")
        print("                    #        ABOUT CORONA        #")
        print("                    ##############################")
        history= """
                  * Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds.
                  
                  * In humans, these viruses cause respiratory tract infections that can range from mild to lethal.
                  
                  * The name "coronavirus" is derived from Latin, meaning "crown" or "wreath".
                  
                  * Coronaviruses were first discovered in the 1930s when an acute respiratory infection of domesticated chickens was shown to be caused by
                    infectious bronchitis virus.
                    Human coronaviruses were discovered in the 1960s.
                    
                  * Coronaviruses are large, roughly spherical particles with bulbous surface projections.

                  * COVID-19 is thought to spread mainly through close contact from person-to-person. """
        print(history)
        input("Press enter to return to menu")
        os.system("cls")
        covidlive()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif choice == "B" or choice =="b":
         print("                    ##############################")
         print("                    #        SYMPTOMS            #")
         print("                    ##############################")
         print("-")
         print("-")
         print("-")
         print('-')
         symptoms= '''                  Symptoms include:

                      * fever
                      * dry cough
                      * tiredness
                      * aches and pains
                      * sore throat
                      * diarrhoea
                      * conjunctivitis
                      * headache
                      * loss of taste or smell
                      * a rash on skin, or discolouration of fingers or toes
                      * difficulty breathing or shortness of breath
                      * chest pain or pressure
                      * loss of speech or movement

                      Seek immediate medical attention if you have serious symptoms.
                      Always call before visiting your doctor or health facility.
                      Call Ministry of Health Helpline: 24441999
                      '''
         print(symptoms)
         input("Press enter to return to menu")
         os.system("cls")
         covidlive()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif choice == "C" or choice == "c":
         print("                    ##############################")
         print("                    #        PREVENTIONS         #")
         print("                    ##############################")
         print("-")
         print("-")
         print("-")
         print('-')
         preventions= '''
            Few Precautions:

                        * Clean your hands often. Use soap and water, or an alcohol-based hand rub.
                        * Maintain a safe distance from anyone who is coughing or sneezing.
                        * Wear a mask when physical distancing is not possible.
                        * Don’t touch your eyes, nose or mouth.
                        * Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
                        * Stay home if you feel unwell.
                        * If you have a fever, cough and difficulty breathing, seek medical attention.

                        * Masks: - Masks can help prevent the spread of the virus from the person wearing the mask to others.
                                 - Masks alone do not protect against COVID-19, and should be combined with physical distancing and hand hygiene.
                    '''
         print(preventions)
         input("Press enter to return to menu")
         os.system("cls")
         covidlive()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif choice=="D" or choice=="d":
        logo()
        questions()
        input("press enter to return to menu")
        os.system("cls")
        covidlive()
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif choice=="E" or choice=="e":
        logo1()
        print("-")
        print("-")
        print("1-India")
        print("2-Oman")
        put=input("Enter your option:")
        os.system("cls")
        if put=="1":
            india()
        if put=="2":
            oman()
        input("press enter to continue...")
        os.system("cls")
        covidlive()
    elif choice=="q" or choice=="Q":
        menu()
    else:
        print("ONE JOB YOU HAD TO ENTER THE CORRECT OPTION !.... ENTER AGAIN NOW")
        print(".")
        covidlive()
#----------------------------------------------------------------(COVID PROGRAM ENDS)---------------------------------------------------------------------------------

#-----------------------------------------------------(FITNESS ZONE CODE STARTS)-------------------------------------------------------------------------------------
def fitneszone():
    print (""" 
  _____ ___ _____ _   _ _____ ____ ____    ________  _   _ _____ 
 |  ___|_ _|_   _| \ | | ____/ ___/ ___|  |__  / _ \| \ | | ____|
 | |_   | |  | | |  \| |  _| \___ \___ \    / / | | |  \| |  _|  
 |  _|  | |  | | | |\  | |___ ___) |__) |  / /| |_| | |\  | |___ 
 |_|   |___| |_| |_| \_|_____|____/____/  /____\___/|_| \_|_____|
                                                                 
                           """)

    choice = input("""
                      A: Workout tasks 
                      B: Check your BMI here !
                      C: Best music to listen during workout !
                      Q: Back to Menu

                      Please enter your choice: """)
    os.system("cls")

    if choice == "A" or choice =="a":
        os.system("cls")
        exercise()
    elif choice == "B" or choice =="b":
        os.system("cls")
        bmii()
        fitneszone()
    elif choice=="C" or choice=="c":
        os.system("cls")
        workoutmusic()
    elif choice=="Q" or choice=="q":
        menu()
    else:
        print("You must only select either A,B or Q.")
        print("Please try again")
        fitneszone()

#-----------------------------------------------------(FITNESS ZONE CODE ENDS)--------------------------------------------------------------------------------------    
def quit():
    print("YOU ARE NOW QUITTING.........:")
    time.sleep(3)
    sys.exit
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    
#---------------------------------------------------------------COVID19 STUFF------------------------------------------------------------------------------------------
def logo():
    print("############################################")
    print("#      CHECK IF YOU HAVE CORONAVIRUS !     #")
    print("############################################")
    print("-")
    print("-")
    print("-")
    print("-")

def questions():
    name=input("Enter your name:")
    os.system("cls")
    age=input("Enter your age : ")
    os.system("cls")
    gender=input("Enter your gender:")
    os.system("cls")
    print("ARE YOU EXPERIENCING THE FOLLOWING SYMPTOMS?")
    print("1- Cough")
    print("2- Fever")
    print("3- Difficulty in Breathing")
    print("4- None of these")
    symp=input("Enter your option:")
    os.system("cls")
    print("Have you ever had any of the following ?")
    print("1-Hypertension")
    print("2-Diabetes")
    print("3-Lung Disease")
    print("4-Heart Disese")
    print("5-none of these")
    lolm=input("Enter your option:")
    os.system("cls")
    print("Are you  experiencing any type of body pain?")
    print("1-yes")
    print("2-no")
    back=input("Enter your option")
    os.system("cls")
    travel=input("Have you travelled internationally in the last 14 days ? (y/n)")
    os.system("cls")
    print("Have you recently interacted with a person infected with covid-19 ?")
    print("1-yes")
    print("2-no")
    inter=input("Enter your option")
    os.system("cls")
    print("Are you a social worker like a doctor , police etc ?")
    print("1-yes")
    print("2-no")
    yes=input("Enter your option :")
    os.system("cls")
    print("Have you been to any of these in the last 7 days?")
    print("1-Mall")
    print("2-Hypermarket")
    print("3-Hospital")
    print("4-any other place where there are a lot of people")
    print("5-none of these")
    have=input("Enter your options:")
    os.system("cls")
    n=0
    if symp== "1" or symp=="2" or symp=="3":
        n=n+1
    if lolm== "1" or lolm=="2" or lolm=="3" or lolm=="4":
        n=n+1
    if back=="1":
        n=n+1
    if travel=="y":
        n=n+1
    if inter=="1":
        n=n+1
    if age>"50":
        n=n+1
    if age<"10":
        n=n+1
    if yes=="1":
        n=n+1
    if have=="1" or have=="2" or have=="3" or have=="4":
        n=n+1
        
    if  n==7:
        print("YOU ARE AT HIGH RISK ! PLEASE MEET A DOCTOR AS SOON AS POSSIBLE ! ")
        input("Press enter to see what you should do")
        os.system("cls")
        print("YOU SHOULD SEE A DOCTOR AS SOON AS POSSIBLE . DONT PANIC ! WE CAN EVEN BE WRONG !")
        print("MAKE SURE TO WEAR MASKS AND GLOVES EVERYWHERE AND ALSO DONT CONTACT WITH OTHERS .")
        print("ITS NOT ONLY HARMFUL FOR YOU BUT ALSO THE PERSON WITH WHOM UR CONTACTING !")
        input("press enter to continue")
    elif n==6:
        print("YOU ARE AT HIGH RISK ! PLEASE MEET A DOCTOR AS SOON AS POSSIBLE ! ")
        input("Press enter to see what you should do")
        os.system("cls")
        print("YOU SHOULD SEE A DOCTOR AS SOON AS POSSIBLE . DONT PANIC ! WE CAN EVEN BE WRONG !")
        print("MAKE SURE TO WEAR MASKS AND GLOVES EVERYWHERE AND ALSO DONT CONTACT WITH OTHERS .")
        print("ITS NOT ONLY HARMFUL FOR YOU BUT ALSO THE PERSON WITH WHOM UR CONTACTING !")
        input("press enter to continue")
    elif n==5:
       print("YOU ARE AT HIGH RISK ! PLEASE MEET A DOCTOR AS SOON AS POSSIBLE ! ")
       input("Press enter to see what you should do")
       os.system("cls")
       print("YOU SHOULD SEE A DOCTOR AS SOON AS POSSIBLE . DONT PANIC ! WE CAN EVEN BE WRONG !")
       print("MAKE SURE TO WEAR MASKS AND GLOVES EVERYWHERE AND ALSO DONT CONTACT WITH OTHERS .")
       print("ITS NOT ONLY HARMFUL FOR YOU BUT ALSO THE PERSON WITH WHOM UR CONTACTING !")
    elif n==4:
        print("YOU ARE AT LOW RISK BUT THERE ARE SYMPTOMS OF CORONAVIRUS ! ")
    elif n==3: 
        print("YOU ARE AT LOW RISK " )
    elif n==2: 
        print("YOU ARE FINE ! MIGHT BE A COMMON FLU OR SMTHING SO JUST CHILL ! " )
    elif n==1:
        print("YOU ARE FINE ! MIGHT BE A COMMON FLU OR SMTHING SO JUST CHILL !")
    else:
        print("WHY DID U USE ME THEN ?")
#----------------------------------------------------------------ends here------------------------------------------------------------------------------------------


#---------------------------------------------------------------YOUTUBE DOWNLOADER STARTS---------------------------------------------------------------------------        
def youtube():
    ydl_opts = {}
    def dwl_vid():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([zxt]) 
    channel = 1
    while (channel == int(1)):
       link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") 
       zxt = link_of_the_video.strip()

       dwl_vid()
       
       channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))
       os.system("cls")
       menu()
#---------------------------------------------------------------YOUTUBE DOWNLOADER ENDS---------------------------------------------------------------------------        


#-----------------------------------------------------------------COVID LIVE CODING-----------------------------------------------------------------------------------
def oman():
    covid = Covid() 
    Oman = covid.get_status_by_country_name("Oman")
    data ={ 
         key:Oman[key] 
         for key in Oman.keys()and {'confirmed',  
                                 'active', 
                                 'deaths', 
                                 'recovered'} 
    } 
  

    for key, value in data.items():
        print(key, ' : ', value)
    

def india():
    covid = Covid() 
    india = covid.get_status_by_country_name("india")
    data ={ 
         key:india[key] 
         for key in india.keys()and {'confirmed',  
                                 'active', 
                                 'deaths', 
                                 'recovered'} 
    } 
  

    for key, value in data.items():
        print(key, ' : ', value)

def logo1():
    print("#########################################")
    print("#         COVID LIVE STATUS             #")
    print("#########################################")
#-----------------------------------------------------------------COVID LIVE CODING ENDS-----------------------------------------------------------------------------------

#-------------------------------------------------------------FITNESS ZONE FUNCTIONS START----------------------------------------------------------------------------
def bmii():
    name=input("Enter your name")
    height = float(input("Input your height in meters: "))
    os.system("cls")
    weight = float(input("Input your weight in kilogram: "))
    os.system("cls")
    bmi= round(weight / (height * height), 2)
    print("Your BMI is",bmi)
    print("-")
    print('-')
    print("-")
    if bmi <18.5:
        print("You are UNDERWEIGHT!!..Start eating mate")
        input("press enter to continure")
        os.system("cls")
    elif 18.5<bmi<24.9:
        print("You are HEALTHY!")
        input("press enter to continure")
        os.system("cls")
    elif 25<bmi<29.9:
        print("You are OVERWEIGHT")
        input("press enter to continure")
        os.system("cls")
    elif bmi>30:
        print("You are OBESE!! Start running or something mate")
        input("press enter to continure")
        os.system("cls")
    else:
        print("One job you had to enter the information correctly")
        input("press enter to continure")
        os.system("cls")

def workoutmusic():
    print("THESE ARE SOME OF THE BEST WORKOUT SONGS WHILE WORKING OUT...")
    print("-")
    print("-")
    time.sleep(1.5)
    print("""              You Shook Me All Night Long — AC/DC JAM

              Take Over Control — Afrojack (feat. Eva Simons)
              
              Addicted to You (David Guetta Remix) — Avicii
              
              Wake Me Up — Avicii
              
              212 — Azealia Banks, Lazy Jay
              
              Harlem Shake — Baauer
              
              Brass Monkey — Beastie Boys
              
              Drunk in Love — Beyonce and JAY Z
              
              Locked Out of Heaven (Sultan + Shepard Remix) — Bruno Mars

              Treasure — Bruno Mars

              Put Your Hands Where My Eyes Could See — Busta Rhymes

              I Need Your Love — Calvin Harris (feat. Ellie Goulding)


              Let’s Go (Radio Edit) — Calvin Harris and Ne-Yo

              Summer — Calvin Harris 
          """)
    input("press enter to return to menu")
    os.system("cls")
    fitneszone()

def exercise():
    day=input("Which day is it today?")
    if day=="Sunday" or day=="sunday":
        input("Today you have to do four exercises...press enter to see them...")
        print("#1-- WARM-UP ")
        print("-")
        print("DURATION :  5 minutes ")
        print("-")
        print("DESCRIPTION  -- Warm-up is essential before doing a workout as warm-up helps to increase the blood flow to the muscles. ")
        input("Press enter to begin with your first exercise...")
        print("#2-- SQUATS")
        print("-")
        print("DURATION :  5 minutes-(3 sets)  ")
        print("-")
        print("DESCRIPTION  --  Squats help to strengthen the muscles of your lower body.")
        input("Press enter to begin with your second exercise...")
        print("#3-- LUNGES")
        print("-")
        print("DURATION :  5 minutes- 2 sets (each leg) ")
        print("-")
        print("DESCRIPTION -- A proper lunge posture can help you achieve a stronger and more stable core. This workout engages your core and abdominal muscles.")
        input("Press enter to begin with your third exercise...")
        print("#3-- WALL SIT ")
        print("-")
        print("DURATION :  1 minute (3 sets) ")
        print("-")
        print("DESCRIPTION  --  Wall sitting primarily builds isometric strength and endurance in glutes, calves, quadriceps, hamstrings, and adductor muscles.")
        input("Press enter to begin with your fourth exercise...")
        print("#4-- HAMSTRING CURLS ")
        print("-")
        print("DURATION :  2 minutes (each leg) ")
        print("-")
        print("DESCRIPTION  --  Hamstring curls helps to strengthen your hamstring and glutes.")
        print("Congratulations! You have completed today's workout.")
        input("Press enter to return back")
        os.system("cls")
        fitneszone()

    elif day == "monday" or day=="Monday":
        input("Take some rest today after your high intensity workout yesterday....Today, you can try meditating instead...")
        print('Mindfulness training improves your ability to maintain attention and regulate emotional distraction.')
        input("Press enter to return back")
        os.system("cls")
        fitneszone()


    elif day=="Tuesday" or day=="tuesday":
        input("Today you have to do four exercises...press enter to see them...")
        print("#1-- WARM-UP ")
        print("-")
        print("DURATION :  5 minutes ")
        print("-")
        print("DESCRIPTION  -- Warm-up is essential before doing a workout as warm-up helps to increase the blood flow to the muscles. ")
        input("Press enter to begin with your first exercise...")
        print("#2-- PUSHUPS")
        print("-")
        print("DURATION :  15 minutes")
        print("-")
        print("DESCRIPTION  --  Pushups are beneficial for building upper body strength. They work the triceps, pectoral muscles, and shoulders.")
        input("Press enter to begin with your second exercise...")
        print("#3-- SQUAT PRESS")
        print("-")
        print("DURATION :  10 minutes")
        print("-")
        print("DESCRIPTION -- The squat press is an excellent addition to your upper body workout routine because it works your shoulders, back and core and gets your heart rate up!")
        input("Press enter to begin with your third exercise...")
        print("#3-- BURPEES")
        print("-")
        print("DURATION :  1 minute-(3 sets) ")
        print("-")
        print("DESCRIPTION  --  Burpees is the most effective exercise to lose belly fat.")
        input("Press enter to begin with your fourth exercise...")
        print("#4-- CRUNCHES ")
        print("-")
        print("DURATION :  5 minutes")
        print("-")
        print("DESCRIPTION  --  Crunches are designed to tone the core muscles of the body. The exercise aids in strengthening the core muscles, improving the posture, and increasing the mobility and flexibility of the muscles.")
        print("Congratulations! You have completed today's workout.")
        input("Press enter to return back")
        os.system("cls")
        fitneszone()


    elif day == "wednesday" or day=="wednesday":
        input("Take some rest today after your high intensity workout yesterday....Today, you can try meditating instead...")
        print('Mindfulness training improves your ability to maintain attention and regulate emotional distraction.')
        input("Press enter to return back")
        os.system("cls")
        fitneszone()


    elif day=="Thursday" or day=="thursday":
        input("Today you have to do four exercises...press enter to see them...")
        print("#1-- WARM-UP ")
        print("-")
        print("DURATION :  5 minutes ")
        print("-")
        print("DESCRIPTION  -- Warm-up is essential before doing a workout as warm-up helps to increase the blood flow to the muscles. ")
        input("Press enter to begin with your first exercise...")
        print("#2-- SHOULDER SHRUGS")
        print("-")
        print("DURATION :  5 minutes-(3 sets)")
        print("-")
        print("DESCRIPTION  --  This workout helps to boost the strength of your shoulder, neck, or upper back muscles,also improving your posture.")
        input("Press enter to begin with your second exercise...")
        print("#3-- OVERHEAD PRESSES")
        print("-")
        print("DURATION :  10 minutes-(3 sets) ")
        print("-")
        print("DESCRIPTION -- This workout helps to strengthen the shoulder and triceps muscles.")
        input("Press enter to begin with your third exercise...")
        print("#3-- DEADLIFT")
        print("-")
        print("DURATION :  1 minute-(3 sets) ")
        print("-")
        print("DESCRIPTION  --  Burpees is the most effective exercise to lose belly fat.")
        input("Press enter to begin with your fourth exercise...")
        print("#4-- CRUNCHES ")
        print("-")
        print("DURATION :  10 minutes-(3 sets) ")
        print("-")
        print("DESCRIPTION  --  Incorporating deadlifts one or two days a week into a weight training session will develop strength in the hamstrings, glutes, low back, and upper back. They also rely on core strength to stabilize your body throughout the lift, which means you'll be working your abs on top of everything else.")
        print("Congratulations! You have completed today's workout.")
        input("Press enter to return back")
        os.system("cls")
        fitneszone()


    elif day=="friday" or day=="Friday" or day=="saturday" or day=="Saturday":
        print("You have no workouts planned today...Enjoy!")
        input("Press enter to return back")
        os.system("cls")
        fitneszone()


    else:
        print("Please enter the name of the day correctly.")
        exercise()

#---------------------------------------------------------------------------(FITNESS ZONE FUNCTIONS END)--------------------------------------------------------------

#----------------------------------------------------------------(FORBES STARTS)-------------------------------------------------------------------------------------
def forbes():
    print(" 1) THE WORLDS MOST POWERFULL PEOPLE ")
    print(" 2) TOP 10 COMPANIES ")
    print(" 3) INDIA'S RICHEST PEOPLE ")
    print(" 4) MOST INNOVATIVE COMPANIES ")
    print(" 5) FORBES 30 UNDER 30 : GAMING ")
    print(" 6) FORBES 30 UNDER 30 : SCIENCE ")
    
    f=input("""Enter The number whose info you want to get :

    To return to menu enter "q" or "Q" : 
""")
    if f=="q" or f=="Q":
        os.system("cls")
        menu()
    if f=="1":
        os.system("cls")
        print("""
 __      _____  ___ _    ___  ___   __  __  ___  ___ _____   ___  _____      _____ ___ ___ _   _ _    _      ___ ___ ___  ___ _    ___  
 \ \    / / _ \| _ \ |  |   \/ __| |  \/  |/ _ \/ __|_   _| | _ \/ _ \ \    / / __| _ \ __| | | | |  | |    | _ \ __/ _ \| _ \ |  | __| 
  \ \/\/ / (_) |   / |__| |) \__ \ | |\/| | (_) \__ \ | |   |  _/ (_) \ \/\/ /| _||   / _|| |_| | |__| |__  |  _/ _| (_) |  _/ |__| _|  
   \_/\_/ \___/|_|_\____|___/|___/ |_|  |_|\___/|___/ |_|   |_|  \___/ \_/\_/ |___|_|_\_|  \___/|____|____| |_| |___\___/|_| |____|___| 
                                                                                                                                    
                                                                                                                                                                                                                                                          
                       """)
        time.sleep(2)
        print(" #1 Xi Jinping")
        time.sleep(0.5)
        print("   China   ")
        print(" ")
        time.sleep(1)
        print(" #2 Vladimir Putin")
        time.sleep(0.5)
        print("   Russia   ")
        print(" ")
        time.sleep(1)
        print(" #3  Donald Trump")
        time.sleep(0.5)
        print("   United States   ")
        print(" ")
        time.sleep(1)
        print(" #4  Angela Merkel")
        time.sleep(0.5)
        print("   Germany   ")
        print(" ")
        time.sleep(1)
        print(" #5  Jeff Bezos")
        time.sleep(0.5)
        print("   Amazon   ")
        print(" ")
        time.sleep(1)
        print(" #6  Pope Francis")
        time.sleep(0.5)
        print("   Roman Catholic church   ")
        print(" ")
        time.sleep(1)
        print(" #7  Bill Gates")
        time.sleep(0.5)
        print("   Bill & Melinda Gates foundation   ")
        print(" ")
        time.sleep(1)
        print(" #8  Mohammed Bin Salman Al Saud")
        time.sleep(0.5)
        print("   Saudi Arabia   ")
        print(" ")
        time.sleep(1)
        print(" #9  Narendra Modi")
        time.sleep(0.5)
        print("   India   ")
        print(" ")
        time.sleep(1)
        print(" #10 Larry Page")
        time.sleep(0.5)
        print("   Alphabet   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()

    elif f=="2":
        os.system("cls")
        print("""
  _____ ___  ___   _  __     ___ ___  __  __ ___  _   _  _ ___ ___ ___    ___  ___   ___ __ ___ __  
 |_   _/ _ \| _ \ / |/  \   / __/ _ \|  \/  | _ \/_\ | \| |_ _| __/ __|  / _ \| __| |_  )  \_  )  \ 
   | || (_) |  _/ | | () | | (_| (_) | |\/| |  _/ _ \| .` || || _|\__ \ | (_) | _|   / / () / / () |
   |_| \___/|_|   |_|\__/   \___\___/|_|  |_|_|/_/ \_\_|\_|___|___|___/  \___/|_|   /___\__/___\__/ 

            """)
        time.sleep(2)
        print(" #1 ICBC")
        time.sleep(0.5)
        print("   China   ")
        print(" ")
        time.sleep(1)
        print(" #2  China Construction Bank  ")
        time.sleep(0.5)
        print("  China   ")
        print(" ")
        time.sleep(1)
        print(" #3  JPMorgan Chase  ")
        time.sleep(0.5)
        print("   US   ")
        print(" ")
        time.sleep(1)
        print(" #4  Berkshire Hathaway  ")
        time.sleep(0.5)
        print("   China  ")
        print(" ")
        time.sleep(1)
        print(" #5  Agricultural Bank of China  ")
        time.sleep(0.5)
        print("   China   ")
        print(" ")
        time.sleep(1)
        print(" #6  Saudi Arabian Oil Company (Saudi Aramco)  ")
        time.sleep(0.5)
        print("   Saudi Arabia   ")
        print(" ")
        time.sleep(1)
        print(" #7  Ping An Insurance Group  ")
        time.sleep(0.5)
        print("   China   ")
        print(" ")
        time.sleep(1)
        print(" #8  Bank of America  ")
        time.sleep(0.5)
        print("   US	")
        print(" ")
        time.sleep(1)
        print(" #9  Apple  ")
        time.sleep(0.5)
        print("   US   ")
        print(" ")
        time.sleep(1)
        print(" #10 Bank of China  ")
        time.sleep(0.5)
        print("  China   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()


    elif f=="3":
        os.system("cls")
        print("""

  ___ _  _ ___ ___   _   _ ___   _____ ___  ___   _____ ___ _  _   ___ ___ ___ _  _ ___ ___ _____   ___ ___ ___  ___ _    ___ 
 |_ _| \| |   \_ _| /_\ ( ) __| |_   _/ _ \| _ \ |_   _| __| \| | | _ \_ _/ __| || | __/ __|_   _| | _ \ __/ _ \| _ \ |  | __|
  | || .` | |) | | / _ \|/\__ \   | || (_) |  _/   | | | _|| .` | |   /| | (__| __ | _|\__ \ | |   |  _/ _| (_) |  _/ |__| _| 
 |___|_|\_|___/___/_/ \_\ |___/   |_| \___/|_|     |_| |___|_|\_| |_|_\___\___|_||_|___|___/ |_|   |_| |___\___/|_| |____|___|
                                                                                                                              
                   """)
        
        time.sleep(2)
        print(" #1 Mukesh Ambani")
        time.sleep(0.5)
        print("   Reliance Industries   ")
        print(" ")
        time.sleep(1)
        print(" #2 Gautam Adani")
        time.sleep(0.5)
        print("   Adani Ports & SEZ   ")
        print(" ")
        time.sleep(1)
        print(" #3  Hinduja Brothers")
        time.sleep(0.5)
        print("   Ashok Leyland   ")
        print(" ")
        time.sleep(1)
        print(" #4  Pallonji Mistry")
        time.sleep(0.5)
        print("   Shapoorji Pallonji Group  ")
        print(" ")
        time.sleep(1)
        print(" #5  Uday Kotak")
        time.sleep(0.5)
        print("   Kotak Mahindra Bank   ")
        print(" ")
        time.sleep(1)
        print(" #6  Shiv Nadar")
        time.sleep(0.5)
        print("   HCL Technologies   ")
        print(" ")
        time.sleep(1)
        print(" #7  Radhakishan Damani")
        time.sleep(0.5)
        print("   Avenue Supermarts   ")
        print(" ")
        time.sleep(1)
        print(" #8  Godrej Family")
        time.sleep(0.5)
        print("   Godrej Group	   ")
        print(" ")
        time.sleep(1)
        print(" #9  Lakshmi Mittal")
        time.sleep(0.5)
        print("   ArcelorMittal   ")
        print(" ")
        time.sleep(1)
        print(" #10 Kumar Mangalam Birla")
        time.sleep(0.5)
        print("  Aditya Birla Group   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()

    elif f=="4":
        os.system("cls")
        print("""
  __  __  ___  ___ _____   ___ _  _ _  _  _____   ___ _____ _____   _____    ___ ___  __  __ ___  _   _  _ ___ ___ ___ 
 |  \/  |/ _ \/ __|_   _| |_ _| \| | \| |/ _ \ \ / /_\_   _|_ _\ \ / / __|  / __/ _ \|  \/  | _ \/_\ | \| |_ _| __/ __|
 | |\/| | (_) \__ \ | |    | || .` | .` | (_) \ V / _ \| |  | | \ V /| _|  | (_| (_) | |\/| |  _/ _ \| .` || || _|\__ \
 |_|  |_|\___/|___/ |_|   |___|_|\_|_|\_|\___/ \_/_/ \_\_| |___| \_/ |___|  \___\___/|_|  |_|_|/_/ \_\_|\_|___|___|___/
                                                                                                                       
              """)
        time.sleep(2)
        print(" #1  Apple  ")
        time.sleep(0.5)
        print("   Technology   ")
        print(" ")
        time.sleep(1)
        print(" #2  Alphabet  ")
        time.sleep(0.5)
        print("  Technology   ")
        print(" ")
        time.sleep(1)
        print(" #3  Amazon  ")
        time.sleep(0.5)
        print("   Consumer Goods   ")
        print(" ")
        time.sleep(1)
        print(" #4  Microsoft  ")
        time.sleep(0.5)
        print("   Technology  ")
        print(" ")
        time.sleep(1)
        print(" #5  Samsung  ")
        time.sleep(0.5)
        print("   Technology   ")
        print(" ")
        time.sleep(1)
        print(" #6  Huawei  ")
        time.sleep(0.5)
        print("   Technology   ")
        print(" ")
        time.sleep(1)
        print(" #7  Alibaba  ")
        time.sleep(0.5)
        print("   Consumer Goods   ")
        print(" ")
        time.sleep(1)
        print(" #8  IBM  ")
        time.sleep(0.5)
        print("   Technology	")
        print(" ")
        time.sleep(1)
        print(" #9  Sony  ")
        time.sleep(0.5)
        print("   Consumer Goods   ")
        print(" ")
        time.sleep(1)
        print(" #10 Facebook  ")
        time.sleep(0.5)
        print("  Technology   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()



    elif f=="5":
        os.system("cls")
        print("""
  ___ ___  ___ ___ ___ ___   ____ __    _   _ _  _ ___  ___ ___   ____ __    _    ___   _   __  __ ___ _  _  ___ 
 | __/ _ \| _ \ _ ) __/ __| |__ //  \  | | | | \| |   \| __| _ \ |__ //  \  (_)  / __| /_\ |  \/  |_ _| \| |/ __|
 | _| (_) |   / _ \ _|\__ \  |_ \ () | | |_| | .` | |) | _||   /  |_ \ () |  _  | (_ |/ _ \| |\/| || || .` | (_ |
 |_| \___/|_|_\___/___|___/ |___/\__/   \___/|_|\_|___/|___|_|_\ |___/\__/  (_)  \___/_/ \_\_|  |_|___|_|\_|\___|
             """)
        
        time.sleep(2)
        print(" #1  Kezie Adamo, 27  ")
        time.sleep(0.5)
        print("   Programmer, StudioMDHR   ")
        print(" ")
        time.sleep(1)
        print(" #2  Nick Amyoony, 25  ")
        time.sleep(0.5)
        print("  Professional Gamer, Nick Eh 30   ")
        print(" ")
        time.sleep(1)
        print(" #3  Brent Batas, 29 & Julian Gari, 28  ")
        time.sleep(0.5)
        print("   Cofounders, AutoAttack Games   ")
        print(" ")
        time.sleep(1)
        print(" #4  Joseph Bentley  ")
        time.sleep(0.5)
        print("   Head of Beyond Entertainment, Logitech  ")
        print(" ")
        time.sleep(1)
        print(" #5  Justin Britch  ")
        time.sleep(0.5)
        print("   Head of Development, Obsidian Entertainment   ")
        print(" ")
        time.sleep(1)
        print(" #6  Maxx Burman  ")
        time.sleep(0.5)
        print("   Cofounder, KitBash3d   ")
        print(" ")
        time.sleep(1)
        print(" #7  Bonnie Burton  ")
        time.sleep(0.5)
        print("   Producer, Bungie   ")
        print(" ")
        time.sleep(1)
        print(" #8  Rebecca Ford  ")
        time.sleep(0.5)
        print("   Live Operations and Community Director, Digital Extremes	")
        print(" ")
        time.sleep(1)
        print(" #9  Lauren Gaba Flanagan  ")
        time.sleep(0.5)
        print("   Cofounder, Theorycraft   ")
        print(" ")
        time.sleep(1)
        print(" #10 Kyle Giersdorf  ")
        time.sleep(0.5)
        print("  Professional Gamer, Sentinels (Bugha)   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()

    elif f=="6":
        os.system("cls")
        print("""
  ___ ___  ___ ___ ___ ___   ____ __    _   _ _  _ ___  ___ ___   ____ __    _   ___  ___ ___ ___ _  _  ___ ___ 
 | __/ _ \| _ \ _ ) __/ __| |__ //  \  | | | | \| |   \| __| _ \ |__ //  \  (_) / __|/ __|_ _| __| \| |/ __| __|
 | _| (_) |   / _ \ _|\__ \  |_ \ () | | |_| | .` | |) | _||   /  |_ \ () |  _  \__ \ (__ | || _|| .` | (__| _| 
 |_| \___/|_|_\___/___|___/ |___/\__/   \___/|_|\_|___/|___|_|_\ |___/\__/  (_) |___/\___|___|___|_|\_|\___|___|
                                                                                                                
              """)
        time.sleep(2)
        print(" #1  G M Mahmud Arif Pavel  ")
        time.sleep(0.5)
        print("   Postdoctoral Associate, Scripps Research   ")
        print(" ")
        time.sleep(1)
        print(" #2  Julie Bliss Mullen  ")
        time.sleep(0.5)
        print("  Cofounder, Aclarity Water   ")
        print(" ")
        time.sleep(1)
        print(" #3  Chris Boyce  ")
        time.sleep(0.5)
        print("   Assistant Professor, Columbia University   ")
        print(" ")
        time.sleep(1)
        print(" #4  Ava Carter  ")
        time.sleep(0.5)
        print("   PhD Student, Stanford University  ")
        print(" ")
        time.sleep(1)
        print(" #5  Kevin Chen  ")
        time.sleep(0.5)
        print("   Postdoctoral Fellow, Harvard University   ")
        print(" ")
        time.sleep(1)
        print(" #6  Meghali Chopra  ")
        time.sleep(0.5)
        print("   CEO, SandBox Semiconductor Incorporated   ")
        print(" ")
        time.sleep(1)
        print(" #7  Lorin Crawford  ")
        time.sleep(0.5)
        print("   Assistant Professor, Brown University   ")
        print(" ")
        time.sleep(1)
        print(" #8  Jeffrey Dick  ")
        time.sleep(0.5)
        print("   Assistant Professor, The University of North Carolina at Chapel Hill	")
        print(" ")
        time.sleep(1)
        print(" #9  Jonathan C. Grima  ")
        time.sleep(0.5)
        print("   Postdoctoral Fellow, Johns Hopkins University   ")
        print(" ")
        time.sleep(1)
        print(" #10  Mark Groden  ")
        time.sleep(0.5)
        print("  Founder, SkyRyse   ")
        print(" ")
        time.sleep(1)
        input("press enter to continue")
        os.system("cls")
        forbes()
        
    else:
        os.system("cls")
        print(" Please enter the correct optionns ( 1 , 2 , 3 ,4 etc..")
        print(" ")
        forbes()
#-----------------------------------------------------------------------(ends here)----------------------------------------------------------------------------------
        
#-------------------------------------------------------------(STARTUP CODE)------------------------------------------------------------------------------------------
def check():
    ask=input("DO  YOU  HAVE  A  CRYPIX  ACCOUNT  ?  (y/n)")
    if ask == "n" or ask=="N" :
        os.system("cls")
        signup()
    elif ask == "y" or ask=="Y":
        os.system("cls")
        signin()
    else:
        print("Please answer in 'y' or 'n' ")
        check()
#--------------------------------------------------------------(STARTUP CODE ENDS)------------------------------------------------------------------------------------
    
    



#------------------------------------------------ THE INITIAL DISPLAY CODE--------------------------------------------------------------------------------------------    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("""                          
                                      ______  _______   ____  ____  _______  _____  ____  ____  
                                    .' ___  ||_   __ \ |_  _||_  _||_   __ \|_   _||_  _||_  _| 
                                   / .'   \_|  | |__) |  \ \  / /    | |__) | | |    \ \  / /   
                                   | |         |  __ /    \ \/ /     |  ___/  | |     > `' <    
                                   \ `.___.'\ _| |  \ \_  _|  |_    _| |_    _| |_  _/ /'`\ \_  
                                    `.____ .'|____| |___||______|  |_____|  |_____||____||____| 
                                                             
""")
print("-")
time.sleep(1.5)
print("""                
                                   ___     __            ___ ___     __         __      __  __ ___ 
                                    | |__||_   |\/|/  \|  | | |  /\ (_ |_/||\ |/ _  __ |__)/  \ |  
                                    | |  ||__  |  |\__/|__| | | /--\__)| \|| \|\__)    |__)\__/ |  """)
                                                                



print(".")
time.sleep(1)
print(".")
time.sleep(1)
check()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


