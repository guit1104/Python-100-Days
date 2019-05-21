import random

def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''

    for _ in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]

    return code

if __name__ == '__main__':
    print(generate_code(1000))
