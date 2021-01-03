from itertools import permutations


class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        mylist = range(1,n+1)
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
                count = count + 1

        return count

if __name__ == '__main__':
    print(Solution().countArrangement(n=15))
