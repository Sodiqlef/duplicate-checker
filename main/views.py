from django.shortcuts import render, redirect
from .models import Duplicates
from .forms import DuplicateForm
from .duplicate import alldup

# Create your views here.


def home(request):
    # Tweet links should be pasted here

    if request.method == 'POST':
        form = DuplicateForm(request.POST)
        if form.is_valid():
            duplicate_form = form.save(commit=False)
            duplicate_form.save()
            return redirect('home')
        else:
            pass
    else:
        form = DuplicateForm()
    obj = Duplicates.objects.last()
    shills = f'''
{obj.duplicate}
'''

    # this turns the string to list
    split = list(shills.split('\n'))
    arr1 = [i for i in split if i != '']
    arr = [i for i in arr1 if i != '\r']

    total = len(arr)

    # these lines removes all numbering less than or equal to 9999
    new = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for each in range(len(arr)):
        if arr[each][0] in num and arr[each][1] not in num:
            new += [','.join(arr[each][1:].split('\n'))]
        if arr[each][1] in num and arr[each][2] not in num:
            new += [','.join(arr[each][2:].split('\n'))]
        if arr[each][2] in num and arr[each][3] not in num:
            new += [','.join(arr[each][3:].split('\n'))]
        if arr[each][3] in num and arr[each][4] not in num:
            new += [','.join(arr[each][4:].split('\n'))]

    # this line prints out amount of valid tweets
    valid = len(set(new))

    # these lines print out duplicated tweets and amount of duplicated tweets
    duplicates = {each2 for each2 in new if new.count(each2) > 1}
    duplicates_length = len(duplicates)

    repeated = total-valid-duplicates_length

    return render(request, 'home.html', {'duplicates': duplicates, 'duplicates_length': duplicates_length,
                                        'shills': shills, 'valid': valid, 'form': form,
                                         'total': total, 'repeated': repeated})


def form_field(request):
    if request.method == 'POST':
        form = DuplicateForm(request.POST)
        if form.is_valid():
            duplicate_form = form.save(commit=False)
            duplicate_form.save()
            return redirect('home')
        else:
            pass
    else:
        form = DuplicateForm()


    return render(request, 'home.html', {'form': form})