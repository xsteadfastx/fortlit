fortlit
=======

[![Build Status](https://cloud.drone.io/api/badges/xsteadfastx/fortlit/status.svg)](https://cloud.drone.io/xsteadfastx/fortlit)

A fortune like program that displays a quote from literature where the actual time is mentioned.

Inspired from the [E-reader clock](https://www.instructables.com/id/Literary-Clock-Made-From-E-reader/) project from [Jaap Meijers](http://www.eerlijkemedia.nl/).

## Installation

`pip install -U git+https://github.com/xsteadfastx/fortlit.git#egg=fortlit`

or

`pipsi install git+https://github.com/xsteadfastx/fortlit.git#egg=fortlit`

or

1. Be sure you have Python 3.6  or Python 3.7 installed
2. Download `pyz` file from [release](https://github.com/xsteadfastx/fortlit/releases)
3. Move it to a place in your `$PATH`

### Fish Shell

i have this in my `~/.config/fish/config.fish`:

```
function fish_greeting
  if test -f ~/.local/bin/fortlit
    fortlit
  end
```
