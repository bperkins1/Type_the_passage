def missed_words(sample, paragraph):
	sample_check = sample.split()
	paragraph_words = iter(paragraph.split())

	for word in paragraph_words:
		if word in sample_check:
			sample_check.remove(word)

	return sample_check

def calculate_wpm(paragraph, time):
	all_words = paragraph.split()
	total_words = len([word for word in all_words if len(word) >= 2])
	time = round(time) / 60
	try:
		wpm = round(total_words/time)
	except ZeroDivisionError:
		wpm = 0
	return wpm

def accuracy(sample, paragraph):
	missed = len(missed_words(sample,paragraph))
	totalwords = len(sample.split())
	accuracy = 100 - (missed/totalwords * 100) 
	return round(accuracy)

#missed_words doc:
	#take both paragraphs
	#put each word in a list as separated by spaces
	#check each word in typed paragraph to see if it is in the sample
	#if paragraph word in sample,  remove first instance of the word from sample.
	#length of sample at the end of loop is the number of missed words

#calculate_wpm:
	#count the amount of words greater than 1 letter
	#divide words by given time(which will be the difference between when submit and begin
	#were hit in UNIX era time)

#accuracy:
	#expresses correct words as a percentage of words in the test