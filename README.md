# [Google Image Scraper](https://github.com/BlackDagger007/Google-Image-scraper)
This repo contains python code to scrapes high resolution images from google using selenium and chromedriver

* [Features](#features)
* [Requirements](#requirements)
* [Install](#install)
* [Usage](#usage)
* [Motivation](#motivation)

## Features
* Lightweight and fast
* Works in background
* Open source and free

## Requirements
* Chrome browser and appropriate chromedriver (see [link](https://chromedriver.chromium.org/downloads#h.p_ID_32))

## Install
Make sure to have all packages in main.py installed eg.
  ```sh
  $ pip install selenium
  ```
  
  ## Usage
  > After running main.py
  1. Enter `'Search Term':` 
     * _str_ Term to be searched in Google
  2. Enter `'Number of Images':` 
     * _int_ Number of images to scrape from Google
  4. All images scraped will be saved in `~/Downloads/_{Search_Term}` directory
  3. Thats it! _Directory opens up upon completion_
  
  ## Motivation
  You guessed it, boredom!
