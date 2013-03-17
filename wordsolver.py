#wordsolver
import collections

class freqword( object ):
    def __init__( self, word, freq ):
        self.word = word
        self.freq = int( freq )
    def __cmp__( self, other ):
        if type( other ) == type( self ):
            return cmp( self.freq, other.freq )
        if type ( other  == str ):
            return cmp( self.word, other )
    #def __repr__( self ):
    #    return self.word
    def __str__( self ):
        return self.word

def load_freq():
    freqlist = []
    #Note: This list was obtained from http://invokeit.wordpress.com/frequency-word-lists/
    #Please support the original word list author.
    with open('en_50k.txt', 'r') as fin:
        for lines in fin:
            sline = lines.split()
            freqlist.append( (freqword( sline[0].strip(), sline[1].strip() ) ) )
    return freqlist

def load_dict():
    wordlist = []
    with open('/usr/share/dict/words', 'r' ) as fin:
        for lines in fin:
            wordlist.append( lines.strip().lower() )
    return wordlist

def main():
    print "Loading Dictionary..."
    worddict = load_dict()
    freqlist = load_freq()
    while( True ):
        sortable_matches = []
        unsortable_matches = []

        letters, length = raw_input( "Letters to decode:\n>" ).split( ' ' )
        for word in worddict:
            if( is_match( word, letters, length ) ):
                if word in freqlist:
                    sortable_matches.append( freqlist[freqlist.index(word)] )
                else:
                    unsortable_matches.append( word )

        #print the uglies, followed by the not uglies
        for i in unsortable_matches:
            print i
        print "----------"

        #most frequent items will be printed last.
        for i in sorted( sortable_matches ):
            print i


def is_match( word, letters, length ):
    if len( word ) == int(length):
        #print word
        if all( letter in letters for letter in word ):
            w_counter = collections.Counter( word )
            #print w_counter
            l_counter = collections.Counter( letters )
            #print l_counter
            if all( l_counter[ i ] >= w_counter[ i ] for i in word ):
                return True
            return False
    return False


if __name__ == '__main__':
    main()