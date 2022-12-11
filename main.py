from playsound import playsound
import time

CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '·−−−−·',
    '!': '−·−·−−',
    '/': '−··−·',
    '(': '−·−−·',
    ')': '−·−−·−',
    '&': '·−···',
    ':': '−−−···',
    ';': '−·−·−·',
    '=': '−···−',
    '+': '·−·−·',
    '-': '−····−',
    '_': '··−−·−',
    '"': '·−··−·',
    '$': '···−··−',
    '@': '·−−·−·',
    ' ': '|',
}


def encrypt(message):
    morse_code = ''
    for letter in message:
        morse_code += CODE[letter.upper()] + ' '
    return morse_code


def sound(message):
    for char in message:
        if char == ".":
            playsound('beep.wav')

        elif char == "-":
            playsound('long_beep.mp3')

        elif char == "|" or char == " ":
            time.sleep(0.5)



question = input("If you would like to translate to Morse Code, enter 1\n"
                 "If you would like to translate from Morse Code to tex, enter 2: ")

if question == "1":
    words = input("Please enter the word or phrase you wish to translate: ")
    morse_code = encrypt(words)

    print(morse_code)
    sound(morse_code)

elif question == "2":
    translate = input("PLease enter the code here you wish to translate: ")
    reverse_dict = {v: k for k, v in CODE.items()}
    to_words = "".join(reverse_dict[char] for char in translate.split(" "))

    print(to_words)


