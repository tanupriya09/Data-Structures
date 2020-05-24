class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def doOverlap(l1, r1, l2, r2):
    if l1.x >= r2.x or l2.x >= r1.x:            # If one rectangle is on left side of other
        return False
    if (l1.y <= r2.y or l2.y <= r1.y):
        return False                             # If one rectangle is above other e
    return True
if __name__== "__main__":
    l1 = Point(0,3)
    r1 = Point(2,0)
    l2 = Point(-4,2)
    r2 = Point(1,-1)
    if (doOverlap(l1, r1, l2, r2)):
        print("Rectangles Overlap")
        def area(l1, l2, r1, r2):
            length = [l1.x, l2.x, r1.x, r2.x]
            width = [l1.y, l2.y, r1.y, r2.y]
            length.sort()
            width.sort()
            area = (length[2] - length[1]) * (width[2] - width[1])
            return area
        print(area(l1,l2,r1,r2))
    else:
        print("Rectangles Don't Overlap")




