from initialize import driver, base_url, timeout, tweets_dir, tweets_container_xpath
from variables import accounts
import time
import json
import re


def handler() -> None:
    for account in accounts:
        driver.get(f'{base_url}/{account}')
        print(f'Scrape {account}')

        tweets = get_tweets()
        save_tweets(tweets, account)


def get_tweets() -> list:
    tweets = []
    times = []
    all_tweets_fetched = 0

    while True:
        try:
            tweets_container = driver.find_element('xpath', tweets_container_xpath)
        except:
            time.sleep(timeout)
            continue
        else:
            break

    while True:
        current_tweets = tweets_container.find_elements('xpath', './/div[@data-testid="cellInnerDiv"]')
        for tweet in current_tweets:
            tweet_time = get_tweet_time(tweet)
            tweet_text = get_tweet_text(tweet)
            tweet_event = get_tweet_event(tweet)
            tweet_owner = get_tweet_owner(tweet)

            if tweet_time and tweet_time not in times:
                times.append(tweet_time)
            else:
                continue

            tweets.append({
                'time': tweet_time,
                'text': tweet_text,
                'event': tweet_event,
                'owner': tweet_owner
            })

            if all_tweets_fetched > 20:
                break
            else:
                all_tweets_fetched += 1
        else:
            scroll_down()
            continue

        break

    return tweets


def get_tweet_time(tweet) -> str:
    try:
        tweet_time = tweet.find_element('xpath', './/time[@datetime]').get_attribute('datetime')
    except:
        tweet_time = None
    finally:
        return tweet_time


def get_tweet_text(tweet) -> str:
    try:
        tweet_text = tweet.find_element('xpath', './/div[@data-testid="tweetText"]').text
    except:
        tweet_text = None
    finally:
        return tweet_text


def get_tweet_event(tweet) -> str:
    try:
        tweet_event = tweet.find_element('xpath', './/span[contains(@id, "id__")]').text
    except:
        tweet_event = None
    finally:
        return tweet_event


def get_tweet_owner(tweet) -> str:
    try:
        tweet_owner = tweet.find_element('xpath', './/div[@data-testid="User-Names"]/child::div[2]').text
        tweet_owner = re.findall(r'@(\w+)', tweet_owner)[0]
    except:
        tweet_owner = None
    finally:
        return tweet_owner


def scroll_down()  -> None:
    try:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    except:
        raise Exception('Something went wrong while scrolling down')


def save_tweets(tweets, account) -> None:
    with open(f'{tweets_dir}/{account}.json', 'w', encoding='utf-8') as file:
        json.dump(tweets, file, indent=1)


def fetch_tweets() -> None:
    handler()
