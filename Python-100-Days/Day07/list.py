def main():
    list1 = [1, 3, 3, 5, 7, 100];
    # print(list1)
    # list2 = ['hello'] * 5
    # print(list2)
    # print(list1[-3])
    # list1[2] = 31
    # print(list1)
    # list1.append(313)
    # list1.insert(1, 400)
    # list1 += [1000, 2000]
    #
    # print(list1)
    #
    # list1.remove(3)
    # print(list1)
    #
    # del list1[0]
    # print(list1)
    # list1.clear()
    # print(list1)
    #
    # fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    # fruits += ['pitaya', 'pear', 'mango']
	# # 循环遍历列表元素
    # for fruit in fruits:
    #     print(fruit.title(), end=' ')
    # print()
    #
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)

    list1.sort(reverse=True)
    print(list1)
if __name__ == '__main__':
    main()
