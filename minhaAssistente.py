import pyautogui
test = pyautogui
import speech_recognition as sr
import pyttsx3 as py
import pyaudio as pi
import pywhatkit
import time
vanda = py.init()
vanda.say("Olá, Jailson")
vanda.runAndWait()
audio = sr.Recognizer()
with sr.Microphone() as source:
    print("ouvindo")
    a = audio.listen(source)
    comando = audio.recognize_google(a, language="pt-BR")
    comando = comando.lower()
    print(comando)
    if "vanda" or "panda" or "landa" or "banda" or "vana" or "wanda" in comando:
        print("ok")
        comando.replace("vanda", "") or comando.replace("panda",'') or comando.replace("landa","") or comando.replace("banda", '') or comando.replace("vana",'') or comando.replace('wanda', '')
        if "abra o navegador" in comando:
            vanda.say("tentando executar ")
            vanda.runAndWait()
            time.sleep(2)
            test.press("win")
            time.sleep(2)
            test.write("Chrome")
            time.sleep(2)
            test.press("enter")
            time.sleep(2)
            test.moveTo(1000, 700)
            time.sleep(2)
            test.click(1000, 700)
            time.sleep(2)
            print('ouvindo')
            a2 = audio.listen(source)
            comando2 = audio.recognize_google(a2, language="pt-BR")
            comando2 = comando2.lower()
            print(comando2)
            if 'abra o swap' or 'abra o suap' in comando2:
                test.write("https://suap.ifrn.edu.br/accounts/login/")
                time.sleep(2)
                test.press("enter")
                test.press("enter")
                test.press('enter')
        elif "busque por" in comando:
            vanda.say("Agora mesmo, querido")
            vanda.say("redirecionando")
            vanda.runAndWait()
            busca = comando.replace("busque por","")
            pywhatkit.playonyt(busca)
        elif "tirar print da tela toda" in comando:
            vanda.say("Agora mesmo")
            vanda.runAndWait()
            test.hotkey("win", 'prtsc')
        elif "gravar a tela" in comando:
            vanda.say("Agora mesmo, querido")
            vanda.runAndWait()
            test.hotkey("win", "alt", "r")
        elif "abrir o visual" in comando:
            vanda.say("Agora mesmo, querido")
            vanda.runAndWait()
            #test.moveTo(1000,1000)
            time.sleep(5)
            test.click(1300,1500)
            time.sleep(2)
            test.click(50,0)
            test.hotkey("ctrl", "n")
        elif 'ligar para meus pais' in comando:
            time.sleep(2)
            test.press('win')
            test.write('Vincular ao Celular')
            test.press('enter')
            #test.moveTo(600, 210)

        else:
            vanda.say("erro de reconhecimento de voz")
            vanda.runAndWait()