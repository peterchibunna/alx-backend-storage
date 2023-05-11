import time

get_page = __import__('web').get_page

if __name__ == '__main__':
    now = time.time()
    print(get_page('http://google.com'))
    print("{} seconds taken".format(time.time() - now))
