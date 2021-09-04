from string import ascii_lowercase as alphabet
import time


def get_alphabet_list():
    a_to_z = []
    for letter in alphabet:
        a_to_z.append(letter)
    return a_to_z


def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    result = []
    for char in word:
        for index, letter in enumerate(alphabet):
            # print(index, letter)
            if letter == char:
                if index + shift >= 25:
                    x = (index + shift) - index - (25 - index)
                    index = x
                    # print(alphabet[x - 1], end=' ')
                    result.append(alphabet[index-1])
                else:
                    # print(alphabet[index + shift], end=' ')
                    result.append(alphabet[index + shift])
    return ''.join(result)


# print(shift_characters('abby', 5))


def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    shifted = [word]
    for _ in range(shift):
        shifted_word = shift_characters(word, shift)
        shifted.append(shifted_word)
        word = shifted_word
    shifted = ''.join(map(str, shifted))
    return shifted[:n]


# print(pad_up_to('abb', 5, 11))


def abc_mirror(word):
    """
    >>> abc_mirror('abcd') SAU abc_mirror('morpheus')
    'zyxw' SAU 'nliksvfh'

index[0]   a    z     => a = alfabet[-(0+1)] => alfabet[-1] = z
index[1]   b    y     => b = alfabet[-(1+1)] => alfabet[-2] = y
index[2]   c    x     => c = alfabet[-(2+1)] => alfabet[-3] = x
index[3]   d    w
index[4]   e    v
index[5]   f    u
index[6]   g    t
index[7]   h    s
index[8]   I    r
index[9]   j    q
index[10]  k    p
index[11]  l    o
index[12]  m    n
    """

    mirrored_word = []
    a_to_z = get_alphabet_list()
    for char in word:
        for index, letter in enumerate(a_to_z):
            if letter == char:
                mirrored_letter = a_to_z[-(index+1)]
                mirrored_word.append(mirrored_letter)
    return ''.join(mirrored_word)


# print(abc_mirror('morpheus'))


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """

    values = []
    for char in word2:
        for index, letter in enumerate(alphabet):
            if char == letter:
                values.append(shift_characters(word1, index))
    return values


# print(create_matrix('mamas', 'papas'))


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """

    result = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix)):
            result.append(matrix[j][i])
    result = result[:4] + list(reversed(result[4:8])) + result[8:]
    return ''.join(result)


# print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    list_of_letters = []
    for letter in word:
        list_of_letters.append(letter)
    lenght = len(list_of_letters)

    list_of_letters = list_of_letters[-(lenght + n) %
                                      lenght:] + list_of_letters[0:-(lenght + n) % lenght]
    return ''.join(list_of_letters)


# print(rotate_right('abcdefgh', 3))


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    square_index_chars = []
    for index in range(len(word)):
        if index * index > len(word):
            break
        square_index_chars.append(word[index*index])
    return ''.join(square_index_chars)


# print(get_square_index_chars('abcdefghijklm'))


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    sliced_words = []
    even_words = []
    count = 0
    for _ in range(5):
        sliced_words.append(word[count:count + block_length])
        count += 3
    for index in range(len(sliced_words)):
        if index % 2 == 0:
            even_words.append(sliced_words[index])
    return ''.join(even_words)


# print(remove_odd_blocks('abcdefghijklm', 3))


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    first_n_letters = []
    for letter in word[:n]:
        first_n_letters.append(letter)
    length = len(first_n_letters)
    first_n_letters = first_n_letters[(
        length + (length // 2) - 1) % length:] + first_n_letters[0:(n + (length // 2) - 1) % n]  # !

    return ''.join(list(reversed(first_n_letters)))


# print(reduce_to_fixed('abcdefghijklm', 6))


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    time.sleep(1)
    # print(padded)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    time.sleep(1)
    # print(elongated)
    rotated = rotate_right(elongated, 3000003)
    time.sleep(1)
    # print(rotated)
    cherry_picked = get_square_index_chars(rotated)
    time.sleep(1)
    # print(cherry_picked)
    halved = remove_odd_blocks(cherry_picked, 3)
    time.sleep(1)
    # print(halved)
    key = reduce_to_fixed(halved, 6)
    time.sleep(1)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
