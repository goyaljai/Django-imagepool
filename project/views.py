from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import View
from project.forms import LoginForm
from django.contrib.auth import authenticate
from django.views import generic
from project.models import *
from django.contrib.auth import login
from django.shortcuts import render
from project.forms import UserForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import re
import operator
from django.db.models import Q
# from django.contrib.auth.mixins import LoginRequiredMixin
# this is used when we want to use login_required for views
from project.mixins import LoginRequiredMixin,LogoutRequiredMixin
from django.contrib.auth.models import Group


def index(request):
    # values = request.META.items()
    # values = sorted(values)
    # html = []
    # for k, v in values:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))

    if request.user.id is None:
        return redirect('login_user')
    else:
       # return redirect('detail', pk=request.user.id)
        return HttpResponseRedirect(reverse('detail', args=(request.user.id,)))


class DetailView(generic.DetailView):
    model = SiteUser
    template_name = 'project/detail.html'


class UserListView(generic.ListView):

    template_name = 'project/search.html'
    context_object_name = 'result'

    def get_queryset(self):
        return SiteUser.objects.all()


class LoginFormView(View):



    form_class = LoginForm
    template_name = 'project/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('detail', pk=user.id)

        return render(request, self.template_name, {'form': form})

# only we can see this if and only if user is logged out because if he is loged in then there is no point using the register
class RegisterView(LogoutRequiredMixin,View):

    form_class = UserForm
    template_name = 'project/register.html'

    # post method means they are sumbmitting the form
    # get method means they only want the form to fill

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST , request.FILES)

        if form.is_valid():

            user = form.save(commit=False)
            # cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            # g = Group.objects.get(name='Male')
            # if user.gender == 'M':
                # user.groups.add(g)

            user.save()

            # returns users objects if credentials are correct



            user = authenticate(username=username,password=password)



        if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('detail', pk=user.id)

        return render(request, self.template_name, {'form': form})


def like_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    cnt = image.like_count + 1
    like = Liker()
    f = 0
    image_list = Liker.objects.filter(image=image)

    for item in image_list:
        if item.user == request.user:
            f = 1
            break

    if f == 0:
        Image.objects.filter(pk=image_id).update(like_count=cnt)
        like.image = image
        like.user = request.user
        like.save()

    return redirect('detail', pk=request.user.id)


class ImageCreate(CreateView):
    model = Image
    fields = ['image','caption','access_users']

    def form_valid(self, form):
        image = form.save(commit=False)
        image.user = self.request.user
        # article.save()  # This is redundant, see comments.
        return super(ImageCreate, self).form_valid(form)



def search(request):
    result = SiteUser.objects.all()
    query = request.GET.get("q")

    if query:
        result = result.filter(Q(username__icontains=query)).distinct()
        return render(request, 'project/search.html', {
                'result': result,
            })
    else:
        return redirect('all-users')


def logout_user(request):
    logout(request)
    return redirect('register')


def follow_user(request, user_id):
    theuser = SiteUser.objects.get(pk=user_id)
    follower = Follow()
    follower.user = request.user
    follower.follower = theuser
    # logged in person request.user ne follow pe click kia
    follower.save()

    return redirect('detail', pk=user_id)


def unfollow(request):
    pass
