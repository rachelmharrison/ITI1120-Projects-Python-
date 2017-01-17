#A4 Part 1
#Rachel Harrison
#8617981

def ap4(m):
    '''
    (2D list)-> 2D List
    determines of m contains an arithmetic progressions of minimum length 4
    progression can be horizontally, vertically, or diagonally
    returns a sorted 2D list of indexes of values in progression
    precondition: m must be a matirx
    '''
    m2=[]
    #test vertivcally
    for i in range(len(m)-3):
        for j in range (len(m[i])):
            if(m[i][j]-m[i+1][j]==m[i+1][j]-m[i+2][j] and m[i+1][j]-m[i+2][j]==m[i+2][j]-m[i+3][j]):
                m2.append([i,j])
                m2.append([i+1,j])
                m2.append([i+2,j])
                m2.append([i+3,j])
                m2=sorted(m2)
                return m2
    
    #test horizonally
    for j in range(len(m[0])-3):
        for i in range (len(m)):
            if(m[i][j]-m[i][j+1]==m[i][j+1]-m[i][j+2] and m[i][j+1]-m[i][j+2]==m[i][j+2]-m[i][j+3]):
                m2.append([i,j])
                m2.append([i,j+1])
                m2.append([i,j+2])
                m2.append([i,j+3])
                m2=sorted(m2)
                return m2

    #test first set of diagonals
    for i in range(len(m)-3):
        for j in range(len(m[i])-3):
            if (m[i][j]-m[i+1][j+1]==m[i+1][j+1]-m[i+2][j+2] and  m[i+1][j+1]-m[i+2][j+2]==m[i+2][j+2]-m[i+3][j+3]):
                m2.append([i,j])
                m2.append([i+1,j+1])
                m2.append([i+2,j+2])
                m2.append([i+3,j+3])
                m2=sorted(m2)
                return m2

    #test second set of diagonals
    for i in range(len(m)-3):
        for j in range(len(m[i])-1,2,-1):
          if (m[i][j]-m[i+1][j-1]==m[i+1][j-1]-m[i+2][j-2] and  m[i+1][j-1]-m[i+2][j-2]==m[i+2][j-2]-m[i+3][j-3]):
              m2.append([i,j])
              m2.append([i+1,j-1])
              m2.append([i+2,j-2])
              m2.append([i+3,j-3])
              m2=sorted(m2)
              return m2
    return m2
        
