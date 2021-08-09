"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    first_word = ""
    if text == "":
        return ""
    elif text[0].isupper(): 
        return text.title().replace("-","").replace("_","")
    else:
        for l in text:
            if l.islower():
                first_word += l
            else:
                break
        return first_word + text[len(first_word):].title().replace("-","").replace("_","")
