import xml.sax 

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attribute):
        print(name)
        # self.current = name
        # self. 
        
handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')