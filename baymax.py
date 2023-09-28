import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import wikipedia
import pyjokes

#----------------------------------------------------------------#
#---------------------------Note!!-------------------------------#
#----------------------------------------------------------------#
#>------use the below prompt to downlod requiered packages------<
#----downlod the  requirements.txt file
#pip install -r requirements.txt
#----------------------------------------------------------------#

#-------------------------------------------------#
# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to speak a message
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.check you inernet connection and try again")
        speak("Sorry, there was an issue with the speech recognition service check you inernet connection and try again")
        return 0
    
#--------------------------------------------------------------------------------#
    
#to get user name
name = input("Enter your name: ")
# Function to wish the user
def wish_user():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 12:
        speak(f"Goodmorning,{name}!")
    elif 12 <= hour < 18:
        speak(f"Good afternoon,{name}")
    else:
        speak(f"Good evening,{name}")

# Function to provide the current date and time
def get_date():
    current_time = datetime.datetime.now()
    date_str = current_time.strftime("%B %d, %Y")
    speak(f"Today is {date_str} ")
def get_time():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%I:%M %p")
    speak(f"the time is {time_str}")    

# Function to search in Google
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

# Function to play music (simplified)
#enter you music file directory in music_dir
def play_music():
    music_dir = "F:\music"
    music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
    
    if music_files:
        random.shuffle(music_files)
        os.system(f"start {os.path.join(music_dir, music_files[0])}")
        speak("Enjoy the music!")
    else:
        speak("No music files found.")

def who():
    print("i was buit by karthik krishnan") 
    speak("i was buit by karthik krishnan")    

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke) 
          

     
        
#---------------------------------------------------------#        
#getuser()    
wish_user()
speak("iam baymax how can i help u")
#---------------------------------------------------------#
# Main loop
while True:
    user_input = recognize_speech().lower()
    if "date" in user_input:
        get_date()
        
    elif "time" in user_input:
        get_time()    
        
    elif "search" in user_input:
        query = user_input.split("search", 1)[1].strip()
        search_google(query)
        
    elif "music" in user_input:
      play_music()
      
    elif "wikipedia" in user_input:
        speak("searching in wikipedia")
        user_input=user_input.replace("wikipedia","")
        results=wikipedia.summary(user_input,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        
    elif "who built you" in user_input:
        who() 
        
    elif "joke" in user_input:
        tell_joke() 
        
    elif "stop" in user_input or "exit" in user_input  or "break" in user_input  or "close" in user_input:
        speak("Goodbye!see u next time")
        break
 