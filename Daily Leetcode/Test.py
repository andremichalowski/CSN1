arr = ["a", "b", "c"] # TEST INPUT
# TEST LOOPS HAVE RELATIVE TO ELEMENT
# TEST LOOPS HAVE RELATIVE TO INDEX
    # RANGE
    # LENGTH

#BASE PRINT TEST
def test(n): # CALLING FUNCTION
    print(arr)
test(arr) # INVOKING FUNCTION

# ELEMENT PRINT TEST
def testElementLoop(n):
    for element in n:
        print(element)

testElementLoop(arr)

# INDEX PRINT TEST
def testIndexLoop(n):
    for i, element in n:
        print(n.index(i))

testElementLoop(arr)


