import urllib.request

def main(url):

  try:
    code = urllib.request.urlopen(url).getcode()
  except:
    code = 404
  #print(code)
    
  if code == 200:
    print("url available")
  else:
    print("url not available")

def reformulr(url):
  
  if url.find("http") != -1:
    return url
  else:
    return "http://" + url


def main_easy(url): 
    try:
      print(urllib.request.urlopen(url).getcode());
    except: 
      print("URL not found. 404")

url = input("Enter url: ")
main(reformulr(url))
