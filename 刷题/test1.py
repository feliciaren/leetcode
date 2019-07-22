def findposition(input1,input2,input3):
    pos = [0 for i in range(input1)]
    head = 0
    for i in range(input2):
        print(i)
        if input3[i][0] == 1:
            pos[head] = 1
            for i in range(head,input1,1):
                if i!= 0:
                    head = i
                    break;
        if input3[i][0] == 2:
            pos[input3[i][1]] = 1
            if head == input3[i][1]:
                for i in range(head,input1,1):
                    if i!= 0:
                        head = i
                        break;
        if input3[i][0] == 3:
            return input3[i][1] - sum(pos[:input3[i][1]])
        return 0
if __name__ == "__main__":
    input1 = 5
    input2 = 1
    input3 = [[1,0]]
    print(findposition(input1,input2,input3))