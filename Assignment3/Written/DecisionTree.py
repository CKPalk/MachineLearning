
import sys
from math import log
from itertools import combinations



def prob( S, Ci_set ):
	#print( ( len( [ s for s in S if s[ -1 ] in Ci_set ] ) / len( S ) ) )
	return ( len( [ s for s in S if s[ -1 ] in Ci_set ] ) / len( S ) )
#

def Entropy( S, C1_set, C2_set ):
	if len( C1_set ) == 0 or len( C2_set ) == 0: return 0
	return ( -1 * ( prob( S, C1_set ) * log( prob( S, C1_set ), 2 ) ) 
			    - ( prob( S, C2_set ) * log( prob( S, C2_set ), 2 ) ) )
#

def subsetOfS( S, A_idx, Ci_set ):
	return [ s for s in S if s[ A_idx ] in Ci_set ]
#

def valuesOfAttribute( S, A_idx ):
	return list( set( [ s[A_idx] for s in S ] ) )

def Gain( S, A_idx, C1_set, C2_set ):
	vals = valuesOfAttribute( S, A_idx )
	subsets = [ subsetOfS( S, A_idx, { val } ) for val in vals ]
	print( subsets )
	return ( 
		Entropy( S, C1_set, C2_set ) - 
		sum( [ ( len(s) / len(S) ) * Entropy( s, C1_set, C2_set ) for s in subsets ] ) 
	)
#

def main( argv ):
	# COUNT:			# of rows for each
	# AGE:				> 60 = 3 | 30 - 60 = 2 | < 30 = 1
	# GENDER:			Male = 1 | Female = 0
	# YEAR_INCOME:		> 100k = 3 | 60k - 100k = 2 | < 60k = 1
	# CREDIT_RANKING: 	Excellent = 3 | Good = 2 | Fair = 1
	S = [ 	[ 16, 1, 1, 2, 3 ],
			[  4, 1, 0, 1, 3 ],
			[ 16, 3, 1, 1, 3 ],
			[  4, 3, 0, 2, 3 ],
			[ 15, 2, 1, 1, 2 ],
			[  5, 2, 0, 2, 2 ],
			[ 15, 1, 1, 1, 2 ],
			[  5, 1, 0, 2, 2 ],
			[ 18, 3, 1, 1, 1 ],
			[ 18, 2, 0, 2, 1 ],
			[  2, 1, 1, 2, 1 ],
			[  2, 1, 1, 1, 1 ]	]

	S2 = [ 	[ 2, 2, 1, 0, 0 ],
			[ 2, 2, 1, 1, 0 ],
			[ 1, 2, 1, 0, 1 ],
			[ 0, 1, 1, 0, 1 ],
			[ 0, 0, 0, 0, 1 ],
			[ 0, 0, 0, 1, 0 ],
			[ 1, 0, 0, 1, 1 ],
			[ 2, 1, 1, 0, 0 ],
			[ 2, 0, 0, 0, 1 ],
			[ 0, 1, 0, 0, 1 ],
			[ 2, 1, 0, 0, 1 ],
			[ 1, 1, 1, 1, 1 ],
			[ 1, 2, 0, 0, 1 ],
			[ 0, 1, 1, 1, 0 ] 	]

	#S = S2
	all_classes = set( [ s[-1] for s in S ] )
	
	possible_class_groups = [ ( set( c ), all_classes - set( c ) ) for c in combinations( all_classes, 2 ) ]
	#possible_class_groups = [ ( {0},{1} ) ]

	print( possible_class_groups )

	print( '\n', S, '\n' )

	for class_group in possible_class_groups:
		print( "Trying", class_group[0], "vs.", class_group[1] )
		for i in range( 1, 4 ):
			print( "Index", i, "Gain:", Gain( S, i, class_group[0], class_group[1] ) )
#

if __name__=='__main__':
	main( sys.argv[ 1: ] )
#
