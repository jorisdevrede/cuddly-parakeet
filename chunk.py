#!/usr/bin/env python

import cStringIO

class Processor:
    """Basic Processor implementation"""
    
    def do(self, element):
        print element

class Chunk:
    """Cuts XML files into separate chunks"""
    
    processor = None
    
    def __init__(self):
        self.processor = Processor()
    
    def __init__(self, processor):
        self.processor = processor
    
    def cut(self, stream, start, end):
        """Cuts an inputstream into chunks and feeds it to Processor.do()
        
        """
        buffer = None
        intag = False
        
        for line in stream:
            line = line.strip()
            if start in line:
                print 'start', line
                intag = True
                buffer = cStringIO.StringIO()
                buffer.write(line)
            elif end in line:
                print 'end', line
                intag = False
                buffer.write(line)
                chunk = buffer.getvalue()
                buffer.close()
                buffer = None
                
                # do processing                
                self.processor.do(chunk)

            else:
                print 'else', line
                if intag:
                    buffer.write(line)
