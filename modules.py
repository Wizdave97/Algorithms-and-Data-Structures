import math
import random
import scripting.py

def main():
    print(math.pow(2,3))
    def generate_password():
        try:
            word_list=[]
            with open('words_list.txt','r') as f:
                for line in f:
                    word_list.append(line.strip('\n'))
            password_list=random.sample(word_list,3)
            password=''.join(password_list)
            return password
        except Exception as e:
            print('\n{}: check if file exists '.format(e))
    print(generate_password())
if __name__=='__main__':
    main()
