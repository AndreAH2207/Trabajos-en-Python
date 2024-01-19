def greet(lang):
    if lang=='es':
        print ("Hola")
    elif lang=='fr':
        print("Bonjour")
    else:
        print ("Hello")

        greet('en')
        greet('es')
        greet('fr')
        greet('us')

def greet2(lang):
    if lang=='es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"
    print(greet2('es'),"Pedro")
    print(greet2('fr'),"Juan")
