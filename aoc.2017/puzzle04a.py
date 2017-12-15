import sys
import hashlib


def generate_md5_hash(word):
    md5 = hashlib.md5(word)
    return md5.hexdigest()

def load_puzzle():
    phrases = []
    phrases.append('aa bb cc dd ee')
    phrases.append('aa bb cc dd aa')
    phrases.append('aa bb cc dd aaa')

    words = 'aa bb cc dd ee'
    # chars = 'aa bb cc dd aa'
    # chars = 'aa bb cc dd aaa'

    return words


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    final = 0
    wordlist = list(indata.split())
    hashlist = []

    for word in wordlist:
        print(word)
        hash = generate_md5_hash(word)
        print(hash)
        print('')
        hashlist.append(hash)

    return final


def show_puzzle(output):
    print('')
    print('solution: ',output)


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
