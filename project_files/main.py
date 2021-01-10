import time
from multiprocessing import Pool
from project_files import reader


def is_prime(number):
    for i in range(3, number):
        if number % i == 0:
            return 1
    return 0


def f(a_list):
    out = 0.0
    for n in a_list:
        out += is_prime(n)
    return out


def g(args):
    a_list, i, j = args
    out = 0.0
    for number in range(i, j):
        out += is_prime(a_list[number])
    return out


def f_mp(a_list):
    chunks = [(a_list, i, i + 1000) for i in range(0, len(a_list), 1000)]
    pool = Pool(processes=12)
    result = pool.map(g, chunks)
    return sum(result)


def find_mistake_mp(word_list):
    chunks = [word_list[i: i + 1000] for i in range(0, len(word_list), 1000)]
    print(len(chunks))
    pool = Pool(processes=4)
    result = pool.map(reader.find_mistakes, chunks)
    result_set = set()
    for r in result:
        result_set |= r

    return len(result_set)


if __name__ == '__main__':
    text = reader.get_text()
    print(len(text))
    start_mp = time.time()
    print(f"MP RESULTS: {find_mistake_mp(text)}")
    end_mp = time.time()
    start = time.time()
    print(f"Reg RESULTS: {len(reader.find_mistakes(text))}")
    end = time.time()

    print(f"Mp Time :{end_mp - start_mp}")
    print(f"Reg Time :{end - start}")
