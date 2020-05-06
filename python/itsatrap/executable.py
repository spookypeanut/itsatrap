import sys
from time import sleep
import getpass
from pathlib import Path

from itsatrap.trap import Trap

# Touch a file every minute, so we know when the battery ran out
TOUCHPATH = "/tmp/itsatrap.%s.touch" % getpass.getuser()


def main():
    if sys.argv[0] == "itsadryrun":
        photos = False
    else:
        photos = True
    trap = Trap(photos=photos, verbose=True)
    print("Starting trap, touching %s" % TOUCHPATH)
    touchfile = Path(TOUCHPATH)
    trap.start_trap()
    try:
        while True:
            sleep(60)
            touchfile.touch()
    except KeyboardInterrupt:
        print("Stopping trap")
        trap.stop_trap()

if __name__ == "__main__":
    main()
