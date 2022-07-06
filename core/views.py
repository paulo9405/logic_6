from django.shortcuts import render, redirect
from .models import Double
from .forms import DoubleForm


def double_list(request):
    doubles = Double.objects.all()
    return render(request, 'double_list.html', {'doubles': doubles})


def double_create(request):
    form = DoubleForm(request.POST or None)
    name_user_form = form.data.get('name')
    val_user = request.POST.get('value')
    value_user_form = int(val_user or 0)
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


    data_obj = None
    obj = Double.objects.filter(name=name_user_form, value = value_user_form)
    if obj.count() > 0:
        data_obj = obj[0]

    if data_obj is not None:
        return render(request, 'obj_exist.html', {'name_obj': data_obj.name,
                                                  'value_obj': data_obj.value,
                                                  'double_obj': data_obj.double_value,
                                                  'date_obj': data_obj.date,
                                                  })

    elif value_user_form > 1000 or value_user_form < -1000:
        erro_value = 'Plaese maximum 1000 and minum -1000'
        return render(request, 'double_create.html', {'form': form, 'erro_value': erro_value})


    elif name_user_form is not None:
        for letter in name_user_form:
            if letter not in valid_characters:
                erro_char = 'Plaese dont use special character'
                return render(request, 'double_create.html', {'form': form, 'erro_char': erro_char})
            else:
                if form.is_valid():
                    form.save()
        return redirect('double_list')
    return render(request, 'double_create.html', {'form': form})


