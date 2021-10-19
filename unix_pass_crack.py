import crypt

def ciph_pass(passwd):
    return crypt.crypt('egg', 'HX')

def testPass(crypt_pass):
    salt = crypt_pass[0:2]
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.