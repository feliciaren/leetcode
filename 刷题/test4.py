def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l_p = prices[0]
    maxprofit = 0
    for i in range(1,len(prices)):
        l_p = min(l_p,prices[i-1])
        print(l_p)
        maxprofit = max(prices[i] - l_p, maxprofit)
    return maxprofit
if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))