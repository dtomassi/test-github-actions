import sys


def bfs(l, val):
    if not len(l):
        return -1
    low, high = 0, len(l)

    while low < high:
        mid = (low + high) // 2
        if l[mid] > val:
            high = mid
        elif l[mid] < val:
            low = mid
        else:
            return val
    return -1


def _validate_input(argv):
    if len(argv) != 3:
        print('Incorrect number of arguments. Exiting')
        sys.exit(1)
    array = [int(v) for v in argv[1].strip('[]').split(',')]
    value = int(argv[2])
    return array, value


def main(argv=None):
    if argv is None:
        argv = sys.argv
    list_nums, value = _validate_input(argv)

    bfs_ret = bfs(list_nums, value)
    print('Value {} in list'.format(bfs_ret)) if bfs_ret != -1 else print('Value {} not in list'.format(value))


if __name__ == '__main__':
    sys.exit(main())
