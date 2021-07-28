# mproject (English)

## Table of Contents
  * [Presentation](#chapter-1-en)
  * [Installation](#chapter-2-en)
  * [Create a project](#chapter-3-en)
  * [Project structure](#chapter-4-en)
  * [Create a new application](#chapter-5-en)
  * [Site routes](#chapter-6-en)

## Presentation <a name="chapter-1-en"></a>

### Project description
mproject is a website I created as part of a university course to learn how the Django framework works.

### License
The Django framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Installation <a name="chapter-2-en"></a>

### Step 1 : Installing python 3.8 (or higher) :
Django is a framework that uses the python language, so it will be necessary to have a recent version of python to make it work.
<a href="https://www.python.org/downloads/">[Download Python]</a>

Warning in order to be able to use python commands more easily from the windows terminal it is useful to add python to the path.
<a href="https://datatofish.com/add-python-to-windows-path/">[How to add python to path ?]</a>

### Step 2 : Installing pip (latest version) :
Pip is the official package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.
<a href="https://pypi.org/project/pip/">[Download pip]</a>

### Step 3 : Installing django (with python from pip index):
Open the windows terminal and enter the following command :
```bash
python -m pip install Django 
```

## Create a project <a name="chapter-3-en"></a>
To create a django project you have to use the following command in the windows terminal :
```bash
python -m django startproject mproject
```
_Warning: the directory in which you are when executing this command will host the project, you can of course move it later._

## Project structure <a name="chapter-4-en"></a>
When a project is created the following tree is added to the current directory :
```bash
mproject/
    manage.py
    mproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
* **mproject/** : This directory is a container for your project. His name does not have not important to Django. You can rename it as you want.
  * **manage.py** : This file is a kind of command line executable that allows you to interact with this project Django in different ways.
  * **mproject/** : Matches the actual Python package in your project. This is the name of the Python package that you should use to import its contents (e.g : mproject.urls).
    * **__ init __.py** : An empty file that tells Python that this directory should be considered as a package.
    * **settings.py** : Settings and configuration of this Django project.
    * **urls.py** : The declarations of the URLs of this Django project, a sort of "table of content" from your Django site.
    * **asgi.py** : An entry point for aSGI compatible web servers to deploy your project.
    * **wsgi.py** : An entry point for WSGI compatible web servers to deploy your project.

## Create a new application <a name="chapter-5-en"></a>
To create your application, make sure you are in the same directory as manage.py and enter the command :
```bash
python manage.py startapp developer
```
_What is the difference between a project and an application? An application is a
web application that does something - for example a blog system, a database
public data or a small survey app. A project is a set of
settings and applications for a particular website. A project can contain several
applications. An application can appear in several projects._

## Site routes <a name="chapter-6-en"></a>
The site's routes are managed by the urls.py file. There is one for the project and one for each application you create. This urls.py file contains a list "urlpaterns" which contains all the routes for the project or application to which it belongs. 

Within this list each url is called by a "path ()" function which will contain several arguments :
```python
path('', views.index, name='index')
```
* **First arg : route (required)** : This is a string containing a url pattern.
* **Second arg : view (required)** : Will link the triggering of a function in the view.py file to the call of this url. 
* **Third arg : kwargs (optional)** : Will allow you to specify one or more arguments for the targeted function.
* **Fourth arg : kname (optional)** : Will add a name to the url.

# mproject (Français)

## Table des Matières
  * [Présentation](#chapter-1-fr)
  * [Installation](#chapter-2-fr)
  * [Créer un projet](#chapter-3-fr)
  * [Structure d'un projet](#chapter-4-fr)
  * [Créer une nouvelle application](#chapter-5-fr)
  * [Les routes du site](#chapter-6-fr)

## Présentation <a name="chapter-1-fr"></a>

### Description du projet
mproject est un site web crée dans le cadre d'un cours de haute école ayant pour but d'apprendre les bases du framework Django.

### License
Le framework Django est un logiciel open source sous [licence MIT](https://opensource.org/licenses/MIT).

## Installation <a name="chapter-2-fr"></a>

### Étape 1 : Installer python 3.8 (ou plus récent) :
Django est un framework qui utilise le langage python, il faudra donc avoir une version récente de python pour le faire fonctionner.
<a href="https://www.python.org/downloads/">[Télécharger Python]</a>

Attention afin de pouvoir utiliser plus facilement les commandes python depuis le terminal windows il est utile d'ajouter python au PATH.
<a href="https://datatofish.com/add-python-to-windows-path/">[Comment ajouter python au PATH ?]</a>

### Étape 2 : Installer pip (dernière version) :
Pip est l'installateur de package officiel pour Python. Vous pouvez utiliser pip pour installer des packages à partir de l'index de packages Python et d'autres index.
<a href="https://pypi.org/project/pip/">[Télécharger pip]</a>

### Étape 3 : Installer django (avec python via les index pip):
Ouvrez le terminal windows et tapez la commande suivante :
```bash
python -m pip install Django 
```
## Créer un projet <a name="chapter-3-fr"></a>
Pour créer un projet django il faut utiliser la commande suivante dans le terminal windows :
```bash
python -m django startproject mproject
```
_Attention : le repertoire dans lequel vous vous trouvez au moment d'executer cette commande acceuillera le projet, vous pouvez bien-entendu le deplacer par la suite._

## Structure d'un projet <a name="chapter-4-fr"></a>
Lorsqu'un projet est créer l'arborescence suivante est ajouter au repertoire courant :
```bash
mproject/
    manage.py
    mproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
* **mproject/** : Ce répertoire est un contenant pour votre projet. Son nom n’a pas d’importance pour Django, vous pouvez le renommer comme vous voulez.
  * **manage.py** : Ce fichier est une sorte d'executable en ligne de commande qui vous permet d’interagir avec ce projet Django de différentes façons.
  * **mproject/** : Correspond au paquet Python effectif de votre projet. C’est le nom du paquet Python que vous devrez utiliser pour importer ce qu’il contient (par ex. : mproject.urls ).
    * **__ init __.py** : Un fichier vide qui indique à Python que ce répertoire doit être considéré comme un paquet.
    * **settings.py** : Réglages et configuration de ce projet Django.
    * **urls.py** : Les déclarations des URL de ce projet Django, une sorte de « table des matières » de votre site Django. 
    * **asgi.py** : Un point d’entrée pour les serveurs Web compatibles aSGI pour déployer votre projet.
    * **wsgi.py** : Un point d’entrée pour les serveurs Web compatibles WSGI pour déployer votre projet. 

## Créer une nouvelle application <a name="chapter-5-fr"></a>
Pour créer votre application, assurez-vous d'être dans le même répertoire que manage.py et saisissez la commande :
```bash
python manage.py startapp developer
```
_Quelle est la différence entre un projet et une application ? Une application est une
application Web qui fait quelque chose – par exemple un système de blog, une base de
données publique ou une petite application de sondage. Un projet est un ensemble de
réglages et d’applications pour un site Web particulier. Un projet peut contenir plusieurs
applications. Une application peut apparaître dans plusieurs projets._

## Les routes du site <a name="chapter-6-en"></a>
Les routes du site sont géré par le fichier urls.py. Il en existe un pour le projet et un pour chaques application que vous créerez. Le fichier urls.py contient une liste "urlpaterns" qui contient toutes les routes pour le projet ou l'application auquel il appartient. 

Au sein de de cette liste chaques url est appellé par une fonction "path()" qui va contenir plusieur arguments :
```python
path('', views.index, name='index')
```
* **Premier argument : route (requis)** : Il s'agit d'une chaîne contenant un modèle d'URL.
* **Second argument : view (requis)** : Va lier le declanchement d'une fonction du fichier view.py a l'appel de cet url.
* **Troisième argument : kwargs (optionnel)** : Va permettre de spécifier un ou plusieurs argument pour la fonction ciblée.
* **Quatrième argument : kname (optionnel)** : Permet de nommer l'url.


<p align="center">Copyright © 2021 InteralexDev | all rights reserved</p>