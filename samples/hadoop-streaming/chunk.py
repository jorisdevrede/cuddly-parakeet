#!/usr/bin/env python

import cStringIO


class Processor:
    """Basic Processor implementation"""

    def __init__(self):
        pass

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
        :param stream standard inputstream:
        :param start index within the inputstream to start processing:
        :param end index within the input stream to end end processing:

        """
        cbuffer = None
        intag = False

        for line in stream:
            line = line.strip()
            if start in line:
                print 'start', line
                intag = True
                cbuffer = cStringIO.StringIO()
                cbuffer.write(line)
            elif end in line:
                print 'end', line
                intag = False
                cbuffer.write(line)
                chunk = cbuffer.getvalue()
                cbuffer.close()
                cbuffer = None

                # do processing                
                self.processor.do(chunk)

            else:
                print 'else', line
                if intag:
                    cbuffer.write(line)
