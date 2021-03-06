def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')

    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    print(get_suffix('foo.txt'))
    print(get_suffix('bar.cpp', True))
