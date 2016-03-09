class rarFormat
   'class to test if a file is a single or multi rar archive filenames'
   
   def isFileSingleArchive(self, fileName):
     if($fileName =~ /\.rar$/ and $fileName !~ /\.part\d+\.rar$/):
        return True		
     else:
        return False

   def isFileMultiArchive(self, fileName):
     if($fileName=~ /\.part[0]*1.rar$/):
        return True
     else:
        return False
