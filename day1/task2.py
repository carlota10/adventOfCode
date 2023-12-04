from word2number import w2n


def find_numbers(sentence):
    nums_dict = {}
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine']

    for number in numbers:
        positions = [i for i in range(len(sentence)) if sentence.startswith(number, i)]

        if positions:
            nums_dict[number] = {'max': max(positions), 'min': min(positions)}

    return nums_dict


def get_min_max(nums_dict):
    if not nums_dict:
        return None, None

    key_min = min(nums_dict, key=lambda k: nums_dict[k]['min'])
    key_max = max(nums_dict, key=lambda k: nums_dict[k]['max'])

    return key_min, key_max


def concat_min_max(minimum, maximum):
    try:
        first = w2n.word_to_num(minimum)
        last = w2n.word_to_num(maximum)
        concatenated_value = int(str(first) + str(last))
        return concatenated_value
    except ValueError:
        return 0


def main(filename):
    total = 0

    with open(filename, 'r') as f:
        for line in f:
            positions = find_numbers(line)
            min_num, max_num = get_min_max(positions)
            concatenated_value = concat_min_max(min_num, max_num)
            total += concatenated_value

    print(total)


def test(line):
    positions = find_numbers(line)
    minim, maxim = get_min_max(positions)
    num = concat_min_max(minim, maxim)
    print(num)


test('4mmbddbxnb')

main('input.txt')
