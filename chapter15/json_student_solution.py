def prn_dict_bubble_sorted(_dict):
    count = False
    _key_list = list(_dict.keys())
    _value_list = list(_dict.values())
    last = len(_dict)
    for i in range(0, last - 1):
        for j in range(0, last - 1 - i):
            if _value_list[j] < _value_list[j + 1]:
                swap(_value_list, j, j + 1)
                swap(_key_list, j, j + 1)
                count = True
        if not count:
            print_dict(_key_list, _value_list)
            return
        else:
            count = False

    print_dict(_key_list, _value_list)
    return


def pop_dictItem(_dict, _threshold):
    _key_list = []
    for _key, _value in _dict.items():
        if _value <= _threshold:
            _key_list.append(_key)
    for _key in _key_list:
        _dict.pop(_key)


def print_dict(_key_list, _value_list):
    for _key, _value in zip(_key_list, _value_list):
        print("word_dict[{}] = {}".format(_key, _value))


def swap(_list, _curr, _next):
    temp = _list[_curr]
    _list[_curr] = _list[_next]
    _list[_next] = temp


if __name__ == "__main__":
    filename = "Gettysburg_Address.txt"
    word_dict = {}

    with open(filename, 'rt') as f:
        print("First line of '{}' is\n{}".format(filename, f.readline()), end='')
        for line in f:
            for word in line.split():
                word = word.strip('.,-')
                if word:
                    word_dict[word] = word_dict.get(word, 0) + 1

    pop_dictItem(word_dict, 2)
    print("\n*****단어 별 내림차순 빈도*****")
    prn_dict_bubble_sorted(word_dict)

    count = 0
    for i in word_dict:
        count += 1
    print("출력된 단어 개수 :", count)