# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        self.headings = []
        self.headings.append(headers)
        
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        self.row = []
        self.row.append(rowdata)
        
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format.
    '''
    def headings(self, headers):
        # your code here
        self.headers =[]
        self.headers.append(headers)
        return self.headers
    def row(self, rowdata):
        # your code here
        self.row = []
        self.row.append(rowdata)
        return self.row


class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
       # your code here 
        self.headers =[]
        self.headers.append(headers)
        return self.headers
    def row(self, rowdata):
       # your code here
        self.row = []
        self.row.append(rowdata)
        return self.row

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
       # your code here
        self.headers =[]
        self.headers.append(headers)
        return self.headers

    def row(self, rowdata):
       # your code here
        self.row = []
        self.row.append(rowdata)
        return self.row

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)

