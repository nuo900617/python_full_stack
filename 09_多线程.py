import time
from concurrent.futures import ThreadPoolExecutor


def task(url):
    print('开始了')
    time.sleep(3)
    return 111

def outer(file_name):
    def done(response):
        print('完成了: ', response.result(), file_name)
    return done

pool = ThreadPoolExecutor(5)

img_list = [
    {'name': '1.jpg', 'url': 'xxxx'},
    {'name': '2.jpg', 'url': 'xxxx'},
    {'name': '3.jpg', 'url': 'xxxx'},
    {'name': '4.jpg', 'url': 'xxxx'},
    {'name': '5.jpg', 'url': 'xxxx'},
    {'name': '6.jpg', 'url': 'xxxx'},
    {'name': '7.jpg', 'url': 'xxxx'},
    {'name': '8.jpg', 'url': 'xxxx'},
    {'name': '9.jpg', 'url': 'xxxx'},
    {'name': '10.jpg', 'url': 'xxxx'},
]

for item in img_list:
    fur = pool.submit(task, item['url'])
    fur.add_done_callback(outer(item['name']))