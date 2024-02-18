import el.txt_speech
import el.speech_txt
import el.img_txt
import el.txt_img
import el.pdf_txt

while(True):
    print("1. Text to speech \n 2. Speech text \n 3. Image to text \n 4. Text to img \n 5. PDF to text")
    ch=input("Enter your choices\t:")
    if(ch=='1'):
        el.txt_speech.txt_speech();
    elif(ch=='2'):
        el.speech_txt.speech_txt();
    elif(ch=='3'):
        el.img_txt.img_txt();
    elif(ch=='4'):
        el.txt_img.txt_img();
    elif(ch=='5'):
        el.pdf_txt.pdf_txt();
    elif(ch=='0'):
        print("Program terminated");
        break;
    else:
        print("Enter the correct option")
