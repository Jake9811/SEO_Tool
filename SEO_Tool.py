#Search Engine Optmization Tool

#libraries
import tkinter as tk
from bs4 import BeautifulSoup as bs4
import requests
import re
import matplotlib.pyplot as plt

def Search():
    global soup
    url = urlText.get()
    source = requests.get(url)
    soup = bs4( source.text, 'html5lib' )
    titleDisplay()

def titleDisplay():
    displayTitle.set(soup.title.text)
    displayLabel.pack( side=tk.LEFT )

def rawData():
    raw = tk.Tk()
    raw.title('RAW Data')
    rawText = tk.Text(raw)
    rawText.insert(tk.INSERT , soup.prettify())
    rawText.pack( side = tk.TOP , fill="both" , expand=True)
    rawText['state'] = 'disabled'
    raw.mainloop()

def textOnly():
    text = tk.Tk()
    text.title('TEXT Only')
    textOnly = tk.Text(text)
    textOnly.insert(tk.INSERT , soup.body.text )
    textOnly.pack( side = tk.TOP , fill="both" , expand=True )
    textOnly['state'] = 'disabled'
    text.mainloop()

def desc():
    desc = tk.Tk()
    desc.title('Description')
    descText = tk.Text(desc)
    content = soup.find( 'meta' , attrs={"name": "description"} )
    descText.insert(tk.INSERT , content['content'] )
    descText.pack( side = tk.TOP , fill="both" , expand=True )
    descText['state'] = 'disabled'
    desc.mainloop()

def meta():
    meta = tk.Tk()
    meta.title('META Tags')
    metaText = tk.Text(meta)
    metaText.insert( tk.INSERT , soup.find_all('meta') )
    metaText.pack( side = tk.TOP , fill="both" , expand=True )
    metaText['state'] = 'disabled'
    meta.mainloop()

def keyword():
    
    def find():
        global keywordList
        global countList
        keyButton['state'] = 'disabled'
        keyword = keyText.get()
        keywordList = keyword.split()
        sequence = soup.text
        countList = list(range(len(keywordList)))
        keyDisplay = tk.Text( resultFrame , font=("Arial",15) )
        keyDisplay.insert( tk.INSERT , "Count :")
        keyDisplay.pack( side=tk.LEFT , fill="both" , expand=True)

        for x in range(len(keywordList)):
            keyList = re.findall( keywordList[x] , sequence )
            countList[x] = len(keyList)
            exec('keyDisplay.insert( tk.INSERT , " %s = %d ")' % ( keywordList[x] , countList[x] ) )
        
        keyDisplay.pack( side = tk.LEFT )
        keyDisplay['state'] = 'disabled'
        
    def displayGraph():
        plt.bar( keywordList , countList )
        plt.title('Keyword Density')
        plt.xlabel('Keywords')
        plt.ylabel('Numbers')
        plt.show()
        
        
    key = tk.Tk()
    key.title('Keyword Tool')
    keyFrame = tk.Frame( key , pady=10 , cursor="circle" )
    keyFrame.pack( side=tk.TOP )
    keylabel = tk.Label( keyFrame , text="Enter the keywords : ", font=("Impact",20))
    keylabel.pack( side=tk.LEFT)
    keyText = tk.Entry( keyFrame , width=70 )
    keyText.pack( side=tk.LEFT , expand=True, fill="x")

    keyButton = tk.Button(keyFrame, text="Search", bd=5, padx=20, cursor="plus", bg="blue", font=("Arial",15), fg="white", command=find )
    keyButton.pack( side=tk.LEFT )

    resultFrame = tk.Frame( key , pady=10 , cursor="circle" )
    resultFrame.pack( side=tk.TOP , fill="x" )
    keydesclabel = tk.Label( resultFrame , text="Enter the keywords separated by a blank space" , font=("Arial",15) )
    keydesclabel.pack( side=tk.TOP , fill="x" , expand=True)
    barFrame = tk.Frame( resultFrame , bg="grey", height=10 )
    barFrame.pack( side=tk.TOP , fill="x" )
    graphButton = tk.Button( resultFrame , text="Generate Graph", bd=5, padx=20, cursor="plus", font=("Arial",15), command=displayGraph )
    graphButton.pack( side=tk.BOTTOM )
    key.mainloop()

#Main Window
top = tk.Tk()
top.title('Search Engine')

frameTop = tk.Frame(top, bg="grey", bd="10", cursor="circle")
frameTop.pack(fill="x")

#Title
labelHead = tk.Label(frameTop, text="Search Engine", anchor="center", bg="grey", font=("Arial", 40), fg="white")
labelHead.pack()

frameMain = tk.Frame(top, cursor="circle")

#LeftBar
frameL = tk.Frame(frameMain, bg="cyan", width=100, cursor="circle")
frameL.pack( side=tk.LEFT, expand=True, fill="y" )

frameR = tk.Frame(frameMain, bg="orange", width=100, cursor="circle")
frameR.pack( side=tk.RIGHT, expand="true", fill="y" )

#URL_Bar
urlFrame = tk.Frame(frameMain, cursor="circle", pady=10)
urlFrame.pack( side=tk.TOP )

urlLabel = tk.Label(urlFrame, text="URL : ", font=("Impact",20))
urlLabel.pack( side=tk.LEFT )

urlText = tk.Entry(urlFrame, width=100)
urlText.pack( side=tk.LEFT , expand=True, fill="x")

urlButton = tk.Button(urlFrame, text="Analyze", bd=5, padx=20, cursor="plus", bg="blue", font=("Arial",15), fg="white", command=Search)
urlButton.pack( side=tk.RIGHT )

#Options
optFrame = tk.Frame(frameMain, cursor="circle", pady=10)
optFrame.pack( side=tk.TOP , fill="x" )

barFrame = tk.Frame(optFrame, bg="grey", height=10)
barFrame.pack( side=tk.TOP , fill="x" )

titleFrame = tk.Frame(optFrame , cursor="circle", pady=10)
titleFrame.pack( side=tk.TOP , fill="x" )

titleLabel = tk.Label(titleFrame, text="Title : ", font=("Impact",20))
titleLabel.pack( side=tk.LEFT )

displayTitle = tk.StringVar()
displayLabel = tk.Label(titleFrame, textvariable=displayTitle , font=("Arial",15))

rawButton = tk.Button(optFrame, text="RAW Data", bd=5, padx=20, cursor="plus", font=("Arial",15), command=rawData)
rawButton.pack( side=tk.LEFT )

textButton = tk.Button(optFrame, text="TEXT Only", bd=5, padx=20, cursor="plus", font=("Arial",15), command=textOnly)
textButton.pack( side=tk.LEFT )

descButton = tk.Button(optFrame, text="Description", bd=5, padx=20, cursor="plus", font=("Arial",15), command=desc)
descButton.pack( side=tk.LEFT )

metaButton = tk.Button(optFrame, text="META Tags", bd=5, padx=20, cursor="plus", font=("Arial",15), command=meta)
metaButton.pack( side=tk.LEFT )

keyButton = tk.Button(optFrame, text="Keyword Tool", bd=5, padx=20, cursor="plus", font=("Arial",15), command=keyword)
keyButton.pack( side=tk.LEFT )

frameMain.pack( fill="both" , expand=True)
top.mainloop()