class Comparator:

    def make_comparator(dict):
        def compare(x, y):
            if dict(x[1], y[1]):
                return 1
            elif x[1] == y[1]:
                return 0
            else:
                return -1
        return compare

    def cmpValue(subInfo1, subInfo2):
        if subInfo1 > subInfo2:
            return True
        else:
            return False