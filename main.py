LETTER_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..'}


MORSE_TO_LETTER = {}
for key, value in LETTER_TO_MORSE.items():
    MORSE_TO_LETTER[value] = key


def letter_to_morse(message):
    morse = []
    for char in message:
        if char in LETTER_TO_MORSE:
            morse.append(LETTER_TO_MORSE[char])
    return " ".join(morse)


def morse_to_letter(message):
    message = message.split(" ")
    letter = []
    for code in message:
        if code in MORSE_TO_LETTER:
            letter.append(MORSE_TO_LETTER[code])
    return " ".join(letter)


def main():
    while True:
        response = input("Morse to Letter (1) or Letter to Morse (2)?").upper()
        if response == "1" or response == "2":
            break

    if response == "1":
        print("Enter Morse code (with a space after each code): ")
        morse = input("> ")
        letter = morse_to_letter(morse)
        print("Decoded Version")
        print(letter)

    elif response == "2":
        print("Enter Text Message: ")
        letter = input("> ").upper()
        morse = letter_to_morse(letter)
        print("Encoded Version")
        print(morse)


if __name__ == "__main__":
    main()