alphabet= 'abcdefghijklmnopqrstuvwxyz'
def alphabet_position(text):
    text = text.lower()
    sp  = [str(alphabet.find(i) + 1) for i in text if i in alphabet]
    return ' '.join(sp)
    pass
