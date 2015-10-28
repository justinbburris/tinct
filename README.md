Tinct
=====

Control your Phillips Hue lights via a touch screen raspberry pi

## Equipment needed

* raspberry pi
* raspberry pi touch display
* wifi dongle
* power adapter

## Setup

### Python

I use Python 2.7.10 and pyenv + pyenv-virtualenv to manage my python verion

```
$ pyenv install 2.7.10
$ pyenv virtualenv 2.7.10 tinct
```

### Install dependencies

```
$ pip install -r requirements.txt
```

## Development

### New depenencies

When adding new depencies, be sure to add them to the requirements.txt file

```
$ pip freeze > requirements.txt
```

## Roadmap

* I plan to use Kivy to drive the GUI and to intercept the touch events

* To start, all connections will be hardcoded to my current home

* I need to make API calls to my local Hue lights

* After hardcoded connections work with touch events, work on a manager

## Testing

:boom: I have no idea how to test this yet :boom:
