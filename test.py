text = 'Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar.'

def countWords(text):
    text = text.replace(',','')
    text = text.replace('.','')
    newWordArray = text.split(' ')
    for word in newWordArray:
        wordCounter = newWordArray.count(word)
        print(f'word {word} appears {wordCounter} times in the the text')
        
    
    
countWords(text)