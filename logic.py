import json

indxx = None
ww = None
isActive = False


def check(a):
    try:
        file = open('assistant_database.json', encoding='utf-8')
        data = json.loads(file.read())
        for idx, w in enumerate(data['baza'][0]['categories']):
            global ww
            global indxx
            global isActive
            ww = w
            indxx = idx
            isKey = False
            for key in data['baza'][idx + 1][w]['keywords']:
                for word in a.split():
                    if key == word:
                        isKey = True
                        isActive = True
            if isKey:
                for child in data['baza'][idx + 1][w]['children']:
                    isChildKey = False
                    for childKey in child['keywords']:
                        for wword in a.split():
                            if childKey == wword:
                                isChildKey = True
                    if isChildKey:
                        return child['odpowiedz']

    except FileNotFoundError():
        print("error")


def active(c):
    try:
        file = open('assistant_database.json', encoding='utf-8')
        data = json.loads(file.read())

        global indxx
        global ww

        for child in data['baza'][indxx + 1][ww]['children']:
            isChildKey = False
            for childKey in child['keywords']:
                for wword in c.split():
                    if childKey == wword:
                        isChildKey = True
            if isChildKey:
                return child['odpowiedz']

        file.close()

    except FileNotFoundError():
        print("error")


def conversation(sentence):
    if isActive:
        print("Uzytkownik: " + sentence)
        print("Asystent: " + active(sentence))

    else:
        print("Uzytkownik: " + sentence)
        print("Asystent: " + check(sentence))