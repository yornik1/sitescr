# -*- coding: utf-8 -*-
import json
from .models import Photo

KEYS_LIST = ['ip', 'domain', 'datetime', 'url', 'status', 'size', 'user']

def top_media(name, number):
    json_list = []

    with open('%s.json' % name, "r") as json_file:
        json_list += json.loads(json_file.read())
    l = []
    #print(json_list)
    for i in range(number):
        l.append(max(json_list, key=lambda k: k['likes']))
        json_list.remove(l[i])
    print(l)
    json_list = []  # clearing memory
    #json_list = json_list[]
    for dict in l:
        photo = Photo(url=dict.get('url'), likes=dict.get('likes'), comments=dict.get('comments'))
        photo.save()
    #Photo.objects.order_by('likes')
    return None
