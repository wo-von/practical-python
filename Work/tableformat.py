#!/usr/bin/python3

#--
# Ex4.5
#--

class TableFormatter(object):
    '''
    Abstract base class, does nothing
    Design specification for additional classes
    '''
    def headings(self, headers):
        '''
        Emit table headings
        '''
    raise NotImplementedError()
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
    raise NotImplementedError()

