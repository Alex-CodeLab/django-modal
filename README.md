# django-modal
modal windows for django/bootstrap3



Requires jQuery and Bootstrap 3 on client side. Depends on django-crispy-forms on server side.
This app allows to make responsive AJAX modal forms for creating, editing, deleting objects in Django.

This is a more generic approach to adding modal windows, based on https://github.com/FZambia/django-fm


###Install.###

Add the files to your app folder.
install crispy_forms.

Add crispy_forms and modal to INSTALLED_APPS:
```
INSTALLED_APPS = (
    ...
    'crispy_forms',
    'modal',
)
```
Also in settings.py set crispy template pack to bootstrap3:

CRISPY_TEMPLATE_PACK = 'bootstrap3'

Include modal template into your project template and initialize jQuery plugin:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script type="text/javascript" src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    </head>
    <body>
        {% block content %}{% endblock %}
        {% include "modal/modal.html" %}
        <script type="text/javascript">
            $(function() {
                $.fm({debug: true});
            });
        </script>
    </body>
</html>
```

There are 3 class-based views in django-modal to inherit from when you want AJAX forms:

-    AjaxCreateView
-    AjaxUpdateView
-    AjaxDeleteView

You create urls for them as usual, in templates you just create links to create, update, delete resources with special class (fm-create, fm-update, fm-delete).