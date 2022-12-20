from initialize import driver
from core import fetch_tweets
from typing import NoReturn


def main() -> NoReturn:
    while True:
        fetch_tweets()

if __name__ == '__main__':
    try:
        main()
    except (Exception, KeyboardInterrupt) as err:
        if type(err) is KeyboardInterrupt:
            err = 'Interrupted'
        print('\nError:', err)
        exit()
    finally:
        print("\nWait for the WebDriver to quit")
        driver.quit()
