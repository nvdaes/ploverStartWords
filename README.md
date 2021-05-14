# Plover Start words #

This plugin provides a meta for Plover, so we can choose the output produced deppending on the last typed text.

Based on plugins like [plover_merge_words](https://github.com/morinted/plover_merge_words).

## Usage ##

```

# initial.json
{
"STROke": "{:initial:textStartingNextWord | textFollowingPreviousFragment}"

...
}

```

## API ##

API can be manipulated via [Python dictionaries](https://github.com/benoit-pierre/plover_python_dictionary).

For example:

```

# single.py
from plover_start_words import meta

meta.prefixes = ("", "foo", "var")

LONGEST_KEY = 1


def lookup(key):
	raise KeyError

```

## Versioning ##

We use [SemVer](https://semver.org/).

## Changes ##

[Changelog](https://github.com/nvdaes/plover_start_words/blob/master/CHANGELOG.md)
