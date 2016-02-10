
import sys
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

def printConfidencesFor( test_set, transactions, support, stream_out ):
	for elem in test_set:
		new_set = test_set - set(elem)
		confidence = transactionsWith( test_set, transactions ) / transactionsWith( new_set, transactions )
		if confidence < min_conf:
			continue
		res = ""
		for item in new_set:
			if res is not "":
				res += " ^ "
			res += "buys(X,{})".format( item )
		res += " => buys(X,{})[{}%, {}%]\n".format( elem, int( support * 100 ), int( confidence * 100 ) )
		stream_out.write( res )

def subsetsOfLength( length ):
	possible = set( list( 'ABCDEFHSTOUFWDOAECFGX' ) )
	return set( itertools.combinations( possible, length ) )


def main( argv ):
	print( transactions )
	with open( argv[0], 'w+' ) as stream_out:
		for length in range( 2, 5 ):
			stream_out.write( "\n--- Associations of length {} ---\n".format( length ) )
			for s in subsetsOfLength( length ):
				sup = supportFor( set(s), transactions )
				if sup >= min_sup:
					#print( set(s), ":", sup )
					printConfidencesFor( set(s), transactions, sup, stream_out )


if __name__=='__main__':
	main(sys.argv[1:])
