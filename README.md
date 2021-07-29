# mproject (English)

## Table of Contents
  * [Presentation](#chapter-1-en)
  * [Installation](#chapter-2-en)
  * [Create a project](#chapter-3-en)
  * [Project structure](#chapter-4-en)
  * [Create a new application](#chapter-5-en)
  * [Site routes](#chapter-6-en)
  * [Models (database)](#chapter-7-en)
  * [Django Shell (database)](#chapter-8-en)

## Presentation <a name="chapter-1-en"></a>

### Project description
mproject is a website I created as part of a university course to learn how the Django framework works.

### License
The Django framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Installation <a name="chapter-2-en"></a>

### Step 1 : Installing python 3.8 (or higher) :
Django is a framework that uses the python language, so it will be necessary to have a recent version of python to make it work.
<a href="https://www.python.org/downloads/">[Download Python]</a>

_Warning in order to be able to use python commands more easily from the windows terminal it is useful to add python to the path._
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

#### Launch the server
```bash
python manage.py runserver
```

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

#### add 'INSTALLED_APPS' in settings.py
```python
'grades.apps.GradesConfig',
```

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

## models (database) <a name="chapter-7-en"></a>
Unlike other frameworks django has its own database system. These databases are managed by models and the user can interact with them directly through the command prompt. By default the databases are in sqlite3.

### The models.py file
It contains classes which correspond to tables in the database and which contain each column as an argument.
```python
class Teacher(models.Model):
    trigram = models.CharField("Trigramme", max_length=3, unique=True, primary_key=True)
    first_name = models.CharField("Prénom", max_length=50)
    last_name = models.CharField("Nom", max_length=50)
```
_Warning : This file works in a linear system, which implies that for joins a table only knows the tables declared above it in the code of the file.

### Relations between tables
As with any database system, the relationships between tables must follow a standard.
#### Define a OneToOne relation :
```python
group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True)
```
_Group being the target class._
#### Define a ManyToOne relation :
```python
student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
```
_The class where it is defined is one, the target is many._
#### Definie a ManyToMany relation :
```python
teachers = models.ManyToManyField(Teacher)
```
_An association class will automatically be created in which an automatically generated id will be added._

## Django Shell (database) <a name="chapter-8-en"></a>
### Launch the shell
To fill the database django has its own shell. You can access it with the following command :
```bash
python manage.py shell
```
### Manipulate data
#### Import a table :
```bash
from grades.models import Student
```
#### Add an element to a table :
```bash
e = Student(serial_number='42424', first_name='foo', last_name='Bar')
e.save()
```
_Warning: a variable used in the shell remains registered, so remember to choose other names to create other elements._

#### Assign an element to a variable :
```bash
e = Student.objects.get(pk=1)
```
_Here we get the element by its id in Student table._

#### Add an object from an associasion class (ManyToMany) :
```bash
object.variable.add(object)
```
_We choose the object then its variable (which contains the other object) and then we add with add (). Of course in the parenthesis of the add it is necessary to indicate the variable of the shell which one chose beforehand (example for e = ... it is e)._

_Warning : don't forget to save the changes with 'yourvariable'.save()._

#### Show all content from a table :
```bash
from grades.models import Student
Student.objects.all()
```

#### Notes :
_If you don't want auto-generated id's add **primary_key=True** has your attributes before migrating the db otherwise it will generate an error or it will not be taken into account._

_In case of errors to migrate the db delete the content of migrations, as well as the python cache._

# mproject (Français)

## Table des Matières
  * [Présentation](#chapter-1-fr)
  * [Installation](#chapter-2-fr)
  * [Créer un projet](#chapter-3-fr)
  * [Structure d'un projet](#chapter-4-fr)
  * [Créer une nouvelle application](#chapter-5-fr)
  * [Les routes du site](#chapter-6-fr)
  * [Les modèles (base de données)](#chapter-7-fr)
  * [Le Shell de Django (base de données)](#chapter-8-fr)

## Présentation <a name="chapter-1-fr"></a>

### Description du projet
mproject est un site web crée dans le cadre d'un cours de haute école ayant pour but d'apprendre les bases du framework Django.

### License
Le framework Django est un logiciel open source sous [licence MIT](https://opensource.org/licenses/MIT).

## Installation <a name="chapter-2-fr"></a>

### Étape 1 : Installer python 3.8 (ou plus récent) :
Django est un framework qui utilise le langage python, il faudra donc avoir une version récente de python pour le faire fonctionner.
<a href="https://www.python.org/downloads/">[Télécharger Python]</a>

_Attention afin de pouvoir utiliser plus facilement les commandes python depuis le terminal windows il est utile d'ajouter python au PATH._
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

#### Lancer le serveur
```bash
python manage.py runserver
```

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

#### ajouter dans 'INSTALLED_APPS' de settings.py
```python
'grades.apps.GradesConfig',
```

## Les routes du site <a name="chapter-6-fr"></a>
Les routes du site sont géré par le fichier urls.py. Il en existe un pour le projet et un pour chaques application que vous créerez. Le fichier urls.py contient une liste "urlpaterns" qui contient toutes les routes pour le projet ou l'application auquel il appartient. 

Au sein de de cette liste chaques url est appellé par une fonction "path()" qui va contenir plusieur arguments :
```python
path('', views.index, name='index')
```
* **Premier argument : route (requis)** : Il s'agit d'une chaîne contenant un modèle d'URL.
* **Second argument : view (requis)** : Va lier le declanchement d'une fonction du fichier view.py a l'appel de cet url.
* **Troisième argument : kwargs (optionnel)** : Va permettre de spécifier un ou plusieurs argument pour la fonction ciblée.
* **Quatrième argument : kname (optionnel)** : Permet de nommer l'url.

## Les modèles (base de données) <a name="chapter-7-fr"></a>
Contrairement à d'autres framework django a son propre système de base de données. Ces base de données sont gérées par des modèles et l'utilisateur peut interragir avec elles directement via l'invite de commandes. Par default les base de données sont en sqlite3.

### Le fichier models.py
Il contient des classes qui correspondent a des tables dans la base de données et qui contiennent chaques colonnes sous forme d'argument.
```python
class Teacher(models.Model):
    trigram = models.CharField("Trigramme", max_length=3, unique=True, primary_key=True)
    first_name = models.CharField("Prénom", max_length=50)
    last_name = models.CharField("Nom", max_length=50)
```
_Attention ce fichier fonctionne de facon linéaire, ce qui implique que pour les jointure, une table ne connais que les tables déclarées au dessus d'elle dans le code du fichier._

### Les relations entre les tables
Comme pour tout système de base de données, les relation entre les tables doivent respecter une norme.
#### Definir une relation OneToOne :
```python
group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True)
```
_Group étant la classe ciblée._
#### Definir une relation ManyToOne :
```python
student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
```
_La classe ou on le défini est le one, la cible est le many._
#### Definir une relation ManyToMany :
```python
teachers = models.ManyToManyField(Teacher)
```
_Une classe d'associasion va automatiquement etre créer dans laquelle un id généré automatiquement va etre ajoutée._

## Le Shell de Django (base de données) <a name="chapter-8-fr"></a>
### Lancer le shell
Pour remplir la base de données django possède son propre shell. Vous pouvez y accéder via la commande suivante :
```bash
python manage.py shell
```
### Manipulater les données
#### Importer une table :
```bash
from grades.models import Student
```
#### Ajouter un élément a une table :
```bash
e = Student(serial_number='42424', first_name='foo', last_name='Bar')
e.save()
```
_Attention : une variable utilisée dans le shell reste enregistrée, pensez donc à choisir d'autres noms pour créer d'autres éléments._

#### Assigner un élément à une variable :
```bash
e = Student.objects.get(pk=1)
```
_Ici, nous obtenons l'élément par son identifiant dans la table Student._

#### Ajouter un objet a une table d'associasion (ManyToMany) :
```bash
object.variable.add(object)
```
_On choisit l'objet puis sa variable (qui contient l'autre objet) puis on rajoute avec add(). Bien entendu dans la parenthèse de l'add il faut indiquer la variable de la coque que l'on a choisi au préalable (exemple pour e = ... c'est e)._

_Attention : n'oubliez pas de sauvegarder les modifications avec 'votrevariable'.save()._

#### Afficher tous les éléments d'une table :
```bash
from grades.models import Student
Student.objects.all()
```

#### Notes :
_Si vous ne voulez pas que les identifiants générés automatiquement, ajoutez **primary_key=True** a vos attributs avant de migrer la base de données sinon cela générera une erreur ou il ne sera pas pris en compte._

_En cas d'erreurs pour migrer la db supprimez le contenu des migrations, ainsi que le cache python._

<p align="center">Copyright © 2021 InteralexDev | all rights reserved</p>