# 로또번호 생성기를 작성하고 당첨번호에 따라 순위를 구하는 프로그램
# 5000원치 로또번호를 생성하세요.

import random as rnd
from chapter04.exam02(use) import bubble_sort

def lotto_generator ():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 46))
    return lotto_num


if __name__ == "__main__":
    rnd.seed(4)
    sorted_lotto = list(lotto_generator())
    print("로또번호 : {}".format(bubble_srt(sorted_lotto)))  # 정렬된 결과
    num = rnd.randint(1, 46)
    lotto_num = set()
    for result in lotto_num

    lotto_num.add(num)
    lotto_num.add(rnd.randint(1, 46))
    print("{}\t{}".format(lotto_num, len(lotto_num)))
    set_lotto = lotto_generator()