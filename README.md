# url-auth-open-linux
This is a small script using Selenium and geko to load a web page, use the HTML in the page to get the login form. This will then open a Firefox browser pane with your logged in.

This project requires the gekodriver found at (https://github.com/mozilla/geckodriver/releases)
Also, "python -m install selenium" is required to install the Selenium package to run the above driver.

The intent behind this script is to have an auto-login functionality that can be triggered on system startup. 
