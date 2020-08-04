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

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-'*10 + ' ') * len(headers))
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')
    def row(self,rowdata):
        print('<tr>', end = '')
        for d in rowdata:
            print(f'<td>{d}</td>', end = '')  
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(format):
    if format == 'txt':
        return TextTableFormatter()
    elif format == 'csv':
        return CSVTableFormatter()
    elif format == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'unknown table format {format}')

def print_table(portfolio, select, formatter):
    formatter.headings(select)
    for p in portfolio:
        rows = [ str(getattr(p, s, None)) for s in select ]
        formatter.row(rows)       