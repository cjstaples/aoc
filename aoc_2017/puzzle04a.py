import sys
import hashlib


def generate_md5_hash(word):
    md5 = hashlib.md5(word.encode())
    return md5.hexdigest()


def load_puzzle():
    #   with open("data/aoc-2017_puzzle-4_test.txt", "r") as ins:
    with open("data/aoc-2017_puzzle-4_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        phraselist = [i.split(" ") for i in tmp]

    return phraselist


def solve_puzzle(phraselist):
    #   take in phraselist
    #   for each phrase
    #       get wordlist
    #       for each word
    #           generate a hash
    #           add hash to hashlist
    #
    #       once hashlist done
    #           check it for duplicates
    #
    #       if no duplicates
    #           phrase is valid,
    #           increase count
    #
    #   once phraselist is done
    #       return count as answer

    #   print('-- solving for ' + str(phraselist))  # this will get old quickly
    final = 0

    for phrase in phraselist:
        wordlist = phrase
        hashlist = []
        is_valid = False

        for word in wordlist:
            #   print(word)
            hash = generate_md5_hash(word)
            #   print(hash)
            #   print('')
            hashlist.append(hash)

        is_valid = check_duplicates(hashlist)
        if is_valid:
            final += 1

    return final


def check_duplicates(hashlist):
    #   print('')
    #   print('hashlist: ', hashlist)

    hashcounts = {}
    is_valid = False

    for i in hashlist:
        hashcounts[i] = hashlist.count(i)
    #    print('hashcounts: ', hashcounts)

    maxval = max(zip(hashcounts.values(), hashcounts.keys()))
    if maxval[0] == 1:
        is_valid = True

    return is_valid


def show_puzzle(output):
    print('')
    print('solution: ', output)


def main():
    print('(puzzle04a) main:')
    print('')

    mydata = load_puzzle()

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle04a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
