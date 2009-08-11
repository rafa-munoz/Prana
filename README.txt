=========
  Prana
=========

Prana is a simple word/meaning anotation application that allows you to store
words and their meaning so that you can list all of them or just displaying a
random word/meaning anywhere you like.

With this app you can easily memorize words in other languages by the old
method of repetition, but instead of using a fridge or your bedroom's wall
you use your computer :)
You can embed this application to any webpage you own, desktop widget or
even Gmail.

There is support as well for verbs, so you are not limited to a single word
anotation.

It was developed on Debian 5.0 Lenny and Django 1.0.2.

Please send comments/suggestions to http://github.com/Menda/Prana/issues
Prana code page: http://github.com/Menda/Prana

Hope you like it,
Rafa Muñoz Cárdenas


Prerequisites
-------------

    1. You first need to install Markdown.

    - Debian, Ubuntu or derived distributions:
      $ sudo apt-get install python-markdown

    - Fedora or Red Hat:
      # yum install python-markdown

    - OpenSuse or Suse:
      XXXXXXXXXXXXXXXXXXXXXXXXXXX

    - Arch Linux:
      XXXXXXXXXXXXXXXXXXXXXX

    - Gentoo:
      XXXXXXXXXXXXXXXXXX

    - Windows:
      XXXXXXXXXXXXXXXXXXXXXXXXXX

    - Mac OS:
      XXXXXXXXXXXXXXXXXXXXXXXXXX

    2. django.contrib.auth and django.contrib.admin have to be in your
    INSTALLED_APPS in settings.py

    3. Add django.core.context_processors.request to
    TEMPLATE_CONTEXT_PROCESSORS in settings.py


Instalation
-----------

    1. Clone the code via Git into any existing project or anywhere in your
       python path:
       git clone XXXXXXXXXXXXXXXXXXXXXXX

    2. Now you have 2 options:

       - Cut the prana template dir and paste into your templates dir.

       OR:

       - Add into TEMPLATE_DIRS in settings.py the following:
       '/home/youruser/yourproject/prana/templates',

       The advantages for the second approach is that you are able to git clone
       whenever you want to get the latest version for the project and you
       don't have to do anything else.

    3. Activate internationalization in settings.py:
       USE_I18N = True

    4. Add 'prana', to your INSTALLED_APPS in settings.py

    5. Run:
       $ python manage.py syncdb

    6. Update your project urls.py:
       (r'^prana/', include('prana.urls')),

    7. That's all amigo!


Start using it
--------------

It's very easy to start using it.
Go to the admin page and add some words or verbs to the program. After that
browse the main page http://yoursite.com/prana/

If you want to embed it somewhere you can play with the url to make everything
bigger or smaller.

Use GET arguments "font" and "width" for this.

    - font: default is 100 (as in 100%). If you want it smaller, set a value
      less than 100, for example 70. More than 100 is for bigger fonts.

    - width: you can set in pixels the width of the webpage. It's really useful
      if you want to use it in small widgets or small devices. The default
      value is your current screen resolution.

    Examples:
    http://yoursite.com/prana/?font=70 - Font 70% (smaller)
    http://yoursite.com/prana/?font=70&width=300 - Font 70%, 300 pixels width
    http://yoursite.com/prana/?width=150 - 150 pixels width

    Note that you have to use (&) to separate every GET argument from the other
    and put a (?) after the last slash.

Get involved
------------

Help is always good, so if you want to make your contribution you can:

    - Send your feedback.
    - Find new features/ideas and implement them (if you can).
    - Submit patches.
    - Perform Prana localization for your language (explained next).


How to localize for your language
---------------------------------

    1. Move to prana dir in your shell.

    2. Run (replace es_ES to your language and country):
       django-admin makemessages -l es_ES

    3. Go to prana/locale/your_language and edit with your translations the
       django.po file.

    4. django-admin compilemessages
       
    5. Restart your server to see Prana in your language.

    6. Check the results and if everything it's OK send us your translations!


What the heck is "Prana"?
-------------------------

Prana is the 11th song of Trentemøller's album "The Last Resort".
This album is one of the best electronic works made ever, and I like it so much
that I decided to take the name of one of it's songs.

