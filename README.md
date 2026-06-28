# Spotify Background Setter

This program periodically sets your Windows 11 desktop background to be the last album you played on your Spotify account. It checks the last 15 (for now) songs you've played on Spotify; if at least one of them was listened in the context of an album, it sets your desktop background to be that album cover; otherwise, nothing is changed.

Note that playing from a playlist, or looking a song up and playing it does NOT count as 'album context'; you need to go to an album and listen to at least one song from start to end for it to be considered 'recent' and in an 'album context'.

Downloaded album covers can be found at the root of your repo under `\downloaded_covers\artist\album\cover.png` after at least changing your desktop background once. DO NOT delete the album cover image after it has been downloaded; delete the directory of that album entirely if you wish to delete its album cover.

<img src="https://github.com/Ayk-12/spotify-background-setter/blob/main/Screenshots/underscores%20-%20U%20with%20a%20blue%20background.jpg"/>

A bit of setting up is needed for the program to work properly. Here are the steps below.

## Setup

You need to have a working and active Spotify Premium account for this to work. The premium plan for the account does not matter. This should not affect other accounts if your premium plan is shared.

### Python

1. Download and install Python.
2. Install the necessary Python libraries:
    - Spotipy: `pip install spotipy`
    - Win11Toast: `pip install win11toast`

### Spotify Web API

You can follow the guide to create your web app [here](https://developer.spotify.com/web-api/); but these are the basic steps:
1. Visit [Spotify for Developers dashboard](https://developer.spotify.com/dashboard).
2. Login with your premium account.
3. Create an app. You can call it anything you want (I called it "Background Changer").
4. You can use any valid redirect URI (I used `http://127.0.0.1:9090`).
5. Select "Web API" for the question asking which API you want to use.

From the app, we need the Client ID, Client Secret, and Redirect URI.

### Environment Variables

Copy your Client ID, Client Secret, and the Redirect URI; look up "Edit the system environment variables" on your machine. Add the three to your System Variables:
- `SPOTIPY_CLIENT_ID=your-client-id`
- `SPOTIPY_CLIENT_SECRET=your-client-secret`
- `SPOTIPY_REDIRECT_URI=your-redirect-uri`

### Repo

Clone the repo somewhere on your machine (I keep it under Documents).

### Task Scheduler

Although the program can be run manually, it is intended to be run automatically using Task Scheduler.
Create a new task, call it whatever you want, set it to be triggered however you want. Under "Action", add a new action. Choose "Start a program", and for "Program script" paste the path to your `python.exe`. In my case, it's: `C:\Users\Owner\AppData\Local\Programs\Python\Python312\python.exe`. If your path has spaces in it, surround it with double quots

For "Arguments", copy the path to `spotify_handler.py`. Again, if the path has spaces in it, surround it with double quotes.

#### Choose the correct Python version

If you have many Python versions installed, choose the one that has the required libraries for that version. For example, I can find my installed Python packages under `C:\Users\Owner\AppData\Local\Programs\Python\Python312\Lib\site-packages` for Python 3.12. Choose the version where you can find your installed Spotipy and Win11Toast libraries under `site-packages`.

### First Run

I recommend running the program for the first couple of times manually, then you can set up the Task Scheduler (or schedule it to run every five minutes, then set it to whatever you want). On the first run, you will be prompted to open a link from your terminal. Click on the link; you will be redirected to another page. Copy the link of that page, paste it into the terminal, and press Enter. The program should run and a `.cache` file should appear in the root of the repo.

After you are sure that `.cache` file is at the root of the repo, you can change the `...\python.exe` to `...\pythonw.exe` in the Task Scheduler (`python.exe` opens a terminal; `pythonw.exe` does not).

### Background Settings

If all works correctly, your background should be set to the last album you recently played. But the image may be stretched, tiled, etc. depending on your previous desktop background settings. To edit, go to Personalization > Background in your Settings, and "Choose a fit for your desktop image". I personally like the 'center' option, then I choose an appropriate background color from the background settings.

### More?

- Could add a `blacklist` option so the program can ignore certain artists/albums
- Could edit the image using `PIL` before setting it as the background (don't know what I would change though)