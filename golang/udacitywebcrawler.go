package main

import (
	"fmt"
	"github.com/tarun2502/mygolibrary/stringutil"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

func getPage(url string) string {
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	//fmt.Printf("%s", body)
	return string(body)
}

func getNextTarget(page string) (url string, endQuote int) {
	startLink := strings.Index(page, "<a href=")
	//fmt.Printf("startLink:%d\n", startLink)
	if startLink == -1 {
		return
	}
	startQuote := stringutil.IndexAfterPos(page, `"`, startLink)
	//fmt.Printf("startQuote:%d\n", startQuote)
	if startQuote == -1 {
		return
	}
	endQuote = stringutil.IndexAfterPos(page, `"`, startQuote+1)
	if endQuote == -1 {
		return
	}
	url = page[startQuote+1 : endQuote]
	return
}

func getAllLinks(page string) []string {
	links := []string{}
	for {
		url, endQuote := getNextTarget(page)
		if url != "" {
			//fmt.Printf("Url:%s\n", url)
			links = append(links, url)
			page = page[endQuote:]
		} else {
			break
		}
	}
	return links
}

//To append list2 into list1
func union(list1 []string, list2 string) []string {
	for _, value := range list2 {
		for i := 0; i < len(list1); i++ {
			if list1[i] == value {
				break
			}
		}
		append(list1, value)
	}
}

func main() {
	link := `<span><a href="/"><img src="//imgs.xkcd.com/static/terrible_small_logo.png" alt="xkcd.com logo" height="83" width="185"/></a></span><span id="slogan">A webcomic of romance,<br/> sarcasm, math, and language.</span></div><div id="news>
		<a href="http://blog.xkcd.com/?p=805"><img border=0 src="//imgs.xkcd.com/store/te-news.png"></a><br />      <script>
		`
	link = "https://www.udacity.com/cs101x/index.html"
	fmt.Print(getAllLinks(getPage(link)))
}
