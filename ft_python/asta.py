import speech_recognition as sr
import pyttsx3
import random
import datetime
import webbrowser
import os
import wikipedia

class Asta:
    def __init__(self):  # Corrigido aqui
        self.name = "Asta"
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        wikipedia.set_lang('pt')

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                self.listener.adjust_for_ambient_noise(source)
                audio = self.listener.listen(source)
                command = self.listener.recognize_google(audio, language='pt-BR')
                command = command.lower()
                print("Compreendi:", command)
                return command
        except:
            return ""

    def greet(self):
        greetings = [
            "Olá Como posso ajudar?",
        ]
        greeting = random.choice(greetings)
        print(greeting)
        self.say(greeting)

    def search_google(self, query):
        response = f"Procurando por '{query}' no Google..."
        print(response)
        self.say(response)
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

    def search_instagram(self, query):
        response = f"Procurando por '{query}' no instagram..."
        print(response)
        self.say(response)
        url = f"https://www.instagram.com/{query}"
        webbrowser.open(url)

    def search_youtube(self, query):
        response = f"Procurando por '{query}' no youtube..."
        print(response)
        self.say(response)
        url = f"https://www.youtube.com/search?q={query}"
        webbrowser.open(url)

    def search_youtube_music(self, query):
        response = f"Procurando por '{query}' no youtube Music..."
        print(response)
        self.say(response)
        url = f"https://music.youtube.com/search?q={query}"
        webbrowser.open(url)

    def search_wikipedia(self, query):
        response = f"Procurando por '{query}' na Wikipedia..."
        print(response)
        self.say(response)
        try:
            page_summary = wikipedia.summary(query, sentences=2)
            print(page_summary)
            self.say(page_summary)
        except:
            print("Desculpe, não consegui encontrar informações sobre isso na Wikipedia.")
            self.say("Desculpe, não consegui encontrar informações sobre isso na Wikipedia.")

    def study_help(self, subject):
        response = f"Vamos estudar {subject}..."
        print(response)
        self.say(response)
        try:
            page_summary = wikipedia.summary(subject, sentences=5)
            print(page_summary)
            self.say(page_summary)
        except:
            print("Desculpe, não consegui encontrar informações sobre isso na Wikipedia.")
            self.say("Desculpe, não consegui encontrar informações sobre isso na Wikipedia.")

    def perform_action(self, action):
        if "pesquisar" in action:
            query = action.split("pesquisar")[-1].strip()
            self.search_google(query)
        elif "perfil" in action:
            query = action.split("instagram")[-1].strip()
            self.search_instagram(query)
        elif "assistir" in action:
            query = action.split("assistir")[-1].strip()
            self.search_youtube(query)
        elif "ouvir" in action:
            query = action.split("ouvir")[-1].strip()
            self.search_youtube_music(query)
        elif "pesquise" in action:
            query = action.replace("pesquisar na wikipedia", "").strip()
            self.search_wikipedia(query)
        elif "estudar" in action:
            subject = action.replace("estudar", "").strip()
            self.study_help(subject)
        else:
            self.say("Desculpe, não entendi o comando.")

    def goodbye(self):
        goodbyes = [
            "Até mais! Se precisar de mais alguma coisa, estarei por aqui.",
            "Até logo! Espero ter sido útil. Tenha um ótimo dia!",
            "Tchau! Se cuida e até a próxima."
        ]
        goodbye = random.choice(goodbyes)
        print(goodbye)
        self.say(goodbye)


# Exemplo de uso:
asta = Asta()
asta.greet()

while True:
    action = asta.listen()
    asta.perform_action(action)

    if "tchau" in action or "adeus" in action:
        asta.goodbye()
        break