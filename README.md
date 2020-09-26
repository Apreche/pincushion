# pincushion
Aggregate web activity into pinboard.in

## Summary

I used to use an online service to gather my activity from several different web sites and collect it into pinboard.in. However, that service is now charging too much money, so I wrote this little project to replace it.

## Usage

This project contains several small utility functions and API client code that could be useful if another Python project were to import it. However, the primary usage is to simply configure the app and run it in a cron at the desired frequency.

## Settings

This application gets all of its settings from environment variables. Check the settings.py to see the environment variables and set them in a way that is appropriate for your environment. Be sure to keep the envirionment variables properly secured as they will contain secrets that allow API access to various online services.
