import sys
from math import log, factorial, ceil

"""
$ python big_o_arithmetic_progression.py.py
Qtd objects: n | Constant: O(1) | Logarithmic: O(log n) | Linear: O(n) | N-Log-N O(n * log n): | Quadratic: O(n²) | Cubic: O(n³) | Exponential: O(2^n) | Factorial: O(n!)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1              | 1              | 1                     | 1            | 1                     | 1                | 1            | 2                   | 1
2              | 1              | 1                     | 2            | 2                     | 4                | 8            | 4                   | 2
3              | 1              | 1.58                  | 3            | 4.75                  | 9                | 27           | 8                   | 6
4              | 1              | 2                     | 4            | 8                     | 16               | 64           | 16                  | 24
5              | 1              | 2.32                  | 5            | 11.61                 | 25               | 125          | 32                  | 120
6              | 1              | 2.58                  | 6            | 15.51                 | 36               | 216          | 64                  | 720
7              | 1              | 2.81                  | 7            | 19.65                 | 49               | 343          | 128                 | 5040
8              | 1              | 3                     | 8            | 24                    | 64               | 512          | 256                 | 40320
9              | 1              | 3.17                  | 9            | 28.53                 | 81               | 729          | 512                 | 362880
10             | 1              | 3.32                  | 10           | 33.22                 | 100              | 1000         | 1024                | 3628800
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
50             | 1              | 5.64                  | 50           | 282.19                | 2500             | 125000       | 1.125899e+15        | 3.041409e+64
100            | 1              | 6.64                  | 100          | 664.39                | 10000            | 1000000      | 1.267650e+30        | 9.332621e+157
1000           | 1              | 9.97                  | 1000         | 9965.78               | 1000000          | 1000000000   | 1.071508e+301       | 4.023872e+2567
10000          | 1              | 13.29                 | 10000        | 132877.12             | 100000000        | 1.000000e+12 | 1.995063e+3010      | 2.846259e+35659
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
8              | 1              | 3                     | 8            | 24                    | 64               | 512          | 256                 | 40320
16             | 1              | 4                     | 16           | 64                    | 256              | 4096         | 65536               | 2.092278e+13
32             | 1              | 5                     | 32           | 160                   | 1024             | 32768        | 4294967296          | 2.631308e+35
64             | 1              | 6                     | 64           | 384                   | 4096             | 262144       | 1.844674e+19        | 1.268869e+89
128            | 1              | 7                     | 128          | 896                   | 16384            | 2097152      | 3.402823e+38        | 3.856204e+215
256            | 1              | 8                     | 256          | 2048                  | 65536            | 16777216     | 1.157920e+77        | 8.578177e+506
512            | 1              | 9                     | 512          | 4608                  | 262144           | 134217728    | 1.340780e+154       | 3.477289e+1166

"""

sys.set_int_max_str_digits(0)


def print_artimetic_table(qtd_objects):
    artimetic_table = []
    for n in qtd_objects:
        # generate arithmetics progressions
        arithmetic_progressions = [n, 1, log(n, 2), n, n * log(n, 2), n ** 2, n ** 3, 2 ** n, factorial(n)]
        # format display numbers
        formated_line_progression = []
        for progression in arithmetic_progressions:
            # if less then 1 round to 1
            # progression = progression 
            # force int type for float with 0 decimals
            progression_int = int(progression)
            progression_str = str(progression_int) if progression_int == progression else '{0:.2f}'.format(progression)



            
            # apply notation for large numbers with max str digits
            if len(progression_str.split('.')[0]) > 10:
                progression = f'{progression_str[0]}.{progression_str[1:3]}e+{len(progression_str) - 1}'


            elif '.' in progression_str:
                progression = f'{ceil(progression)} ({progression_str})'
            elif progression < 1:
                progression = f'1 ({progression_str})'

            else:
                progression = progression_int



            formated_line_progression.append(progression)
        # define final table
        artimetic_table.append(formated_line_progression)
    for line_args in artimetic_table:
        print("{:<14} | {:<14} | {:<21} | {:<12} | {:<21} | {:<16} | {:<12} | {:<19} | {}".format(*line_args))


if __name__ == '__main__':
    print('Qtd objects: n', '| Constant: O(1)', '| Logarithmic: O(log n)', '| Linear: O(n)', '| N-Log-N O(n * log n):',
          '| Quadratic: O(n²)', '| Cubic: O(n³)', '| Exponential: O(2^n)', '| Factorial: O(n!)')
    max_line_chars = 175
    print('-' * max_line_chars)
    print_artimetic_table([i for i in range(1, 11)])
    print('-' * max_line_chars)
    print_artimetic_table([50, 100, 1000, 10000])
    print('-' * max_line_chars)
    print_artimetic_table([8, 16, 24, 32, 64, 128, 256, 512])
