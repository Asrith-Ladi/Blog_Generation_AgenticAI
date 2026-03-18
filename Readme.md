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

Create src folder and __init__.py file inside src folder to consider that as package.

Under src folder we are going to create 4 folders.

- graphs
- llms
- nodes
- states
and __init__.py file inside each folder.

.env is going to hold all our important keys and secrets.

1) Langchain_project
2) langchain_api_key
3) groq_api_key


## Project Structure

```text
Blog_Generation_AgenticAI/
├── src/
│   ├── __init__.py
│   ├── graph/
│   │   └── __init__.py
│   ├── llms/
│   │   └── __init__.py
│   ├── nodes/
│   │   └── __init__.py
│   └── states/
│       └── __init__.py
├── images/
│   └── result.png
├── .gitignore
├── .python-version
├── NOTES.md
├── Readme.md
├── main.py
├── pyproject.toml
└── requirements.txt
```
once app.py file create then run `python app.py` file will handle to run uvicorn

To Test it we will use the postman https://www.postman.com/downloads/

There only we can give get and post requests to test the APIs.

0.0.0.0:8000 is basically referring to localhost url.

127.0.0.1:8000 is also referring to localhost url.

![Result](images/postman.png)