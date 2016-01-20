import sys

def readStringCSV( filename ):
    data = open( filename, 'r' ).read().split()
    attributes = data[0].split(',')
    relations = [ line.split(',') for line in data[1:] ]
    return ( attributes, relations )

def readBooleanCSV( filename ):
    data = open( filename, 'r' ).read().split()
    attributes = data[0].split(',')
    relations = [ [ True if elem is '1' else False for elem in line.split(',') ] for line in data[1:] ]
    return ( attributes, relations )

if __name__=='__main__':
    main( sys.argv[1:] )
