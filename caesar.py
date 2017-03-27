
def alphabet_position(letter):
    alpha1 = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in letter:

        if char in alpha1:

            return alpha1.index(char)

        if char in alpha2:

            return alpha2.index(char)


def rotate_character(char, rot):


    alpha3 = "abcdefghijklmnopqrstuvwxyz"
    alpha4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in char:
        if char in alpha3:

            return alpha3[(alphabet_position(char) + rot) % 26]

        elif char in alpha4:

            return alpha4[(alphabet_position(char) + rot) % 26]

        else:

            return char

def encrypt(text, rot):

    alpha3 = "abcdefghijklmnopqrstuvwxyz"
    alpha4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    place = ""
    for char in text:
        if char in alpha3:

            final = alpha3[(alphabet_position(char) + rot) % 26]

        elif char in alpha4:

            final = alpha4[(alphabet_position(char) + rot) % 26]

        else:

            final = char

        place = place + final

    return place
