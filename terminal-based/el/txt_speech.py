import pyttsx3
def txt_speech():
    # Create a pyttsx3 object
    engine = pyttsx3.init()

    # Set speech rate
    #engine.setProperty('rate', 150)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1)
    engine.setProperty('pitch', 200)

    # Select a high-quality voice
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.languages[0] == 'en_US':
            engine.setProperty('voice', voice.id)
            break

    # Ask user for input text
    text = input("Enter the text you want to convert to speech: ")
    text = text.replace('. ', '.\n\n')
    text = text.replace(', ', ',\n')
    
    if text.isspace() or len(text.strip()) == 0:
        print("\nThe string is empty or contains only white spaces\n")
    else:
        #print("The string is not empty and contains non-white space characters")
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
