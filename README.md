# my_blog_Django

Projet faire un blog pour apprendre les bases de Django

I: base configuration Django

  creation d'un dossier puis dans le dossier

   1: Creation environment virtual
   $ python -m venv env
   prendre note que cette environnement virtual n'est pas dans
   le depot git il faudra la creer lors d'un nouveau clone.

   2: activer environment virtuel sous windows: source env/Scripts/activate (Pour mac et linux  source env/bin/activate)
      pour le desactiver on fait deactivate

   3: faire update de pip : pip install --upgrade pip

   4: install django : pip install django==version_souhaite  dans ce projet j'utilise la version 3.1.6
       verifie l'installation c'est bien passe pip -m django --version

   5 : requirement.txt : geler l'environnement virtuel dans ce fichier.il regroupe toutes les bibliotheques installees
       en faisant : pip freeze > requirements.txt et cat requirements.txt pour voir afficher contenu
       pour le tester: desinstaller pip uninstall django  et faire pip install -r requirements.txt pour reinstaller tout les bibliotheques

II : Creer un projet django 
    
   1: pour le projet : django-admin startproject nom_projet 
    Dans ce projet je vais faire django-admin startproject MyBlog

   2: Lancer le server local: python manage.py runserver 
    Il faut avant faire un python manage.py migrate pour la bd
    Il faut naviguer dans le dossier src afin de le lancer
    il faudrait configurer l'interpreter :
         -> Settings -> nom du projet -> Python interpreter
   