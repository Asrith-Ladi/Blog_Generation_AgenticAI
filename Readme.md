# **Introduction**

- This blog can be generated based on Topic, Topic and Language, Transcript of Youtube video.
## We are going to build this

![Result](images/result.png)

- Here we are not focussing much on frontend, we will be using FASTAPI, FAST API framework in order to create the APIs itself.

- We are going to use UV Package manager, which is a fast, reliable and easy to use Python package and dependency manager.

Now, we are going to do the project structure setup with help of UV Package.

https://docs.astral.sh/uv/getting-started/installation/

once we hit the command
`uv init`

These files got created.

- .python-version
- main.py
- pyproject.toml

create an virtual environment

`uv venv`

- Whatever the packages you keep on adding you will be able to see that particular package over here.

Activate with: `.venv\Scripts\activate`

Now create the requirements.txt file and required packages.

if you want to install single packages use `uv add <package_name>`

if you want to install multiple packages use `uv add -r requirements.txt`

pyproject.toml is the file where we are going to update the names of  all the installed packages.