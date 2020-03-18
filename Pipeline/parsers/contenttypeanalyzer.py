import re

class ContentTypeAnalyzer:

    @classmethod
    def IsImageByContentType(cls, ContentType):
        regex = re.compile(r'^image\/',re.I)
        return regex.match(ContentType)
    
    @classmethod
    def IsPdfByContentType(cls, ContentType): 
        return True if ContentType == 'application/pdf' else False

    @classmethod
    def IsTextByContentType(cls, ContentType):
        regex = re.compile(r'^text\/',re.I)
        return regex.match(ContentType)

    @classmethod
    def IsAudioByContentType(cls, ContentType):
        regex = re.compile(r'^audio\/',re.I)
        return regex.match(ContentType)

    @classmethod
    def IsVideoByContentType(cls, ContentType):
        regex = re.compile(r'^video\/',re.I)
        return regex.match(ContentType)

    # @classmethod
    # def IsArchive(cls, FileName):      
    #     regex = re.compile('(\\.zip$)', re.I)  
    #     return True if regex.search(FileName) else False
    @classmethod
    def IsArchive(cls, FileName):
        ext_type = ['(\\.zip$)', '(\\.gz)', '(\\.tar$)', '(\\.rar$)', '(\\.arc$)', '(\\.7z$)', '(\\.jar$)', '(\\.bz2?$)']
        pattern = '(?:% s)' % '|'.join(ext_type)
        return True if re.search(pattern, FileName) else False

    @classmethod
    def IsPst(cls, FileName):      
        regex = re.compile('(\\.pst$)', re.I)  
        return True if regex.search(FileName) else False

    @classmethod
    def IsPdf(cls, FileName): 
        regex = re.compile('(\\.pdf$)', re.I)  
        return True if regex.search(FileName) else False