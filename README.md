# Python Template 🐍
A template repo holding Roboflow's common setup for a python project.

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
├── README.md
├── pyproject.toml
├── src
│   └── sandbox
│       ├── __init__.py
│       └── hello.py
└── test
    └── test_hello.py
```

### Code Quality 🧹

We use `pre-commit` to ensure code quality. You can install it using:

```bash
pre-commit install
```

You can run the checks manually on all files:

```bash
pre-commit run --all-files
```

So far, **there is no types checking with mypy**. See [issue](https://github.com/roboflow-ai/template-python/issues/4).

### Tests 🧪

[`pytest`](https://docs.pytest.org/en/7.1.x/) is used to run our tests.

```bash
export PYTHONPATH=src
pytest
```

### Publish on PyPi 🚀

**Important**: Before publishing, edit `__version__` in [src/sandbox/__init__.py](/src/sandbox/__init__.py) to match the wanted new version.

We use [`twine`](https://twine.readthedocs.io/en/stable/) to upload our package.

```bash
# Build the package
python3 -m build

# Upload to TestPyPI (to verify everything is correct)
# Note: For TestPyPI you need to use your TestPyPI credentials
twine upload -r testpypi dist/* --verbose

# Upload to PyPI
twine upload dist/* --verbose
```

**Note**: For authentication, we recommend using [API tokens](https://pypi.org/help/#apitoken). Set `TWINE_USERNAME` to `__token__` and `TWINE_PASSWORD` to your token value.

### CI/CD 🤖

We use [GitHub actions](https://github.com/features/actions) to automatically run tests and check code quality when a new PR is done on `main`.

On any pull request, we will check the code quality and tests.

When a new release is created, we will try to push the new code to PyPi. We use [`twine`](https://twine.readthedocs.io/en/stable/) to make our life easier.

The **correct steps** to create a new realease are the following:
- edit `__version__` in [src/sandbox/__init__.py](/src/sandbox/__init__.py) to match the wanted new version.
- create a new [`tag`](https://git-scm.com/docs/git-tag) with the release name, e.g. `git tag v0.0.1 && git push origin v0.0.1` or from the GitHub UI.
- create a new release from GitHub UI

The CI will run when you create the new release.

# Q&A

## Why no cookiecutter?
This is a template repo, it's meant to be used inside GitHub upon repo creation.

## Why reinvent the wheel?

There are several very good templates on GitHub, I prefer to use code we wrote instead of blinding taking the most starred template and having features we don't need. From experience, it's better to keep it simple and general enough for our specific use cases.
