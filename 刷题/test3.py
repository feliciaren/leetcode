def beat_monster(n,w,m):
    dc = {}
    totalpower = 0
    result = 0
    count = 0
    dc[str(m[0]* 1.0/ w[0])] = 0
    for i in range(1,n):
        print('round',i)
        if totalpower < w[i]:
            totalpower2 = totalpower
            count2 = count
            result2 = result
            while(totalpower2 < w[i]):
                cur_key = sorted(dc.keys())[count2]
                totalpower2 += w[dc[cur_key]]
                result2 += m[dc[cur_key]]
                count2 += 1
                print('2',cur_key,dc[cur_key],totalpower2,result2,count2)
            if result2 > result + m[i]:
                print('1')
                result += m[i]
                totalpower += w[i]
                print('1',totalpower)
            else:
                print('222')
                count = count2
                result = result2
                totalpower = totalpower2
        dc[str(m[i]* 1.0/ w[i])] = i
    return result


if __name__ == '__main__':
    
    print(beat_monster(4,[3,2,1,5],[2,3,1,7]))