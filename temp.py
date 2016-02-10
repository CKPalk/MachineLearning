
import itertools


min_sup  = 0.60
min_conf = 0.75


transactions = [ 
    set( list( 'ABCDEF' ) ),
    set( list( 'BHSCFT' ) ),
    set( list( 'AUOFWD' ) ),
    set( list( 'OAECFG' ) ),
    set( list( 'XACDEF' ) )
]


def transactionsWith( test_set, transactions ):
    return len( list( filter( lambda x: x >= test_set, transactions ) ) )

def supportFor( test_set, transactions ):
    return transactionsWith( test_set, transactions ) / len( transactions )

def printConfidencesFor( test_set, transactions ):
    for elem in test_set:
        new_set = test_set - set(elem)
        confidence = transactionsWith( test_set, transactions ) / transactionsWith( new_set, transactions )
        print( "\t", new_set, " + ", elem, ":", confidence )

def subsetsOfLength( length ):
    possible = set( list( 'ABCDEFHSTOUFWDOAECFGX' ) )
    return set( itertools.combinations( possible, length ) )


def main():
    print( transactions )
    for length in range( 1, 5 ):
        print( "\n--- LENGTH", length, "---\n" )
        for s in subsetsOfLength( length ):
            sup = supportFor( set(s), transactions )
            if sup >= min_sup:
                print( set(s), ":", sup )
                printConfidencesFor( set(s), transactions )


if __name__=='__main__':
	main()
