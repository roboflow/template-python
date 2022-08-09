# Python Template 🐍
A template repo holding our common setup for a python project.

## Installation

You can install the package using pip

```bash
pip install -e .
```

or for development

```bash
pip install -e ".[dev]"
```

## Structure

The project has the following structure

```
├── .github
│   └── workflows
│       └── test.yml # holds our github action config 
├── .gitignore
├── Makefile
├── README.md
├── setup.py
├── src
│   ├── __init__.py 
│   ├── hello.py 
└── test 
    └── test_hello.py
```

### Code Quality 🧹

We provide two handy commands inside the `Makefile`, namely:

- `make style` to format the code
- `make check_code_quality` to check code quality (PEP8 basically)

So far, **there is no linting with mypy`. See [issue](link) 

### Tests 🧪

[`pytests`](https://docs.pytest.org/en/7.1.x/) is used to run our tests.

### CI/CD

We use [GitHub actions](https://github.com/features/actions) to automatically run tests and check code quality when a new PR is done on `main`.


# Q&A

## Why no cookiecutter?
This is a template repo, it's meant to be used inside GitHub upon repo creation.

## Why reinvent the wheel?

There are several very good templates on GitHub, I prefer to use code we wrote instead of blinding taking the most starred template and having features we don't need. From experience, it's better to keep it simple and general enough for our specific use cases.