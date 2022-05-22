import string
import random

def fuzz_generator(max_length=100, char_start=32, char_range=32):
    # TODO: Implement this function
    chars = string.ascii_uppercase + "1" + "2" + "3" + "4"
    size = random.choice([max_length, int(max_length/2), int(max_length/4), int(max_length/5), int(max_length/6) ,int(max_length/7)])
    print(size)
    return ''.join(random.choice(chars) for _ in range(size))

# TODO: Implement fuzzer logic

def main():
    print(fuzz_generator(100))

if __name__ == "__main__":
    main()