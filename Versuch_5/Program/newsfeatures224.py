# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np

debug = False

#A and B are of type numpy.matrix
#returns the summed euclidean distance of the passed matrices
def cost(A, B):
    #TODO test if the matrices are of same shape
    k = 0
    """
    print "Matrix A:"
    pp.pprint(A)
    print '-' * 64, "\nMatrix B:"
    pp.pprint(B)

    print '-' * 64, "\n", '-' * 64
    """

    #create iterators
    iteratorA = A.flat
    iteratorB = B.flat

    try:
        while True:
            #iterate over all elements in both matrices
            Aij = iteratorA.next()
            Bij = iteratorB.next()
            k += pow(Aij - Bij, 2)
            #print "Aij=%d | Bij=%d" % (Aij, Bij)

    except StopIteration:
        pass  #needed because the iterator does not know if there are more elements coming

    return k


# Calculate NNMF
# parameters:
#     A: non-negative Matrix
#     m: count of merkmal
#     it: number of iterations
# returns: {
#     H: Merkmalsmatrix
#     W: Gewichtsmatrix
# }
def nnmf(A, m, it):
    #get row count and column count of A
    r, c = A.shape

    #step 2:
    ## assert that m < c, else: throw exception
    if m >= c:
        #throw Argument Error
        print "nnmf throws argument Error: m must be smaller than c (count of columns)"
        return

    #step 3+4:
    #initialize matrices H and W
    H = np.matrix(np.random.randint(1, 7, (m, c))) #0 needs to be excluded
    W = np.matrix(np.random.randint(1, 7, (r, m))) #0 needs to be excluded

    if debug:
        print "shape of H: ", H.shape, "\nshape of W: ", W.shape
        pp.pprint({'H': H, 'W': W})

    #step 5:
    while it > 0:
        #calculate current product of H and W
        #a)
        B = W * H
        k = cost(A, B)

        if not debug:
            pp.pprint({'A': A, 'B': B})
            print "cost: %d" % k

        #break if desired matrix and factorized matrix are very similar
        if k < 5:
            break

        #b) recalculate H
        # Hij = Hij * (W_transposed * A)ij / (W_transposed * W * H)ij
        temp1 = np.array(W.T * A)
        temp2 = np.array(W.T * W * H)
        H = np.matrix( np.array(H) * np.true_divide(temp1, temp2) ) #normal divide floors the results

        if not debug:
            print "shape of H: ", H.shape, "H:"
            pp.pprint(H)

        #c) recalculate W
        #Wij = Wij * (A * H_transposed)ij / (W * H * H_transposed)ij
        nextW = np.array(W) * np.true_divide(np.array(A * H.T), np.array(W * H * H.T)) #normal divide floors the results
        W = np.matrix( nextW )


        it -= 1
        if not debug:
            print "current values: (%d more iterations)\n" % it
            print "W:\n", W, "\nH:\n", H
            print "-"*64

    #return {'H': H, 'W': W}
    return W, H


if __name__ == "__main__":
    A = np.matrix([[1, 2, 3], [0, 0, 2], [2, 0, 1], [2, 0, 0]])

    result = nnmf(A, 2, 3)
    W, H = result

    print "\n", "-"*64, "\nresult:\nW:\n", W, "\nH:\n", H


    pass