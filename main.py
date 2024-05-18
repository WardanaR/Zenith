##############################
#                            #
#  Created by Wardana'2024   #
#  Indonesia                 #
#                            #
##############################

#pip install flet
#pip install ollama
#pip install pyttsx3

import flet as ft  #for GUI
import ollama      #for Ollama
import pyttsx3     #for speech

def main(page):
    page.title = "Zenith the GUI of Ollama"

    #some controls
    txt_pesan = ft.TextField(label="Prompt", multiline=True, max_lines=8)
    txt_hasil = ft.TextField(label="Response", multiline=True, max_lines=8)
    lbl_lastorder = ft.Text("Last Prompt", size=20)
    chk_speech= ft.Checkbox(label="Speech", value=True)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    
    def btn_click(e):
        if not txt_pesan.value:
            txt_pesan.error_text = "Input the message"
            page.update()
        else:
            pesan = txt_pesan.value
            txt_pesan.value = "Please Wait"
            page.update()
            #llava
            #deep-coder
            #llama3
            response = ollama.chat(model='llama3', messages=[
              {
                'role': 'user',
                'content': pesan,
              },
            ])
            txt_hasil.value = response['message']['content']
            txt_pesan.value = ""
            txt_hasil.focus()
            lv.controls.append(ft.Text(pesan))
            page.update()
            #speech
            if chk_speech.value==True:
              engine = pyttsx3.init()
              rate = engine.getProperty('rate')
              engine.setProperty('rate', rate-50)
              engine.say(txt_hasil.value)
              engine.runAndWait()
                
    page.add(txt_pesan, ft.FilledButton("Send Message", on_click=btn_click, icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED), chk_speech, txt_hasil, lbl_lastorder, lv)

ft.app(target=main)
