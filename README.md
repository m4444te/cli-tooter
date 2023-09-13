# fedi-cli

A Command Line Interface (CLI) that take text as input and post in on the Fediverse

## Installation

Clone the repository :

```sh
git clone git@github.com:spinning-fantasies/fedi-cli.git
```

Activate a virtualenv :

```sh
cd fedi-cli
python -m venv .
source ./bin/activate
```

Install the dependencies :

```sh
python -m pip install -r requirements.txt
```

Add environment variables to `.env` :

```sh
MASTODON_INSTANCE_URL=<your_mastodon_instance_url>
MASTODON_ACCESS_TOKEN=<your_mastodon_access_token>
```

Install using [pipx](https://github.com/pypa/pipx) :

```sh
pipx install -e .
```

## Usage

Share a message to the Fediverse :

```sh
toot "Hello World!"
```
