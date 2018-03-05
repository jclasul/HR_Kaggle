# TO:DO : Make Importable module
# Store in GitHub/HR/IDnumbers
#

class IDnumbers(object):
    def GetFile(self, Mode, WriteString = None, FileName = 'IDnumbers'):
        '''
        self: IDnumbers
        Mode: (a) for writing; (r) for reading
        WriteString: !!! IN STRING FORMAT !!! otherwise TypeError exception gets executed;
                     not required for reading
                           
        FileName: default = IDnumbers; change to create new file
        '''
        try:
            with open(FileName, mode=Mode) as f:
                if Mode == 'a':
                    f.write(str(WriteString) + "\n")
                else:
                    self.IDnumbers_read = f.read()
                    return self.IDnumbers_read.split()
            f.closed       
        except FileNotFoundError:
            print('NOT FOUND -- wrote to disk: ', FileName)
            open(FileName, mode = 'w')
            self.GetFile(Mode='a', FileName=FileName, WriteString = WriteString)
        except TypeError:
            print('ERROR \n')
            print('Please provide input value to write')
    def EraseFile(self, FileName = 'IDnumbers'):
        '''
        Erase content from FILE; change FileName if needed
        '''
        open(FileName, mode='w').close()