alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', 
'..-', '...-', '.--', '-..-', '-.--', '--..']

# Converts English messages into Morse Code
def english_to_morse(message):

    morse_message = ''

    # Finds and adds the corresponding Morse string to the message
    for letter in message:
        if letter == ' ':
            morse_message += ' / '
        else:
            # If there isn't a corresponding Morse string to a character used, ignore it.
            try:
                morse_message += f'{morse_alphabet[alphabet.index(letter.upper())]} '

            except:
                continue

    return f'Translated Message: {morse_message}'

# Converts Morse messages into English
def morse_to_english(message):

    english_message = ''

    # Splits message into list of morse_letters
    morse_message = message.split()

    # Finds and adds the corresponding English letter to the message
    for sequence in morse_message:
        if sequence == '/':
            english_message += ' '
        else:
            # If there isn't a corresponding English letter to the sequence used, ignore it.
            try:
                english_message += f'{alphabet[morse_alphabet.index(sequence)]}'

            except:
                continue

    return f'Translated Message: {english_message}'

def main():

    input('._._._._._.MORSE TRANSLATOR._._._._._.')

    while True:

        print('1. Translate English to Morse Code \n2. Translate Morse Code to English \n3. Exit')

        # Asks user what they want to do, then does it
        match input('What would you like to do? '):

            case '1':
                input(english_to_morse(input('What do you want to translate into Morse Code? \n')))

            case '2':
                input(morse_to_english(input('What do you want to translate into English? \n')))

            case '3':
                break

            case _:
                input('Invalid Input')

main()