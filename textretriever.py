import requests
import bs4
import random
import webbrowser

#get a 50 word text string from a random book on project gutenberg. if that doesn't work, use a default string
num = random.randint(1, 1500)
url = f'https://www.gutenberg.org/files/{num}/{num}-h/{num}-h.htm'

def find_sample():
	try:
		
		book = requests.get(url)
		soup = bs4.BeautifulSoup(book.text, 'html.parser').find_all('p')

		#iterates over <p> tags, starting at the 30th to avoid undesirable strings i.e. table of contents,
		#until it finds the text block of >= 50 words. Stores that block in a variable.
		end = len(soup)
		text_blocks = iter(soup[30:end])
		for p in text_blocks:
			block = p.get_text().split()
			if len(block) >= 50:
				sample = block[0:50]
				break
		sample = " ".join(sample)

		return sample

	except:
		sample = "To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly,"
		sample = sample.split()
		sample = sample[0:50]
		sample = " ".join(sample)
		check = True
		return sample


	
















