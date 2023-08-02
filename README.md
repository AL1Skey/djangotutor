# Django Cheat Sheet

### Requirement
- virtualenv for django
- django on virtualenv

### Installing package
```
    pip install <package-name>
```

### Creating Virtual Environment
```
    makevirtualenv <name-of-virtual-environment>
```

### Log in to created Virtual Environment
```
    workon <name-of-virtual-environment>
```

### Creating django project
```
    django-admin startproject <project-name>
```

### Creating app/middleware/api
```
    python manage.py startapp <name-of-app/middleware/api>
```

### Run django project
```
    python manage.py runserver
```

### Insert urls from API to main project
mainProject/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('<name-of-api>'))
]
```

### Using Templates
mainProject/settings.py
```py
......
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, '<name-of-templates-foder>'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
......
```

name-of-API/urls.py
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.<method-you-have>, name='<method-you-have>'),
]    
```

name-of-API/views.py
```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def <method-you-have>(request):
    name='this is optional'
    return render(request,'<name-of-templates>.html',{'name':name})
```

name-of-templates-foder/name-of-templates.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Something {{name}}</h1>

    <form action="counter" method="post">
        <!-- insert csrf token for bypass post request -->
        {{% csrf_token %}}

        <textarea name="words" placeholder="WErite Here" id="" cols="30" rows="10"></textarea>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

output
```
    Something This is Optional

    >textarea



    >/textarea

    >/button:submit
```


### 