class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        #[(7,2),(10,1),(19,3)]
        arr=[(price[i],i+1) for i in range(n)]
        arr.sort()
        # print(arr)
        # return 0
        total_stocks=0
        for cost,day in arr:
            # print(f"{cost} and {day}")
            if cost*day<=k:
                total_stocks+=day
                k-=cost*day
            else:
                total_stocks+=int(k/cost)
                break
        return total_stocks
