
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


def python_cours_details(request, course_id):
    try:
        course = PythonCourse.objects.get(pk=course_id)
    except:
        return redirect('python_intro')
       

    else:
        # if course.DoesNotExist:
        #     return redirect('python_intro')

            
        if course.id == 1:
            context = {'course':course}
            return render(request, 'tutorial/variable_and_datatype.html', context)
        elif course_id == 2:
            context = {'course':course}
            return render(request, 'tutorial/operators_and_input.html', context)
        elif course_id == 3:
            context = {'course':course}
            return render(request, 'tutorial/conditions.html', context)
        elif course_id == 4:
            context = {'course':course}
            return render(request, 'tutorial/if_else.html', context)
        elif course_id == 5:
            context = {'course':course}
            return render(request, 'tutorial/nested_statements.html', context)
        elif course_id == 6:
            context = {'course':course}
            return render(request, 'tutorial/forloops.html', context)
        elif course_id == 7:
            context = {'course':course}
            return render(request, 'tutorial/whileloops.html', context)
        elif course_id == 8:
            context = {'course':course}
            return render(request, 'tutorial/listandtuple.html', context)
        elif course_id == 9:
            context = {'course':course}
            return render(request, 'tutorial/string_method.html', context)
    

        elif course_id == 10:
            context = {'course':course}
            return render(request, 'tutorial/slice_operator.html', context)
        elif course_id == 11:
            context = {'course':course}
            return render(request, 'tutorial/functions.html', context)
        elif course_id == 12:
            context = {'course':course}
            return render(request, 'tutorial/reading_files.html', context)
        elif course_id == 13:
            context = {'course':course}
            return render(request, 'tutorial/writing_files.html', context)
        elif course_id == 14:
            context = {'course':course}
            return render(request, 'tutorial/listmethod.html', context)
        elif course_id == 15:
            context = {'course':course}
            return render(request, 'tutorial/modular_programing.html', context)
        elif course_id == 16:
            context = {'course':course}
            return render(request, 'tutorial/error_handling.html', context)
        elif course_id == 17:
            context = {'course':course}
            return render(request, 'tutorial/global_vs_local.html', context)
        elif course_id == 18:
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