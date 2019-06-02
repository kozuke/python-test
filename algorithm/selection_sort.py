class Algorithm(object):

    def select_sort(self, target):
        """
        >>> algo=Algorithm()
        >>> a = [2, 6, 4, 1, 3]
        >>> algo.select_sort(a)
        [1, 2, 3, 4, 6]
        """
        for i in range(0, len(target) - 1):
            self.select_min(target, i)
        return target

    def select_min(self, target, i):
        min = i
        for j in range(i + 1, len(target)):
            if target[min] > target[j]:
                min = j
        target[i], target[min] = target[min], target[i]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
