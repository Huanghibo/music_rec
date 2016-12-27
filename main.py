import acoustid
print "Enter the file name with the path : "
path=raw_input()

#match function takes two inputs : first one is the API key provided by AcoustID after registering one's application. Second one is the file
#Behind the hood : match function first creates a fingerprint of the song and then matches it to the AcoustID database 
#match function returns ALL entries that were found to match the fingerprint. So more than one entries may be returned
#each entry consists of 4 variables : score, fingerprint_id, title, artist

for score,song_id,title,artist in acoustid.match('vfmtz8hHRi',path):
	print artist+" - "+title
