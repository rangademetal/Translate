from googletrans import Translator
import db;
translate = Translator()

while True:

    lang = input("(rom/eng):")
    if lang == 'rom':
        print("Romanian to English")
        n = input("Introdu propozitia:")
        m = input("propozitia corecta:")
        if translate.translate(n).text == m:
            print("Correct!")
        else:
            print("Expecting:" + translate.translate(n).text)
        db.insert(n, m, translate.translate(n).text)
    if lang == 'eng':
        print("English to Romanian")
        n = input("Enter your sentence:")
        m = input("Excpecting:")
        if translate.translate(n, dest='ro').text == m:
            print("Correct!")
        else:
            print("Expecting:" + translate.translate(n).text)
        db.insert(n, m, translate.translate(n, dest='ro').text)