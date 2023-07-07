import time
from palindrome import *
from the_string import strings

algo_name = "recursive_algo"

f = open(algo_name+".csv", "a+")

for n_sized_strings in strings:
    for s in n_sized_strings:
        start = time.time()
        #din_palindrome(s)
        rec_palindrome(s, 0, len(s)-1)
        #reset_m(len(s))
        #memo_palindrome(s, 0, len(s)-1)
        end = time.time()
        f.write(f"{len(s)}, {end-start}\n")
        f.flush()

f.close()

        


