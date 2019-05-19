import os


TOP = []


def safe_make_folder(i):
    '''Makes a folder if not present'''
    try:
        os.mkdir(i)
    except:
        pass

def make_top_level(top):

    for i in range(len(top)):
        safe_make_folder(top[i])



def main():
    link_file = open('LINKS.txt', 'r')

    list1 = []
    i = 1

    for line in link_file:
        new_list = line.strip('\r\n')
        list1.append(str(i) + '. ' + new_list)
        i = i + 1

    make_top_level(list1)


if __name__ == "__main__":
    main()
