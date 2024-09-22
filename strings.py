with open ('snowwhite.txt', 'r') as file:
    text = file.read()

words = text.split('. ')
cap_words = []

for w in words:
    w = w.capitalize()
    cap_words.append(w)
    
    
cap_text = ' '.join(cap_words)

with open ('snowwhite_corrected.txt', 'w') as file:
    file.write(cap_text)
    
    
