# imports
from string import ascii_lowercase as alphabet

def char_teleportation(strng: str) -> str:
    prev = []
    pairs = []
    
    # Get pairs of letters which open portals
    for char_ind, char in enumerate(strng[:-1]):
        if alphabet[::-1].index(strng[char_ind + 1].lower()) == alphabet.index(char.lower()):
            pairs.append((char, strng[char_ind + 1]))
    
    if len(pairs) != 0: # main process: move letters around based on portal
        for pair in pairs:
            if alphabet.index(pair[0].lower()) < alphabet.index(pair[1].lower()):
                strng = strng[:strng.index(pair[1])] + strng[strng.index(pair[1])+1:] + pair[1]
                if strng.index(pair[0]) != 0:
                    strng = strng[strng.index(pair[1]) - 1] + strng

            elif alphabet.index(pair[0].lower()) > alphabet.index(pair[1].lower()):
                strng = pair[1] + strng[:strng.index(pair[1])] + strng[strng.index(pair[1])+1:]
                if strng.index(pair[0]) != 0:
                    strng = strng[strng.index(pair[0]) - 1] + strng[:strng.index(pair[0])-1] + strng[strng.index(pair[0]):]
                    
        if strng in prev: # check if you're in an infinite loop
            print("INDEFINITE")
            return
            
        prev.append(strng)
        char_teleportation(strng) # recursion
        
    elif pairs == []: # exit recursion if there are no more portals
        print(strng)
        return
    
if __name__ == "__main__":
    strng = input()
    char_teleportation(strng)
