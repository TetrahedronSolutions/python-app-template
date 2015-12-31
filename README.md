Template: Python applications

## Inspire by
[Jeff knupp](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
[Open Stack](http://openstack.com/)

---

# GOAL
## Primary
The purpose of this is to create proper python applications with file structures, documentation, testing, and tools to use.

## Secondary
From this template we will be constructing either a python scaffolding tool or
using yeoman.io to scaffold our python projects.

---

# Tools

## Virtualenv
This is your best friend. Virtualenv is a applications that isolates your local environments python libary/packages with a fresh install python. This is good in order to limit the things that you need to install in order to run your application and not be affected by other existing modules.

### How to:
#### install `sudo apt-get install virtualenv`

#### Use `virtualenv <environment-name>`

## Docker
This could be an alternative to virtualenv its just a bigger environment isolation. Instead of python libary level it would be a kernel level umbrella.

## Tox
[Tox](http://tox.readthedocs.org/en/latest/example/basic.html)

Tox is a generic virtualenv management and test command line tool you can use for:

* checking your package installs correctly with different Python versions and interpreters
* running your tests in each of the environments, configuring your test tool of choice
* acting as a front-end to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

.... SO in order words this tools allows you to manage your virtual environments
with a wide range of tests not just py27. Handles that all installations and
testing is done with various environments with you having to do it by had.


## Pip
This is your package manager. if you need to install a lib you will need to add
you will run `pip install <lib>` or you will create a `requirements.txt` file
in order to keep track of all the lib that belong to that program and the
correct version of the libs that one needs to install. Run this file by running
`pip install -r <file_name>`. If you have ever played with node.js, the
requirements.txt is similar to the package.js file. If you ever do get to a
point of where you are installing packages and don't know their version, just
run `pip freeze` and it will echo a list of the installed python packages/libs
with their versions. if you do not have a requirements.txt file you can run
`pip freeze > requirements.txt` and there you go. :)

##### file example
```
argparse==1.2.1
coverage==4.0.3
flake8==2.2.4
flake8-docstrings==0.2.4
hacking==0.10.2
mccabe==0.2.1
```



## Git Flow
[Git-flow](http://nvie.com/posts/a-successful-git-branching-model/)
[atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
