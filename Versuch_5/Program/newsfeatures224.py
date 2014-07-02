# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np

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
    H = np.random.randint(0, 6, (m, c))
    H = np.matrix(H)

    W = np.random.randint(0, 6, (r, m))
    W = np.matrix(W)
    print "shape of H: ", H.shape, "\nshape of W: ", W.shape

    pp.pprint({'H': H, 'W': W})

    #step 5:
    while it > 0:
        #calculate current product of H and W

        #a)
        B = W * H
        print "shape of B: ", B.shape

        k = cost(A, B)
        pp.pprint({'A': A, 'B': B})
        print "cost: %d" % k

        #break if desired matrix and factorized matrix are very similar
        if k < 5:
            break

        #b)
        #recalculate
        # Hij = Hij * (W_transposed * A)ij / (W_transposed * W * H)ij

        eins = W.T * A
        print "shape of eins: ", eins.shape

        zwei = W.T * W * H
        print "shape of zwei: ", zwei.shape

        drei = np.array(eins) / np.array(zwei)
        print "shape of drei: ", drei.shape

        H_arr = np.array(H) * drei

        print "HArray:"
        pp.pprint(H_arr)

        H = np.matrix(H_arr)
        print "shape of H: ", H.shape, "H:"
        pp.pprint(H)

        #c)
        #Wij = Wij * (A * H_transposed)ij / (W * H * H_transposed)ij

        nextW = np.array(W) * np.array(A * H.T) / np.array(W * H * H.T)

        W = nextW
        it -= 1
        print "current values: (%d more iterations)\n" % it
        print "W:\n", W, "\nH:\n", H
        print "-"*64

        pass


    print "r: %d, c: %d" % (r, c)
    #return {'H': H, 'W': W}
    return W, H


if __name__ == "__main__":
    #TODO Exercise 2.2.3: check if Matrix contains no row only of zeros
    A = np.matrix([[1, 2, 3], [0, 0, 2], [2, 0, 1], [2, 0, 0]])

    A *= 1.0
    result = nnmf(A, 2, 3)
    W, H = result

    print "W:\n", W
    print "H:\n", H

    #print "k = " + str(cost(A,B))
    """try:
        nnmf(A, 2, 4)
    except Exception, e:
        print "Exception: ", e
        pass

    print "\n", '#' * 80, "\n"

    "" "
    try:
        nnmf(A, 2, 4)
    except Exception, e:
        print "Exception: ", e
        pass
    #print "nnmf result:"
    #pp.pprint(result)
    """

    pass