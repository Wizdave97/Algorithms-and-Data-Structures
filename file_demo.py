lines=[]
with open('file_demo.txt','r') as f:
    for newline in f:
        lines.append(newline.strip())


def create_cast_list(filename):
    cast_list=[]
    try:
        with open('{}.txt'.format(filename)) as f:
            for line in f:
                line=line.split(',')
                cast_list.append(line[0])
        return cast_list
    except Exception as e:
        print('\n {} :please check your input string'.format(e))
print(create_cast_list('flying_circus_cast'))
