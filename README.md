# substrate-api
Substrate microservice API providing REST endpoints for multi-signature trading, originally built for [LocalCoinSwap](https://localcoinswap.com)

----

## Pre-requisites

 - Python 3.8.1 (preferred)

We suggest using [`pyenv`](https://github.com/pyenv/pyenv-virtualenv) to easily manage python versions. Some of the following commands use `pyenv`.
Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for easy installation. Then add pyenv-virtualenv plugin to it.

### Configure local development setup

 - Install and activate python 3.8.1 in the root directory
    - `pyenv install 3.8.1`
    - `pyenv virtualenv 3.8.1 substrateapi`
    - `pyenv local substrateapi`

 - Install project requirements
    - `pip install -r requirements.txt`

 - Install precommit hook
    - `pre-commit install`

 - Create a file `local.env` in `service/config/local.env` from `example-local.env`

You're all set to hack!

Before making changes, let's ensure tests run successfully on local.

### Running Tests

 - Run all tests with coverage
    - `coverage run -m pytest -v`
 - Show report in terminal
    - `coverage report -m`
