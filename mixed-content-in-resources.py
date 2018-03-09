import sys
import re
import urllib.request

exp_comments = '/\*(.|\n)*?\*/';
exp = 'http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
counter = 1

if len(sys.argv) < 2: 
  print("Please pass a .txt file, containing URL's (1 per line) as the first argument")
  quit()
else:
  input_file = sys.argv[1]
  print('\n'*3)
  print('*'*72 + "\n\nStart crawling URL's in " + input_file + '\n\n' + '*'*72 + '\n')
with open('output_'+input_file, 'w') as output_file:
  with open(input_file) as f:
    for line in f:
      line = line.strip()
      print('\n'+line)
      print('-'*72)
      try:
        content = urllib.request.urlopen(line).read().decode('utf-8')
        #strip out the comments
        content = re.sub(exp_comments,'',content)
        urls = re.findall(exp,content)
        if urls:        
          output_file.write(str(counter) + '.' +line+'\n' + '-'*72+'\n')
          for pos,url in enumerate(urls):
            print(url)
            output_file.write(url+'\n')
            if pos == len(urls) -1:
              output_file.write('\n'*2)
          counter +=1
        else:
          print ('This file is clean')
      except urllib.error.URLError as e:
        print(e.reason)
        output_file.write(line +'\n' + '-'*72+'\n' + e.reason + '\n')

