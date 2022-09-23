from string import ascii_lowercase as alphabet

def char_teleportation(strng):
    prev = []
    pairs = []
    
    for char_ind, char in enumerate(strng[:-1]):
        if alphabet[::-1].index(strng[char_ind + 1].lower()) == alphabet.index(char.lower()):
            pairs.append((char, strng[char_ind + 1]))
    if len(pairs) != 0:
        for pair in pairs:
            if alphabet.index(pair[0].lower()) < alphabet.index(pair[1].lower()):
                strng = strng[:strng.index(pair[1])] + strng[strng.index(pair[1])+1:] + pair[1]
                if strng.index(pair[0]) != 0:
                    strng = strng[strng.index(pair[1]) - 1] + strng

            elif alphabet.index(pair[0].lower()) > alphabet.index(pair[1].lower()):
                strng = pair[1] + strng[:strng.index(pair[1])] + strng[strng.index(pair[1])+1:]
                if strng.index(pair[0]) != 0:
                    strng = strng[strng.index(pair[0]) - 1] + strng[:strng.index(pair[0])-1] + strng[strng.index(pair[0]):]
        if strng in prev:
            print("INDEFINITE")
            return
            
        prev.append(strng)
        char_teleportation(strng)
    elif pairs == []:
        print(strng)
        return
    
if __name__ == "__main__":
    strng = input()
    char_teleportation(strng)
        
