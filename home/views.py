from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Recipe
from .forms import UserForm

#def home(request):
#    return render(request,'home/dishesByMeWelcome.html')


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_recipes'

    def get_queryset(self):
        return Recipe.objects.all()

class TemplateView(generic.TemplateView):
    template_name = 'home/dishesByMeWelcome.html'
#class DetailView(generic.ListView):
#    template_name = 'home/dishesByMeWelcome.html'
#    context_object_name = 'all_recipes'

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'home/detail.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipeTitle', 'recipeImage', 'courseType', 'mealType', 'ingredients', 'directions']

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipeTitle', 'recipeImage', 'courseType', 'mealType', 'ingredients', 'directions']

  #####  model = Recipe
  #####  template_name = "recipe_form.html"

  #####  def get_form_class(self):
  #####      return Custom

# /home/recipe/2/  this is where you can choose where you are redirected after Deletion
class RecipeDelete(DeleteView):
    model = Recipe
    success_url= reverse_lazy('home:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #register and add user to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #check info for validity
            #creates object from form..w/o saving to db
            user = form.save(commit=False)

            #normalized/formatted data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #saves to db
            user.save()

            #returns User obj if credentials are valid
            user = authenticate(username=username, password=password)

            if user is not None:

                #you have ability to ban or disable user
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        return render(request, self.template_name, {'form': form})

