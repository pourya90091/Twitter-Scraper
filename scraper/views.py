from django.shortcuts import render, redirect
from django.urls import reverse
import re

# Create your views here.


def index(req):
    if 'Cookie' in req.headers:
        code = re.findall(r'access_token=(.+)', req.headers['Cookie'])
        if code:
            return redirect(reverse('twitter-index'))

    return render(req, 'index.html')


# partial view
def header(req):
    return render(req, 'components/header.html', {})


def footer(req):
    return render(req, 'components/footer.html', {})
