#Team 45
#Vansh Sharma
#Sanket Deb
import pyttsx3 , datetime , wikipedia , webbrowser , os , wolframalpha , time , random
import speech_recognition as sr
from selenium import webdriver
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour<17:
        print("Good Afternoon")
        speak("Good Afternoon")
    elif hour>=17 and hour<19:
        print("Good Evening")
        speak("Good Evening")
    else:
        print("Hope you had a great day")
        speak("Hope you had a great day")
    print("I am Dhruv, Please tell me how may I help you ?")
    speak("I am Dhruv, Please tell me how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print("User said: "+query)
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query
def pause():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold=0.8
            audio=r.listen(source)
        query=r.recognize_google(audio,language="en-in")
        try:
            if query=="resume" or query=="Dhruv":
                print("Yes,sir")
                speak("Yes, sir")
            else:
                print("...")
                pause()
        except:
            pause()
    except:
        pause()
def whatsapp(txt):
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    import time
    Chrome_Profile_Path = "user-data-dir=C:\\Users\\vansh\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"
    options = webdriver.ChromeOptions()
    options.add_argument(Chrome_Profile_Path)
    def new_chat(user_name):
        time.sleep(2)
        new_chat = driver.find_element_by_xpath('//div[@class="RPX_m"]')
        new_chat.click()
        new_user = driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
        new_user.send_keys(user_name)
        time.sleep(1)
        try:
            user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException:
            print('Given user "{}" not found in the contact list'.format(user_name))
        except Exception as e:
            driver.close()
            print(e)
            sys.exit()
    ask_text = txt
    ask_contact= ["Android"]
    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com/')
    for names in ask_contact:
        time.sleep(1)
        WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')).send_keys(names)
        WebDriverWait(driver,15).until(lambda driver:driver.find_element_by_xpath('//span[@title="{}"]'.format(names))).click()
        inp_xpath = '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)
        input_box.send_keys(ask_text + Keys.ENTER)
    time.sleep(5)
    driver.quit()
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia")
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'hi' in query or 'hey' in query or 'hello' in query:
            print("Hi")
            speak("Hi")
        elif 'what\'s up' in query or 'how are you' in query:
            reply=['I\'m great','I\'m good','I\'m fine','I\'m excited to help you out']
            out=random.choice(reply)
            print(out)
            speak(out)
        elif 'time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M")
           print(f"Sir, the time is {strTime}")
           speak(f"Sir, the time is {strTime}")
        elif 'who are you' in query or 'what are you' in query or 'describe yourself' in query:
            print("I am Dhruv. I make things easy for you. I can perform different tasks.")
            speak("I am an Dhruv. I make things easy for you. I can perform different tasks.")
        elif 'you do' in query or 'your work' in query:
            print('I make things easy and help you as much as I can')
            speak('I make things easy and help you as much as I can')
        elif 'according to google' in query or 'google' in query:
            query=query.replace("according to google","")
            browser=webdriver.Chrome() 
            browser.get("https://google.com/?#q="+str(query))
        elif 'pause' in query or 'shut up' in query or 'hold on' in query:
            print("Ok")
            pause()
        elif 'i am not feeling well' in query or "I am ill" in query:
            print("Disease prediction starting...")
            speak("Disease prediction starting")
            import disease_prediction
            disease_prediction.NaiveBayes()
            print("Take care")
            speak("Take care")
        elif 'emergency' in query:
            whatsapp("*EMERGENCY*\nTHERE IS AN IMMEDIATE NEED OF HUMANN ASSISTANCE. KINDLY ATTEND TO IT ASAP\n ~ automated reply by Dhruv")
        elif 'quit' in query or 'log off' in query or 'close' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            print("Thankyou for using me. See you soon.")
            speak("Thankyou for using me. See you soon.")
            print("_____________LOGGING OFF_____________")
            break
        else:
            client1=wolframalpha.Client('JW6Y7Q-GKWVR76AJG')
            if query!='none':
                try:
                    try:
                        res=client1.query(query)
                        results=next(res.results).text
                        print('Look what I found')
                        speak('Look what I found')
                        print(results)
                        speak(results)
                    except:
                        results=wikipedia.summary(query, sentences=3)
                        print('According to Wikipedia')
                        speak('According to Wikipedia')
                        print(results)
                        speak(results)
                except:
                    browser=webdriver.Chrome() 
                    browser.get("https://google.com/?#q="+str(query))