"""Everything that is needed to create literature string from time."""
import json
import re
from random import choice

import pkg_resources


def create(time: str) -> str:
    """Find literature for time."""
    with open(
        pkg_resources.resource_filename(__name__, "data/times.json"), "r"
    ) as times_file:
        times = json.load(times_file)

    if time in times.keys():
        quote = choice(times[time])

        text = re.sub(
            quote["time"],
            "\x1b[1m\x1b[95m{time}\x1b[0m".format(time=quote["time"]),
            quote["text"],
            flags=re.IGNORECASE,
        )

        return "\n{text}\n- {book}, \x1b[1m{author}\x1b[0m\n".format(
            text=text, book=quote["book"], author=quote["author"]
        )

    return ""
