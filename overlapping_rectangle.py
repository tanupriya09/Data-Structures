"""(x1,y1)=(0,0)
(x2,y2)=(2,3)
(x3,y3)=(0,0)        #Overlapping
(x4,y4)=(1,2)"""

(x1,y1)=(-3,-2)
(x2,y2)=(2,4)
(x3,y3)=(-5,-6)        #Overlapping
(x4,y4)=(4,6)

"""(x1,y1)=(0,0)
(x2,y2)=(6,7)
(x3,y3)=(8,9)        # Not Overlapping
(x4,y4)=(9,10)

(x1,y1)=(-2,-1)
(x2,y2)=(3,3)
(x3,y3)=(-5,4)        # Not Overlapping
(x4,y4)=(-3,7)

(x1,y1)=(-2,0)
(x2,y2)=(1,2)
(x3,y3)=(-4,-2)        # Not Overlapping
(x4,y4)=(-3,1)"""
if (x2-x1)>(x4-x3) and (y2-y1)>(y4-y3):
    if x1<x3<x4 or y1<y3<y4:
        if x3>x2 or y3>y2:
            print("Not Overlapping")
        else:
            print("overlapping")
    elif x3<x4<x2 or y3<y4<y2:
        if x1>x4 or y1>y4:
            print("Not Overlapping")
        else:
            print("overlapping")
else:
    if x3<x1<x4 or y3<y1<y4:
        if x1>x4 or y1>y4:
            print("Not Overlapping")
        else:
            print("Overlapping")
    elif x1<x2<x3 or y1<y2<y3 :
        if x3>x2 or y3>y2:
            print("Not Overlapping")
        else :
            print("Overlapping")







