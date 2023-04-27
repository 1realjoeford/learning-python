def emoji_converter(message):
    emojis = {
        ':)' : '(happy)',
        ':(' : "sad"
    }
    words = message.split(' ')
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output
        
    

#message = input('> ')

#print(emoji_converter(message))

kofi = emoji_converter()
ama = kofi('hiiii :)')
print(ama)