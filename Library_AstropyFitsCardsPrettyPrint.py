

"""
DESCRIPTION:
    Takes astropy cards and pretty prints them


ARGS:
    CardList
        astropy hdulist[k].header.cards
        type: http://docs.astropy.org/en/v0.2.1/io/fits/api/cards.html
    
    Names
        If supplied limits printing to the subset of the cards which have .keyword in `Names`
        type: python list

RETURNS

"""
import astropy
import astropy.io.fits
#------------------------------------------------------------------------------




def Main(\
    CardList = None, \
    Names = None,\
    ):
    cardnumber = 0
    for card in CardList:
        if ((Names == None) or (card.rawvalue in Names) ):
            print ''
            print 'card.rawvalue', card.rawvalue

            print 'card.keyword' , card.keyword
            print 'card.comment' , card.comment
            #print 'card.unit', card.unit
            print 'cardnumber'   , cardnumber
        cardnumber += 1

