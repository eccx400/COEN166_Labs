S='Spam' # make a 4-character string, and assign it to a name
len(S) # Length
S[0] # the 1st item in S, indexing by zero-based position
S[1] # the 2nd item from the left
S[-1] # the last item from the end in S
S[-2] # the second-to-last item from the end
S[len(S)-1]
S[1:3] # Slice of S from offsets 1 through 2 (not 3)
S = 'z' + S[1:]
S
