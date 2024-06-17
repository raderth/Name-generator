import random

length = {5:1,6:1,7:17,8:46,9:30,10:5} # This is the approximate distribution of place names' lengths
vowels = {'E': 12.02, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'U': 2.88} # I pulled these numbers from the probability of a letter being in a word
consonants = {'T': 9.10, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07}
sum_length = sum(length[i] for i in length)
sum_vowels = sum(vowels[i] for i in vowels)
sum_cononants = sum(consonants[i] for i in consonants)

combos_to_avoid_like_the_plague = ["OAH","BAO","AVI","IEG","TUI","OIR","EYI","IDG","UHO","RTV","IFT","IUH","NKA","AIY","PB","OGF","AEY","OAY","IOD","UOT","RWO","EAY","IOM","OBT","EHA","INP","UES","IEH","GSI","AVL","YAI","AUC","EUM","DIU","IRT","AIH","EOD","ATUH","AB","RIR","DOA","IWN","EYT","AED","EOR","EC","OEN","ASN","UED","BHE","II","IUG","IAS","OAG","IOR","AOP","OEV","IAH","IOY","EUTN","ERV","ICW","SNIO","YBE","YMI","AX","AAN","UU","UOF","HH","KWI","IUW","EIW","EIH","UDW","FDA","EOH","LW","APU","OIY","MHI","IOH","RYI","AOF","NN", "XK", "PT", "BV", "QW", "ZX", "VX", "VW", "VF", "GV", "ZV", "VV", "FV", "YH", "EHY", "HIH", "YC", "TG", "EEH", "WEE", "IGT", "IDF", "EIG", "PYT", "LH", "NC"]
doubles_to_reduce = ["AA", "BB", "CC", "EE", "GG", "HH", "JJ", "KK", "PP", "QQ", "RR", "UU", "VV", "WW", "XX", "YY", "ZZ","TT"]

word = ""

def random_option(dict,total): # Picks a random choice from the dictionary using the numbers as weights
    total_percent = 0
    rand = random.random()*total
    for key, i in dict.items():
        total_percent += i
        if rand <= total_percent:
            return key

def find_word():
    vowel = None
    vowel_last_time = None
    vowel_time_before_last = None
    lword = ""
    for i in range(random_option(length, sum_length)):
        if vowel_last_time == vowel_time_before_last: # if two of any type in a row
            vowel = not vowel_last_time
        else:
            vowel = False if random.randrange(3) == 0 else True

        if vowel:
            lword += random_option(vowels,sum_vowels)
        else:
            lword += random_option(consonants,sum_cononants)

        vowel_time_before_last = vowel_last_time
        vowel_last_time = vowel
    return(lword)

for i in range(10):
    repeat = True
    while repeat:
        repeat = False
        word = find_word()
        found = False
        while found == False:
            found = True
            for i in combos_to_avoid_like_the_plague:
                if i in word:
                    print("Bad Combo " + i + " - " + word)
                    if len(word) >= 7:
                        word = word.replace(i, "")
                    else:
                        word = find_word()
                    found = False
        # final checks
        has_doubles = True
        while has_doubles:
            has_doubles = False
            for i in doubles_to_reduce:
                if i in word:
                    print("Double Letter " + i + " - " + word)
                    word = word.replace(i, i[0])
                    has_doubles = True

        if len(word) < 5:
            repeat = True
            print(word + " is unsalvagable")

    print(word)