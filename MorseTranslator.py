class MorseTranslator:

    @staticmethod
    def translate_from_morse(source_text):
        translation_result = ""
        for code in source_text.split(" "):
            if not code:
                translation_result += " "
            else:
                value = MorseTranslator._code_table_from_Morse[code]
                if value:
                    translation_result += value

        return translation_result

    @staticmethod
    def translate_to_morse(source_text):
        translation_result = ""
        for i in range(len(source_text)):
            code = MorseTranslator._code_table_to_Morse[source_text[i].lower()]
            if code is not None:
                translation_result += code + " "

        if translation_result:
            translation_result = translation_result[:-1]

        return translation_result

    _code_table_from_Morse = {
        ".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd',
        ".": 'e', "..-.": 'f', "--.": 'g', "....": 'h',
        "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l',
        "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p',
        "--.-": 'q', ".-.": 'r', "...": 's', "-": 't',
        "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x',
        "-.--": 'y', "--..": 'z', ".-...": '&', ".----.": '\'',
        ".--.-.": '@', "-.--.-": ')', "-.--.": '(', "---...": ':',
        "--..--": ',', "-.-.--": '!', ".-.-.-": '.', "-....-": '-',
        ".-.-.": '+', ".-..-.": '\"', "..--..": '?', "-..-.": '/',
        "-----": '0', ".----": '1', "..---": '2', "...--": '3',
        "....-": '4', ".....": '5', "-....": '6', "--...": '7',
        "---..": '8', "----.": '9', ".-.-": '\n'
    }

    _code_table_to_Morse = {
        'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..",
        'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
        'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
        'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
        'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
        'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
        'y': "-.--", 'z': "--..", '&': ".-...", '\'': ".----.",
        '@': ".--.-.", ')': "-.--.-", '(': "-.--.", ':': "---...",
        ',': "--..--", '!': "-.-.--", '.': ".-.-.-", '-': "-....-",
        '+': ".-.-.", '\"': ".-..-.", '?': "..--..", '/': "-..-.",
        '0': "-----", '1': ".----", '2': "..---", '3': "...--",
        '4': "....-", '5': ".....", '6': "-....", '7': "--...",
        '8': "---..", '9': "----.", '\n': ".-.-", ' ': ""
    }
