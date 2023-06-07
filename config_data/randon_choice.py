from random import randint

from lexicon.lexicon import answer, type_answer


def random_choice():
    rand_num = randint(0, 3)
    rand_answer = randint(0, 4)
    return answer[type_answer[rand_num]][rand_answer]
