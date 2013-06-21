browserexpose
=============

Shows all open windows across all virtual screens in a Linux system as mini screenshots in a browser. Clicking on a snapshot in the browser raises the 'real' window &amp; gives it focus.

Prerequisites:
    Python
    wmctrl

Usage:
   in the project directory, run:  python -m CGIHTTPServer
   in the browser, go to localhost:8000/desktop.html
   
I did try running this through Apache, but the permissions and X authorization for wmctrl were a big headache.
