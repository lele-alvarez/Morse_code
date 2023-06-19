import time
import platform

freq = 550 # Hz
dotLength = 80 # milliseconds
dashLength = dotLength * 3
pauseWords = dotLength * 10


morse_code_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse_code(string):
    morse_code_list = [morse_code_dict.get(char, "") for char in string]
    morse = " ".join(morse_code_list)
    return morse

def beep(dur):
    """
    makes noise for specific duration.
    :param dur: duration of beep in milliseconds
    """
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(freq, dur)
    else:
        # For non-Windows systems.
        pass


def pause(dur):
    """
    pauses audio for dur milliseconds
    :param dur: duration of pause in milliseconds
    """
    time.sleep(dur / 1000)

def morseaudio(morse):
    """
    plays audio conversion of morse string using inbuilt windows module.
    :param morse: morse code string.
    """
    for char in morse:
        if char == ".":
            beep(dotLength)
        elif char == "-":
            beep(dashLength)
        elif char == "  ":
            pause(pauseWords)
        else:
            # char is blank space
            pause(dashLength)




original_text = input("Please, enter your text: ").upper()

morse = morse_code(original_text)
print(morse)
morseaudio(morse)



