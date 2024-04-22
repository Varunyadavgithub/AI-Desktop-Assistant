import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def tasks(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
    
    elif "hello" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech("hello, sir How can I hep you ?")
        return "hello, sir How can I hep you ?"

    elif "how are you" in  user_data :
        text_to_speech.text_to_speech("I am doing great these days sir") 
        return "I am doing great these days sir"   

    elif "thanku" in user_data or "thank" in user_data:
        text_to_speech.text_to_speech("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"      


    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning, sir how can I help you")
        return "good morning, sir how can I help you"
    
    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("good afternoon, sir how can I help you")
        return "good afternoon, sir how can I help you"

    elif "good evening" in user_data:
        text_to_speech.text_to_speech("good evening, sir how can I help you")
        return "good evening, sir how can I help you"

    elif "good night" in user_data:
        text_to_speech.text_to_speech("good night, sir how can I help you")
        return "good night, sir how can I help you"

    elif "time" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" ,(str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("gana.com is now ready for you, enjoy your music")
        return "gana.com is now ready for you"

    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

    elif "google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"

    elif "linkedin" in user_data:
        webbrowser.open("https://www.linkedin.com/")
        text_to_speech.text_to_speech("linkedin.com is now ready for you")
        return "linkedin.com is now ready for you"

    elif "chatgpt" in user_data:
        webbrowser.open("https://chat.openai.com/")
        text_to_speech.text_to_speech("chat GPT is now ready for you")
        return "chat GPT is now ready for you"

    elif "weather" in user_data:
        ans = weather.weatherData()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"