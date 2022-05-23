import random
import tempfile


###########################
###########################

def fuzz_generator(max_length=100, char_start=32, char_range=32):
    # TODO: Implement this function
    size = random.choice([max_length, int(max_length/2), int(max_length/4), int(max_length/5), int(max_length/6) ,int(max_length/7)])
    # size = randon.randrange(0, max_length+1)
    return "".join(chr(random.randrange(char_start, char_start+char_range)) for _ in range(size))

# TODO: Implement fuzzer logic

##########################
###########################
import os
import tempfile

def write(file, text, mode="w"):
    with open(file, mode) as ff:
        ff.write(text)

"""file = os.path.join(tempfile.mkdtemp(), "fuzz_input.txt")
print(file)"""

###########################
###########################

import subprocess as sp
def external_programs(program):
    fuzz_input = fuzz_generator()
    file = "fuzz_input.txt"
    # store the fuzz input
    write(file, fuzz_input)

    #not inerested in stdin ve just interested in with stdout (standart output) and stderr(error channel).
    # universal_newlines = True means output in text format
    result = sp.run([program, file], stdin=sp.DEVNULL, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines = True)
    return result


if __name__ == "__main__":
    print(external_programs("bc"))
    print(external_programs("uniq"))
    #print(external_programs("md5sum"))


