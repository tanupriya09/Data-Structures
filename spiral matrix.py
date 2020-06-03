def spiral_matrix(a):
    start_column = 0 ; start_row = 0
    end_column = len(a[0])
    end_row = len(a)
    while start_row<end_row and start_column<end_column:
        for i in range(start_column,end_column):
            print(a[start_row][i],end=" ")
        start_row += 1
        for i in range(start_row,end_row):
            print(a[i][end_column-1],end=" ")
        end_column -= 1
        if start_row<end_row:
            for i in reversed(range(start_column,end_column)):
                print(a[end_row-1][i],end=" ")
        end_row -= 1
        if start_column<end_column:
            for i in reversed(range(start_row,end_row)):
                print(a[i][start_column],end=" ")
        start_column += 1
a = ([1,2,3],[4,5,6],[7,8,9],[10,11,12])
a = [[1,2,3,4,5]]
a = [[1],[2],[3],[4],[5]]
a = [[1]]
spiral_matrix(a)
