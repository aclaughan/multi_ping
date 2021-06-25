import os
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    with open("targets.txt") as inFile:
        targets = inFile.read().splitlines()

    for target in targets:
        response = os.system("ping -c 3 " + target)

        if response == 0:
            logging.info(f"{target} is reachable")


if __name__ == '__main__':
    main()

# logging.debug(stuff)
