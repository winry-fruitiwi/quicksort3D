# quicksort visualization
# winry 2021.07.08
# v0.1 recursive quicksort with good comments
# v0.2 iterative quicksort in separate method using call stack
# v0.3 visualize iterative quicksort with rectangles
# v0.4 visualize with boxes in 3D

def recursive_quicksort(lst, start, stop): # end turns out to be a Processing builtin so I'm avoiding it!
    # base case: if the list's length is less than two, return.
    # This is an out-place sort, if such a phrase exists.
    if start >= stop:
        return
    
    # let's define our variables!
    # l_ptr is the less than pointer, which we will use later in the partitioning step. We use it to keep track
    # of where the lesser than values are.
    l_ptr = start
    # the pvt is the pivot value, which we will compare to other elements in the partitioning step loop.
    pvt = lst[stop]
    
    # let's start partitioning! We should get a list where all the elements to the left of the pivot are lesser
    # than it and everything to the right is greater than the pivot.
    for i in range(start, stop):
        # we need to check for elements less than a pivot. If there are:
        if lst[i] < lst[stop]:
            # we need to increment the less than pointer so that we achieve the goal we set before this loop.
            # But first, we need to swap whatever's at the pointer with our current element!
            lst[i], lst[l_ptr] = lst[l_ptr], lst[i] # one of my common mistakes is not swapping at all!
            l_ptr += 1
    
    # Phew, that was a long loop! But before we go out of loop business, we should swap the end with the l_ptr
    # to ensure that the pivot is in the right place.
    lst[stop], lst[l_ptr] = lst[l_ptr], lst[stop]
    
    # Ok, one more complicated obstacle before we can get out of this function: the recursive calls!
    # We need to get two recursive calls that both exclude the pivot.
    recursive_quicksort(lst, start, l_ptr - 1)
    recursive_quicksort(lst, l_ptr + 1, stop)


def iterative_quicksort(lst, start, stop): # end turns out to be a Processing builtin so I'm avoiding it!
    # we want to keep track of all of our calls. Guess what that structure is? A call stack!
    stack = [(start, stop)]
    
    while stack:
        (start, stop) = stack.pop()
        # base case: if the list's length is less than two, return.
        # This is an out-place sort, if such a phrase exists. But be careful! We need to get out of this loop.
        if start >= stop:
            continue
        
        # let's define our variables!
        # l_ptr is the less than pointer, which we will use later in the partitioning step. We use it to keep 
        # track of where the lesser than values are.
        l_ptr = start
        # the pvt is the pivot value, which we will compare to other elements in the partitioning step loop.
        pvt = lst[stop]
        yield
        # let's start partitioning! We should get a list where all the elements to the left of the pivot are 
        # lesser than it and everything to the right is greater than the pivot.
        for i in range(start, stop):
            # we need to check for elements less than a pivot. If there are:
            yield
            if lst[i] < lst[stop]:
                # we need to increment the less than pointer so that we achieve the goal we set before this loop
                # But first, we need to swap whatever's at the pointer with our current element!
                lst[i], lst[l_ptr] = lst[l_ptr], lst[i] # one of my common mistakes is not swapping at all!
                l_ptr += 1
                yield
        
        # Phew, that was a long loop! But before we go out of loop business, we should swap the end with the
        # to ensure that the pivot is in the right place.
        lst[stop], lst[l_ptr] = lst[l_ptr], lst[stop]
        yield
        # Ok, one more complicated obstacle before we can get out of this function: the recursive calls!
        # We need to get two recursive calls that both exclude the pivot.
        # recursive_quicksort(lst, start, l_ptr - 1)
        # recursive_quicksort(lst, l_ptr + 1, stop)
        # Swish swish aroo! Ok I swept those recursive quicksort things into the bucket. Let's start iterating!
        # We want the same parameters in quicksort's stack.
        stack.append((start, l_ptr - 1))
        stack.append((l_ptr + 1, stop))

'''
# This is my test code. We have no need for it now.
test = []

for i in range(1, 100):
    test.append(int(random(1, 50)))

print(test)
iterative_quicksort(test, 0, len(test) - 1)
print(test)

'''

def setup():
    global lst, sorter
    frameRate(16)
    colorMode(HSB, 360, 100, 100, 100)
    background(220, 79, 35)
    size(800, 400, P3D)
    
    lst = []
    for i in range(55):
        lst.append(int(random(10, 301)))
        #lst.append(i)
    print(lst)
    
    sorter = iterative_quicksort(lst, 0, len(lst) - 1)
    
    
def draw():
    global lst, sorter
    background(220, 79, 35)
    fill(0, 0, 100, 70)
    
    # this is the width of each block
    w = 10
    # this is the gap between each block
    gap = 3
    
    for i in range(len(lst)):
        pushMatrix()
        translate(50 + (w + gap)*i, 350)
        rect(0, 0, w, -lst[i])
        popMatrix()
    
    try:
        sorter.next()
    except:
        print(lst)
        noLoop()
