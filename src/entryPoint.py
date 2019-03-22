'''
Created on Mar 21, 2019

@author: maddo
'''

import mechanize


def main():
	url = "https://www.animecharactersdatabase.com/"
	user_agent = [('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')]
	
	#Create browser object
	br=mechanize.Browser()
	br.set_handle_robots(False)
	#add user agent
	br.addheaders=user_agent
	
	#open web url
	page=br.open(url)
	
	#read page source code
	source_code = page.read()

	#print source code
	print(source_code)

main()