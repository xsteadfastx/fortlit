"""Print literature quote from time."""
from datetime import datetime

from fortlit import lit_time


def entrypoint() -> None:
    """Entrypoint."""
    print(lit_time.create(datetime.now().strftime("%H:%M")))
