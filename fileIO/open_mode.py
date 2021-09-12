# mode = 'a' (append): ファイルの最後尾に内容を追加
with open('writing_file.txt', mode='a') as f:
    f.write('mode=a appends text')

# mode = 'r+': 読み書きどちらも可能
# ポインタが一番最初にいる
with open('writing_file.txt', mode='r+') as f:
    f.write('You can write and read with r+ mode!!')
    print(f.read())
    f.write('This should be the last sentence.')
    print(f.read())

# mode = 'w+': 読み書きどちらも可能 Truncateされることに注意
# 最初に全て消える
with open('writing_file.txt', mode='w+') as f:
    print(f.read())
    f.write('You can write and read with w+ mode!!')
    f.seek(0) # positionを先頭に持ってくる
    print(f.read())

# mode = 'a+': 読み書きどちらも可能で、positionが最後尾から始まる
with open('writing_file.txt', mode='a+') as f:
    print(f.read())
    f.write('\n You add sentence to the last of the file content a+ mode')
    print(f.read())