import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
for k in range(729,6927,1):
    print "Opening webpage: " + "https://wallpaperscraft.com/all/page"+str(k)
    web_req = urllib2.Request("https://wallpaperscraft.com/all/page"+str(k),headers={"User-Agent":"Magic Browser"})
    web_con = urllib2.urlopen(web_req)
    try: 
        web_read = web_con.read()
    except:
        print "\n"
        print "*********************************"
        print "ERROR OCCURED... Trying again...."
        print "*********************************"
        print "\n"
        continue 
    print "HTML STRING RECIVED"
    print "Souping the HTML"
    web_soup = BeautifulSoup(web_read)
    web_img_prev = web_soup.findAll("img")
    print "Seaching images"
    web_img_src = []
    for i in web_img_prev:
        web_img_src.append(i["src"][2:])
    for i in range(len(web_img_src)):
        web_img_src[i] = web_img_src[i].replace("300x188","1024x768")
    for i in range(len(web_img_src)):
        web_img_src[i]=web_img_src[i].encode("utf-8")
    for i in range(len(web_img_src)):
        print "Download: " + web_img_src[i]
        r = urllib2.Request("https://"+web_img_src[i],headers={"User-Agent":"Magic Browser"})
        try:
            u = urllib2.urlopen(r).read()
        except:
            print "\n"
            print "*********************************"
            print "ERROR OCCURED... Trying again...."
            print "*********************************"
            print "\n"
            continue
        print len(u)
        print "Data of:" + web_img_src[i] + ": Retrived"
        print "Creating pic#"+str(i+1)
        f = open("wallpapers/pic"+str(k-1)+"_"+str(i+1)+".jpg","wb")
        f.write(u)
        f.close()
        print "pic"+str(i+1)+" created."
        print "-----------------------------------------------------------------------"
    print "\n"
print '\n \n'
print "All images completed"
