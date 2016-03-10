''' Work of Cameron Palk '''

import sys


def splitSamples( samples, split_count ):
	
	test_ratio = 1.0 / float( split_count )
	rows_count = len( samples )

	splits = [ ] # A list of tuples of sample 2D arrays

	test_size = int( rows_count * test_ratio )

	for split_idx in range( split_count ):
	
		next_idx = split_idx + 1

		start_idx = split_idx * test_size
		stop_idx  = next_idx  * test_size

		test_samples = []
		train_samples = []

		if split_idx == 0:
			test_samples  = samples[ : stop_idx ]
			train_samples = samples[ stop_idx : ]

		elif split_idx < next_idx:
			test_samples  = samples[ start_idx : stop_idx ]
			train_samples = samples[ : start_idx ] + samples[ stop_idx : ]

		else:
			test_samples  = samples[ start_idx : ]
			train_samples = samples[ : start_idx ]

		print( len( test_samples ) )
		print( len( train_samples ) )

		splits.append( ( train_samples, test_samples ) )

	return splits



def processSplit( headers, samples, splits_count ):

	splits = splitSamples( samples, splits_count )

	test_filename_template  = "test_split_{idx}.csv"
	train_filename_template = "train_split_{idx}.csv"

	filenames = []
	for idx, split in enumerate( splits ):
		test_filename  = test_filename_template.format ( idx = idx )
		train_filename = train_filename_template.format( idx = idx )

		filenames.append( ( test_filename, train_filename ) )

		test_matrix  = [ headers ] + split[ 0 ]
		train_matrix = [ headers ] + split[ 1 ]

		with open( test_filename, 'w+' ) as test_stream:
			test_stream.write( '\n'.join( test_matrix ) )

		with open( train_filename, 'w+' ) as train_stream:
			train_stream.write( '\n'.join( train_matrix ) )

		print( "{} has been written with line count: {}".format( test_filename,  repr( len( test_matrix  ) ) ) )
		print( "{} has been written with line count: {}".format( train_filename, repr( len( train_matrix ) ) ) )

	print( "All files complete. Files:\n"  )
	print( *filenames, sep='\n' )
	print()




def main( argv ):
	try:

		splits_count = int ( argv[ 1 ] )
		csv_stream   = open( argv[ 2 ], 'r' )
		
		data_matrix = csv_stream.read().split( '\n' )

		headers = data_matrix[ 0  ]
		samples = data_matrix[ 1: ]
		
		processSplit( headers, samples, splits_count )

	except IndexError:
		print( "Error, usage: \"python3 {} <splits> <CSV>\"".format( argv[ 0 ] ) ) 
	except ValueError:
		print( "Error, need an integer value for split count" )
#


if __name__=='__main__':
	main( sys.argv )
#


