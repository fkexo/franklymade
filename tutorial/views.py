
from django.shortcuts import render, redirect
from .models import PythonCourse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostCourseForm

# for the franklymade homepage
def franklymade_home(request):
    context = {}
    return render(request, 'tutorial/tutorial_home.html', context)

# for the search bar
# i still need to work on this function for it to be able to find the required keyword
def searchBar(request):
    keyword_list = ['python', 'django', 'javascript'] 
    if keyword_list.Find['python']:

        return render(request, 'tutorial/python_intro.html', context)
    elif keyword_list.Find['django']:
        return render(request, 'franklymade/djangobase.html', context)
    else:
        return render(request, 'franklymade/base.html', context)


            





# ******************************************
# for the python tutorials
def python_intro(request):   
    context = {}
    return render(request, 'tutorial/python_intro.html', context)


def python_cours_details(request, slug):
    try:
        course = PythonCourse.objects.get(slug=slug)
    except:
        return redirect('python_intro')
       

    else:
        # if course.DoesNotExist:
        #     return redirect('python_intro')

            
        if slug == 'Variables-And-Data-Types':
            context = {'course':course}
            return render(request, 'tutorial/variable_and_datatype.html', context)
        elif slug == 'Operators-and-Input':
            context = {'course':course}
            return render(request, 'tutorial/operators_and_input.html', context)
        elif slug == 'Conditions':
            context = {'course':course}
            return render(request, 'tutorial/conditions.html', context)
        elif slug == 'If-Elif-Else-statements':
            context = {'course':course}
            return render(request, 'tutorial/if_else.html', context)
        elif slug == 'Chained-Conditionals-And-Nested-Statement':
            context = {'course':course}
            return render(request, 'tutorial/nested_statements.html', context)
        elif slug == 'For-Loop':
            context = {'course':course}
            return render(request, 'tutorial/forloops.html', context)
        elif slug == 'While-Loops':
            context = {'course':course}
            return render(request, 'tutorial/whileloops.html', context)
        elif slug == 'List-and-Tuples':
            context = {'course':course}
            return render(request, 'tutorial/listandtuple.html', context)
        elif slug == 'String-methods':
            context = {'course':course}
            return render(request, 'tutorial/string_method.html', context)
    

        elif slug == 'Slice-operator':
            context = {'course':course}
            return render(request, 'tutorial/slice_operator.html', context)
        elif slug == 'Functions':
            context = {'course':course}
            return render(request, 'tutorial/functions.html', context)
        elif slug == 'Read-Files':
            context = {'course':course}
            return render(request, 'tutorial/reading_files.html', context)
        elif slug == 'Write-Files':
            context = {'course':course}
            return render(request, 'tutorial/writing_files.html', context)
        elif slug == 'List-Method':
            context = {'course':course}
            return render(request, 'tutorial/listmethod.html', context)
        elif slug == 'Modular-Programming':
            context = {'course':course}
            return render(request, 'tutorial/modular_programing.html', context)
        elif slug == 'Error-Handling':
            context = {'course':course}
            return render(request, 'tutorial/error_handling.html', context)
        # elif slug == 21:
        #     context = {'course':course}
        #     return render(request, 'tutorial/global_vs_local.html', context)
        elif slug == 'Classes-and-objects':
            context = {'course':course}
            return render(request, 'tutorial/classes_and_objects.html', context)
  
        # else:
            # return HttpResponseRedirect(reverse('python_intro', args=(course.id,)))

    return redirect('python_intro')


    

def create_course(request):
    title = 'Create blog post'
    err_msg = ''
    message = ""
    
    if request.user.is_authenticated:
        # try:
        form = PostCourseForm(request.POST or None, request.FILES or None)
        
        
        if request.method == "POST":
            if form.is_valid():
                
                form.save()

                return redirect(reverse("courses", kwargs={
                    'id':form.instance.id
                }))
        # except IntegrityError as e :
        #     e = "please contact admin  to gain access to post your blog"
        #     err_msg = e
        #     print(err_msg)
        #     pass
    
    message = err_msg
    
    context = {
        # 'title':title,
        
        'message':message,
        'form':form,
        }

    return render(request, 'tutorial/create_course.html', context)
    

# search function
# def searchCourse(request):





    

# def viewtutorial(request):
    
#     context = {'projects':projects}
#     return render(request, 'tutorial/listandtuple.html', context)


# for django tutorial
def django_intro(request):
    context = {}
    return render(request, 'franklymade/djangobase.html', context)