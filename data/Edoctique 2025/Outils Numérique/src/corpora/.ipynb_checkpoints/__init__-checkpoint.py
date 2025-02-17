
import logging

from pathlib import Path
print("Initializing the lib package corpore")

# Initialize some variables, configuration, etc.
config = {
    "version": "0.0.alpha",
    "author": "Jules Nuguet",
}

from .ach import achP
from .corpora import corporaMenu
__all__ = ["achP","corporaMenu"]