
import PyPDF2
import os
import pytesseract
import pyaudio
import wave
import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont
import pyttsx3
import tkinter as tk


def img_txt(path):
    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'environment/lib/python3.10/site-packages/tesseract'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    # Simple image to string
    text=pytesseract.image_to_string(Image.open(path))
    input_box = tk.Toplevel()
    input_box.title("IMG-TEXT")
    if(text.isspace()):
        text="\nThe Image does not contain any image\n"
    label = tk.Label(input_box, text=text)
    label.pack()


def pdf_txt():
    if(os.path.isdir("temp") == False):
        os.mkdir("temp")  
    txtpath = ""
    pdfpath = ""
    pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   #Provide the path for your pdf here
    txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")   #Provide the path for the output text file  
    BASEDIR = os.path.realpath("temp") # This is the sample base directory where all your text files will be stored if you do not give a specific path
    print(BASEDIR)
    if(len(txtpath) == 0):
        txtpath = os.path.join(BASEDIR,os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "")+".txt")
    pdfobj = open(pdfpath, 'rb')
    pdfread = PyPDF2.PdfReader(pdfobj)
    x = len(pdfread.pages)
    for i in range(x):
        pageObj = pdfread.pages[i]
        with open(txtpath, 'a+') as f: 
            f.write((pageObj.extract_text()))
        print(pageObj.extract_text()) #This just provides the overview of what is being added to your output, you can remove it if want
    pdfobj.close()  


def speech_txt(j=0):
    #parameters of the audio
    #name of the file generated
    #length of the recording period
    seconds = 5
    # frameperbuffer is in bytes
    frameperbuffer = 3200
    #sizedepthwidth as in format is bit depth of a audio and is related to accuracy of a audio and has only two values 16 bit(2x) and 24 bits(3x)
    sizedepthwidth = pyaudio.paInt16
    #channels are the number of audio channels(like mono(1) or stereo(2))
    channel = 1
    #framerate as in rate is frequency(or sample frequency or cycle) of a audio and is related to its quality and also affects its file size usually, 48k or 16k or 44.1k
    framerate = 16000
    #pyaudio object creation
    p = pyaudio.PyAudio()
    #set audio parameter 
    stream = p.open(
    format=sizedepthwidth,
    channels=channel,
    rate=framerate,
    input=True,
    frames_per_buffer=frameperbuffer
    )
    #print("start recording...",framerate / frameperbuffer * seconds)
    print("start recording...",seconds,"s")
    # starts recording voice in stream and stores in frames 
    frames = []
    for i in range(0, int(framerate / frameperbuffer * seconds)):
        data = stream.read(frameperbuffer)
        frames.append(data)
    #terminates/close recording
    #stop recording
    stream.stop_stream()
    #close recording object
    stream.close()
    #terminates pyaudio object
    p.terminate()
    print("recording stopped")
    audio_data = sr.AudioData(b''.join(frames), sample_rate=framerate, sample_width=p.get_sample_size(sizedepthwidth))
    r = sr.Recognizer()
    #audio_data = b''.join(frames)
    text = r.recognize_google(audio_data)
    # Print the extracted text
    if(j==1):
        print("inside if")
        txt_img(text,1)
    else:
        input_box = tk.Toplevel()
        input_box.title("VOICE-TEXT")
        label = tk.Label(input_box, text=text)
        label.pack()
        entry = tk.Entry(input_box)
        entry.pack()


def txt_img(text,i=0):
    print("its txt-img")
    if(i==1):
        print("its 1")
    # set the text to be added to the image
    # set the font size and font type
    font_size = 50
    font_type = "arial.ttf"
    # create the font object
    font = ImageFont.truetype(font_type, size=font_size)
    # calculate the required width and height of the image
    text_width, text_height = font.getsize(text)
    image_width = text_width + 20  # add padding to the width
    image_height = text_height + 20  # add padding to the height
    # create a new image with the calculated dimensions
    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    # create a draw object
    draw = ImageDraw.Draw(image)
    # set the position for the text
    text_x = 10
    text_y = 10
    # add the text to the image
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))
    # save the image
    image.save('text_image.png')
    image.show()
    image.close()
    image.__exit__()


def txt_speech(text):
    
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
    text = text.replace('. ', '.\n\n')
    text = text.replace(', ', ',\n')
    if text.isspace() or len(text.strip()) == 0:
        print("\nThe string is empty or contains only white spaces\n")
    else:
        #print("The string is not empty and contains non-white space characters")
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()




def speech_img():
    speech_txt(1)

from tkinter import filedialog

def choose_file_location():
    # Open file dialog and get selected file location
    img_txt(filedialog.askopenfilename()) 


def open_input_box():
    input_box = tk.Toplevel()
    input_box.title("TEXT-VOICE")

    label = tk.Label(input_box, text="Enter your text:")
    label.pack()

    entry = tk.Entry(input_box)
    entry.pack()

    button = tk.Button(input_box, text="speech", command=lambda: txt_speech(entry.get()))
    button.pack()
    button2 = tk.Button(input_box, text="img", command=lambda: txt_img(entry.get()))
    button2.pack()

def open_input_box1():
    input_box = tk.Toplevel()
    input_box.title("TEXT-VOICE")
    label = tk.Label(input_box, text="Enter your text:")
    label.pack()
    entry = tk.Entry(input_box)
    entry.pack()
    button = tk.Button(input_box, text="text", command=lambda: speech_txt())
    button.pack()
    button = tk.Button(input_box, text="image", command=lambda: speech_img())
    button.pack()
    
def open_input_box2():
    input_box = tk.Toplevel()
    input_box.title("TEXT-VOICE")
    label = tk.Label(input_box, text="Enter your text:")
    label.pack()
    entry = tk.Entry(input_box)
    entry.pack()
    button = tk.Button(input_box, text="Choose File Location", command=choose_file_location)
    button.pack()
def main():
    root = tk.Tk()
    root.title("Main Window")
    button = tk.Button(root, text="Text Based", command=open_input_box)
    button.pack()
    button1 = tk.Button(root, text="Voice Based", command=open_input_box1)
    button1.pack()
    button2 = tk.Button(root, text="Image Based", command=open_input_box2)
    button2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

