with open('writing_file.txt', mode='w') as f:
    # truncatedされる:byte=0に切り詰める
    f.write('You can write contents here\n')
    f.write('new write() doesn`t break no')

    print('You can add a new row using "file" parameter', file=f)
    print('new print() method breaks the row for you!!', file=f)