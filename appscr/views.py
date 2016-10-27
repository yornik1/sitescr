from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from .forms import InstaName, RemoveInstaName
from .models import Profile, Photo
from .top import top_media
import os



def index(request):
    form_data = request.POST if request.POST else None
    #if form_data:  # debug info
        #print(form_data)  # POST data (for debug)

    form_add = InstaName(form_data)
    if form_add.is_valid():
        profile = Profile(
                        name=form_data.get('name'),
                        top_count=form_data.get('top_count') if form_data.get('top_count') else 10,
                        videos=form_data.get('videos')
                     )
        profile.save()  # write new row to DB
        os.system('scrapy runspider appscr/instagram_spider.py -a account=%s -a videos=%s' %
                  (profile.name, 'y' if profile.videos else 'n')
                  )
        '''
        r = runspider.Command()
        r.run(args=['instascr/instagram_spider.py'],
              opts=['-a account='+aeprofile.name,
                    '-a videos='+'y' if profile.videos else 'n'
                    ]
              )
        '''

        return redirect('/top/%s' % profile.name)

    form_rem = RemoveInstaName(form_data)
    if form_rem.is_valid():
        prof = Profile.objects.filter(
            name__icontains=form_data.get('name_del'))
        prof.delete()  # delete row from DB
        Photo.objects.all().delete()
        return redirect('/')
    t = loader.get_template('index.html')
    return HttpResponse(t.render({'form_add': form_add,
                                  'form_rem': form_rem}),)


def top(request, name):
    profile = Profile.objects.get(name=name)
    top_media(name, number=profile.top_count)
    photos = Photo.objects.all()
    dict = {}
    dict['photos'] = photos
    dict['photos_count'] = len(photos)
    t = loader.get_template('top.html')
    return HttpResponse(t.render(RequestContext(request, dict)))
