"""
Import essentiel au bon fonctonnement
"""
import string
from unidecode import unidecode
#### Fonction secondaire


def ispalindrome(p):
    """
    Fonction vérifiant si le mot p est un palindrome
    """
    p=unidecode(p).replace(" ","").lower().translate(str.maketrans('','',string.punctuation))
    if len(p)==1:
        return True
    if p=="":
        return True
    if p[0]==p[-1]:
        return ispalindrome(p[1:-1])
    return False

def main():
    """
    fonction main
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie","sé - ES"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
