import time
from multiprocessing import Pool
from project_files import reader


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
    print(f"Reg RESULTS: {reader.find_mistakes(text)}")
    end = time.time()

    print(f"Mp Time :{end_mp - start_mp}")
    print(f"Reg Time :{end - start}")
