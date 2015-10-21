import urllib2

def get_page(url):
    #This is a simulated get page procedure so that we can test our code.
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except:
        return ""
    return ""

def get_next_target(page):
    assert isinstance(page, str)
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endPos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endPos:]
        else:
            break
    return links


def union(p, q):
    # To make union of tow lists.
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            #print page
            #tocrawl.extend(get_all_links(get_page(page)))
            content = get_page(page)
            #Add content to index.
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
    return index
 #Function to build an index of urls



#index = []
def add_to_index(index, keyword, url):
    for elem in index:
        if keyword == elem[0]:
            elem[1].append(url)
            return
    index.append([keyword, [url]])
    return


# Function to query the index
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def make_string(list1):
    s = ""
    for e in list1:
        s = s + e
    return s

def make_big_index(size):
    index = []
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index

def time_execution(code):
    import time
    start_time = time.clock()
    result =  eval(code)
    run_time = time.clock() - start_time
    return result, run_time



def test():

   # link = '<span><a href="/"><img src="//imgs.xkcd.com/static/terrible_small_logo.png" alt="xkcd.com logo" height="83" width="185"/></a></span><span id="slogan">A webcomic of romance,<br/> sarcasm, math, and language.</span></div><div id="news" <a href="http://blog.xkcd.com/?p=805"><img border=0 src="//imgs.xkcd.com/store/te-news.png"></a><br />      <script>'
    
    #link = get_page('https://www.udacity.com/cs101x/index.html')
    #print get_all_links(link)
   # print crawl_web("http://xkcd.com/353")
    #print crawl_web('https://www.udacity.com/cs101x/index.html')
    index = []
    add_page_to_index(index, 'fake.test', "This is a test")
    add_page_to_index(index, 'not.test', "This is not a test")
    print index

index = make_big_index(10)

#test()
def test2():
    #print index
    print time_execution('lookup(index, "udacity")')

test2()
