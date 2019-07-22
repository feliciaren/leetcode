def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n = len(word1) + 1
    m = len(word2) + 1
    matrix = []
    matrix.append(list(range(n))) 
    for i in range(1,m):
    	matrix.append([0]*n)
    	matrix[i][0] = i
    	for j in range(1,n):
    		if word1[j-1] == word2[i-1]:
    			temp = 0
    		else:
    			temp = 1
    		matrix[i][j] = min(matrix[i-1][j-1]+temp,matrix[i][j-1]+1,matrix[i-1][j]+1)
    	print(matrix)
    return matrix[-1][-1]

if __name__ == '__main__':
	print(minDistance('rose','horse'))