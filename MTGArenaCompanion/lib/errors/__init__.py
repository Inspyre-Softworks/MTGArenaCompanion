
class ConfigAvailabilityError(Exception):
    def __init__(self):
        statement = "MTGArena Companion must have a designated directory in which to place crucial files." \
                    "\n\nOnce you've determined where that should be, please run the program again. "
