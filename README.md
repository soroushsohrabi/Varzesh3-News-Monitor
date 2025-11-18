# Varzesh3 News Monitor

I made this small script because I kept checking Varzesh3 for new
headlines and eventually got tired of refreshing the page. So this
little tool simply looks at the site every couple of minutes and notes
down any links that weren't there before. Nothing fancy --- just
something practical that does the job.

## What it actually does

The script loads the main page, grabs the links it finds, and compares
them to whatever is already saved in a text file.\
If something new shows up, it gets added --- **and in the updated
version, the script also downloads and saves the main image of each new
headline.**

## Setup

You only need Python 3 and a couple of common libraries:

``` bash
pip install -r requirements.txt
```

## How the project is laid out

    Varzesh3-News-Monitor/
        varzesh3_scraper.py
        links.txt
        images/
        README.md

## Running it

Just run the script normally:

``` bash
python3 varzesh3_scraper.py
```

It keeps looping every two minutes. If you want a different interval,
you can change the value inside the script --- nothing complicated.

## A few notes

-   The updated version saves images into an `images/` folder
    automatically.
-   If you're planning to leave it running for hours, tools like tmux or
    screen help keep it alive in the background.
-   You can easily adjust it to save timestamps, export JSON, or scrape
    different parts of the site. The code isn't complicated, so tweaking
    it should be straightforward.


