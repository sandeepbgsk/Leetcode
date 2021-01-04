from itertools import permutations


class Solution:
    def countArrangement2(self, n: int) -> int:
        count = 0
        mylist = list(range(1, n + 1))
        mylist = mylist[::-1]
        perm = list(permutations(mylist))
        for i in perm:
            flag = True
            for index, ele in enumerate(i):
                if ((ele % (index + 1)) == 0) or (((index + 1) % ele) == 0):
                    pass
                else:
                    flag = False
                    break
            if flag:
                print(i)
                count = count + 1

        return count

    def countArrangement(self, n: int) -> int:
        prod = 1
        for i in range(1, n + 1):
            prod = prod * int(n / i)
        return prod


if __name__ == '__main__':
    print(Solution().countArrangement(n=7))
    print(Solution().countArrangement2(n=15))
