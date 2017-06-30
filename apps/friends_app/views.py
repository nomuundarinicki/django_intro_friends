from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Friend, User
# Create your views here.

def index(request):
    if not checkAuth(request):
        print 'not authorized'
        return redirect('login:index')

    user = User.objects.get(id=request.session['id'])
    friends = Friend.objects.all()
    print friends
    context = {
        'user': user,
        'friends': friends,

    }
    return render(request, 'friends_app/index.html', context)


def addFriend(request):
    if not checkAuth(request):
        print 'not authorized'
        return redirect('login:index')

    if request.POST:
        results = Friend.objects.addFriend(request.POST,request.session.get('id'))
        if results:
            messages.info(request, 'friend Added')
            return redirect('myfriend:index')
        else:
            for error in results:
                messages.error(request, error)
            return redirect('myfriend:addFriend')


    user = User.objects.get(id=request.session.get('id'))
    context = {
        'user': user,
    }
    return render(request, 'friends_app/addFriend.html', context)


def show(request):
    if not checkAuth(request):
        print 'not authorized'
        return redirect('login:index')

    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    if not 'errors' in request.session:
        request.session['errors'] = []
    contents = Content.objects.all().filter(content_id=id)
    context = {
        'content': context,
        'friend': friend,
    }
    return render(request, 'friends_app/show.html', context)

# def joinFriend(request, quote_id, user_id):
#     if not checkAuth(request):
#         print 'not authorized'
#         return redirect('login:index')
#     results = Friend.objects.joinFriend(friend_id, user_id)
#     if not results['status']:
#         for errors in results['errors']:
#             messages.error(request.error)
#             return redirect('myfriend:add')
#     else:
#         messages.success(request, 'Joined Friends!')
#     return redirect('myfriend:index')


def checkAuth(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Please login First')
        return False
    else:
        return True
