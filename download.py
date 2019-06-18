import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

# まとめてダウンロードしたいURLを指定
url = "{}"

# URLの可変部分のリストを指定
codes = []

def download_all():
  for code in codes:
    download(code)

def download(code):
  try:
    urllib.request.urlretrieve(url.format(code), "{0}.zip".format(code))
    print("success " + code)
  except:
    print("failed " + code)

if __name__ == "__main__":
  download_all()