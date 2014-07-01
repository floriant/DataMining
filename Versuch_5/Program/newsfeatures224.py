# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np
import math


#A and B are of type numpy.matrix
#returns the summed euclidean distance of the passed matrices
def cost(A, B):
    #TODO test if the matrices are of same shape
    k = 0
    print "Matrix A:"
    pp.pprint(A)
    print '-'*64, "\nMatrix B:"
    pp.pprint(B)

    print '-'*64, "\n", '-'*64

    #create iterators
    iteratorA = A.flat
    iteratorB = B.flat

    try:
        while True:
            #iterate over all elements in both matrices
            Aij = iteratorA.next()
            Bij = iteratorB.next()
            k += math.pow(Aij-Bij, 2)
            #print "Aij=%d | Bij=%d" % (Aij, Bij)

    except StopIteration:
        pass #needed because the iterator does not know if there are more elements coming

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

    #pp.pprint({'H': H, 'W': W})

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

        H_t = H.transpose()
        W_t = W.transpose()

        eins = np.array(W_t)*np.array(A)
        print "shape of eins: ", eins.shape

        zwei = np.array(W_t)*np.array(B)
        print "shape of zwei: ", zwei.shape
        drei = ( eins )/(zwei)
        print "shape of drei: ", drei.shape
        HArray = np.array(H) * drei

        print "HArray:"
        pp.pprint(HArray)


        #c)


        it-=1

        break


print "r: %d, c: %d" % (r, c)
return {'H': H, 'W': W}

if __name__ == "__main__":
    #TODO Exercise 2.2.3: check if Matrix contains no row only of zeros
    A = np.matrix([[1, 2, 3], [0, 0, 2], [7, 0, 1], [2, 0, 0]])
    B = np.matrix([[0, 1, 2], [2, 0, 0], [1, 0, 2]])

    #print "k = " + str(cost(A,B))
    try:
        nnmf2(A, 2, 4)
    except Exception, e:
        print "Exception: ", e
        pass

    print "\n", '#'*80, "\n"

    try:
        nnmf2(A, 2, 4)
    except Exception, e:
        print "Exception: ", e
        pass
    #print "nnmf result:"
    #pp.pprint(result)


    pass