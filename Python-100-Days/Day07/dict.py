def main():
    scores = {'a': 95, 'b': 78, 'c':82}
    print(scores['a'])

    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))

    scores['a'] = 81
    scores['d'] = 71
    scores.update(d=67, f=86)
    print(scores)

    print(scores.get('e', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('a', 100))
    print(scores.pop('g', 100))
    scores.clear()
    print(scores)
if __name__ == '__main__':
    main()
