1. REVERSE STRING IN PLACE:

  for i in range(len(s)//2):
    s[i], s[-i-1] = s[-i-1], s[i]

