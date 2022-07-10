import math, random
from Soov import Solution
from Human import Human, HairColor

class Solutionv(object):
    def findMedianSortedArrays(self, nums1, nums2):
        newNums = []
        for i in nums1:
            newNums.append(i)
        for i in nums2:
            newNums.append(i)
        newNums.sort()
        if len(newNums) % 2 == 0:
            return float((newNums[int(math.floor(len(newNums)/2 -.5))] + newNums[int(math.ceil(len(newNums)/2-.5))]))/2
        else:
            return float(newNums[int(math.floor(len(newNums)/2))])

class MakeThings(object):
    def createRandomThing(self):
        Nums1 = []
        Nums2 = []
        for i in range(random.randint(1,100)):
            Nums1.append(random.randint(1,10000))
        for i in range(random.randint(1,100)):
            Nums2.append(random.randint(1,10000))
        return Nums1, Nums2
for i in range(100):
    Num1, Num2 = MakeThings.createRandomThing()
    print(Solution.findMedianSortedArrays(Num1, Num2) == Solutionv.findMedianSortedArrays(Num1, Num2))
newHuman = Human(10, 10, HairColor.BLUE)
