#!/usr/bin/env python3

def add(*args):
    def add_pair(m1, m2):
        if len(m1) != len(m2):
            raise ValueError("Given matrices are not the same size.")

        result = list()

        for l, r in zip(m1, m2):
            if len(l) != len(r):
                raise ValueError("Given matrices are not the same size.")

            row = list()
            for i in range(len(l)):
                row.append(l[i] + r[i])

            result.append(row)

        return result

    result = list(args[0])

    for m in args[1:]:
        result = add_pair(result, m)

    return result


if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(add(matrix1, matrix2))

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print(add(matrix1, matrix2))
