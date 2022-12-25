# Twitter Scraper

**The Twitter Scraper project has minimal development and is very simple. It's light (to use resource).**

**You can use the Core of this project in your projects as a tool for scraping.**

## Setup and Run

### Clone

```bash
git clone --branch master https://github.com/pourya90091/Twitter-Scraper.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Config

- Set web app settings at `scraper/settings.py`.
- Select accounts to scraping at `core/variables.py`.

### Run

- Scraper (selenium bot) must be run manually and as another process.

```bash
python main.py
```

## Tips

>**Tip** : On some hosts that give limited permission, you need to install `chromedriver` manually and place it at `core/` and change `executable_path` to "chromedriver" (it means don't use relative or absolute path).

>**Tip** : On some hosts you don't need to set `executable_path` (remove `service`).

>**Tip** : You can find `executable_path` at `core/initialize.py`.
---
