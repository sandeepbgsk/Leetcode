from itertools import permutations


class Solution:
    def countArrangement2(self, n: int) -> int:
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
                print(i)
                count = count + 1

        return count

    def countArrangement(self, n: int) -> int:
        if(n==1):
           return 1
        if(n==2):
            return 2
        count = 0
        fibo_list = [1,2]
        for i in range(3,n+1):
            fibo_list.append(fibo_list[i-2] + fibo_list[i-3])

        return fibo_list[-1]


if __name__ == '__main__':
    print(Solution().countArrangement(n=4))
    print(Solution().countArrangement2(n=4))
