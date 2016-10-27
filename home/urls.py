from django.conf.urls import url
##from django.contrib import admin
##from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    url(r'^RecipesHome/$', views.IndexView.as_view(), name='index'),

    # /home/DishesByMe
    url(r'^dishesByMe/$', views.TemplateView.as_view(), name='dishesByMe'),

    # /home/Appetizer
    url(r'^Appetizer/$', views.IndexView.as_view(), name='appetizer'),

    #
    ##url(r'^login/$', auth_views.login, name='login'),

    ##url(r'^logout/$', auth_views.logout, name= 'logout'),

    ##url(r'^admin/', admin.site.urls),
    #
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/home/recipeId/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /home/recipe/add/
    url(r'recipe/add/$', views.RecipeCreate.as_view(), name='recipe-add'),

    # /home/recipe/2/
    url(r'recipe/(?P<pk>[0-9]+)/update/$', views.RecipeUpdate.as_view(), name='recipe-update'),

    # /home/recipe/2/
    url(r'recipe/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='recipe-delete'),

]

#def home(request):
#    return render(request,'home/dishesByMeWelcome.html')
