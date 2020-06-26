# kusama-api
Kusama microservice API providing REST endpoints for multi-signature trading, originally built for [LocalCoinSwap](https://localcoinswap.com)

----

# Building and deployment

### Build for production

```bash
export CONTAINER_REPO=YOUR_CONTAINER_REPO_NAME_OR_URL # Update this with your dockerhub username
export IMAGE_NAME=kusama-api
export COMMIT_HASH=$(git rev-parse --short HEAD)
CONTAINER_REPO=$CONTAINER_REPO IMAGE_NAME=$IMAGE_NAME COMMIT_HASH=$COMMIT_HASH docker-compose -f docker-compose.prod.yaml build
```

### Push the image to container repo

```
docker push $CONTAINER_REPO/$IMAGE_NAME:$COMMIT_HASH
```

### Initiate a rolling deployment

```
kubectl edit deployments.apps/kusama-api-deployment
```

It'll open up default editor. Look for the container repo and image name. Change the image tag and save & exit. It will start rolling deployment without causing any outage.


## Pre-requisites

 - Python 3.8.1 (preferred)

We suggest using [`pyenv`](https://github.com/pyenv/pyenv-virtualenv) to easily manage python versions. Some of the following commands use `pyenv`.
Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for easy installation. Then add pyenv-virtualenv plugin to it.

### Configure local development setup

 - Install and activate python 3.8.1 in the root directory
    - `pyenv install 3.8.1`
    - `pyenv virtualenv 3.8.1 ksmapi`
    - `pyenv local ksmapi`

 - Install project requirements
    - `pip install -r requirements.txt`

 - Install precommit hook
    - `pre-commit install`

You're all set to hack!

Before making changes, let's ensure tests run successfully on local.

### Running Tests

 - Run all tests with coverage
    - `coverage run -m pytest -v`
 - Show report in terminal
    - `coverage report -m`
