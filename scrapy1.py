import string, urllib2

def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		sName = string.zfill(i,5)+'.html' #fill as a 5 char filename
		print 'Downloading '+str(i)+' page and saved it as '+sName+'....'
		f = open(sName,'w+')
		m = urllib2.urlopen(url+str(i)+'.html').read()
		f.write(m)
		f.close()



bdurl = "http://www.1point3acres.com/bbs/forum-28-"
begin_page = 1
end_page = 2

baidu_tieba(bdurl,begin_page,end_page)
