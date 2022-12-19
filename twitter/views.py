from django.shortcuts import render
from utils.utils import access_check
from core.variables import accounts
from django.conf import settings
import json
import os

# Create your views here.

tweets_dir = f'{settings.BASE_DIR}/core/tweets'

@access_check
def index(req):
    tweets = []

    for account in accounts:
        if f'{account}.json' in os.listdir(tweets_dir):
            with open(f'{tweets_dir}/{account}.json', 'r') as file:
                tweets.append(json.load(file)[0])

    return render(req, 'twitter/index.html', {'tweets': tweets})


@access_check
def profile(req, account):
    tweets = []

    if f'{account}.json' in os.listdir(tweets_dir):
        with open(f'{tweets_dir}/{account}.json', 'r') as file:
            tweets = json.load(file)

    return render(req, 'twitter/profile.html', {'tweets': tweets, 'account': account})
