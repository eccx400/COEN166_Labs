L=[123, 'spam', 1.23] # A list of three different-type objects
len(L) # number of items in the list
L[0]
L[:-1] # Slicing a list returns a new list
L+[4,5,6] # contact/repeat make new lists too
L*2 # repeat
L # we are not changing the original list
M = ['bb', 'aa', 'cc']
M.sort()
M
M.reverse()
M
M = [[1,2,3], [4,5,6], [7,8,9]] # a list that contains three other lists, 3x3 matrix
M[1] # get row 2
M[1][2] # get row 2, then get item 3 within the row
diag = [M[i][i] for i in [0, 1, 2]]
diag
doubles = [c * 2 for c in 'spam'] 
doubles
list(range(4)) # 0..3 (list() required in 3.X)
list(range(−6, 7, 2)) # −6 to +6 by 2 (need list() in 3.X)
[[x ** 2, x ** 3] for x in range(4)] # Multiple values, “if” filters
[[x, x/2, x * 2] for x in range(−6, 7, 2) if x > 0] 
