import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://google.comr',timeout=20)
        return True
    except urllib2.URLError as err: pass
    return False

def main():
	if internet_on() == True:
		print ("yes")
	else:
		print ("no")
main()
