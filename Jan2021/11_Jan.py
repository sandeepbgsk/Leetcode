class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = [x for x in nums1 if x != 0]
        if (len(nums2) == 0):
            pass
        elif (len(nums1) == 0):
            nums1 = nums2
        elif (nums1[-1] < nums2[0]):
            nums1 = nums1 + nums2
        elif (nums2[-1] < nums1[0]):
            nums1 = nums2 + nums1
        else:
            for i, e in enumerate(nums1):
                if (e < nums2[0]):
                    pass
                elif (e >= nums2[0]):
                    nums1 = nums1[:i] + [nums2[0]] + nums1[i:]
                    nums2 = nums2[1:]
                    return Solution().merge(nums1, len(nums1), nums2, len(nums2))
        print('Num1 : ' + str(nums1))
        return nums1


if __name__ == '__main__':
    Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=6)
