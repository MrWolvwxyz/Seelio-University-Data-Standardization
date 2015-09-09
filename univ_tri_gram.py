from glob import glob

univ_dirty_names = []
univ_dirty_counts = []

with open( 'univ_names.txt', 'r' ) as f:
    for line in f:
        print( line.split() )
        univ_dirty_names.append( line.split() [ 0 ] )
        univ_dirty_counts.append( line.split() [ 1 ] )

print( univ_dirty_names )
print( univ_dirty_counts )

