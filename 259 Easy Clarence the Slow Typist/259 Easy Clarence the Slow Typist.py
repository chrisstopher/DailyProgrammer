
def slowTypist(ipAddress):
    mapping = {'1':(0,0), '2':(1,0), '3':(2,0),
               '4':(0,1), '5':(1,1), '6':(2,1),
               '7':(0,2), '8':(1,2), '9':(2,2),
               '.':(0,3), '0':(1,3), ' ':(2,3)}

    total = 0
    for i in range(1, len(ipAddress)):
        p0 = mapping[s[i-1]]
        p1 = mapping[s[i]]
        a = p1[0] - p0[0]
        b = p1[1] - p0[1]
        dist = (a*a + b*b) ** 0.5
        total += dist
    print('%.2f' % total +'cm')

s = "219.45.143.143"
slowTypist(s)
