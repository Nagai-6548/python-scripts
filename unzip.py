import zipfile
import glob
import re
import os

def unzip_all():
  files = glob.glob("*.zip")
  for filepath in files:
    unzip(filepath)

def unzip(filepath):
  try:
    with zipfile.ZipFile(filepath, 'r') as inputFile:
      # 全て解凍するならextractall
      #inputFile.extractall("/Users/nagai/Downloads")

      # zipファイル内のCSVだけ解凍する
      s = re.compile(".*\.csv")
      fileinfos = inputFile.infolist()
      for fileinfo in fileinfos:
        if s.match(fileinfo.filename):
          # zipファイル内の階層を無視するためにfilenameを書き換え
          fileinfo.filename = os.path.basename(fileinfo.filename)
          inputFile.extract(fileinfo, "name")
    print("success " + filepath)
  except:
    print("failed " + filepath)

if __name__ == "__main__":
  unzip_all()