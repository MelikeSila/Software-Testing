import string
import random
import tempfile

def fuzz_generator(max_length=100, char_start=32, char_range=32):
    # TODO: Implement this function
    chars = string.ascii_uppercase + "1" + "2" + "3" + "4"
    size = random.choice([max_length, int(max_length/2), int(max_length/4), int(max_length/5), int(max_length/6) ,int(max_length/7)])
    return bytes(''.join(random.choice(chars) for _ in range(size)), 'UTF-8')

# TODO: Implement fuzzer logic

def fuzz():
    """new_key = fuzz_generator()
                fp = tempfile.TemporaryFile()
                fp.write(new_key)
                # read data from file
                fp.seek(0)
                fp.read()
            
                # close the file, it will be removed
                fp.close()"""

    # create a temporary file using a context manager
    with tempfile.TemporaryFile() as fp:
        fp.write(fuzz_generator())
        fp.seek(0)
        fp.read()

    # file is now closed and removed

    # create a temporary directory using the context manager
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
    # directory and contents have been removed

if __name__ == "__main__":
    fuzz()