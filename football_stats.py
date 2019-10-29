#!/usr/bin/python
# -*- coding: utf-8 -*-

"""football_stats.py: IS 211 Assignment 9."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin510@spsmail.cuny.edu'

# Imports
import sys
import urllib.request as request
import urllib.error
from bs4 import BeautifulSoup as bs

def print_stats(stats):
    """
    Prints player names, positions, teams, and touchdowns in a table.

    Parameters:
        stats (tuple): A tuple of stats to be printed
    
    Example:
        >>> print_stats(stats)
    """

    print("\nNFL Top 20 Players' Stats\n")
    # Print header border
    print("+-{:<30}-+-{:<20}-+-{:<20}-+-{:>10}-+".format("-"*30, "-"*20, "-"*20, "-"*10))
    # Print the header
    print("| {:<30} | {:<20} | {:<20} | {:>10} |".format(
        'Player', 'Position', 'Team', 'Touchdowns'))
    
    # Print the players' stats
    for stat in stats:
        # Print the cell separators
        print("|-{:<30}-+-{:<20}-+-{:<20}-+-{:>10}-|".format("-"*30, "-"*20, "-"*20, "-"*10))
        # Print the player's stats
        print("| {:<30} | {:<20} | {:<20} | {:>10} |".format(
            stat[0], stat[1], stat[2], stat[3]))

    # Print footer border
    print("+-{:<30}-+-{:<20}-+-{:<20}-+-{:>10}-+".format("-"*30, "-"*20, "-"*20, "-"*10))


def get_html(url):
    """Accepts a URL as a string and opens it.

    Parameters:
        url (string): the url to be opened

    Example:
        >>> get_html(
            'https://www.nasdaq.com/symbol/aapl/historical')
    """

    response = request.urlopen(url).read()
    html = bs(response, 'lxml')

    return html


def get_top_20_stats(html):
    """Accepts a BeautifulSoup object and parses it.

    Parameters:
        html (BeautifulSoup): the content to be parsed

    Example:
        >>> get_top_20_stats(html)
    """


def main():
    """The method that runs when the program is executed."""

    # Set the URL
    url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'

    #https://www.cbssports.com/nfl/stats/playersort/sortableTable/nfl/year-2019-season-regular-category-touchdowns?:sort_col=7&:sort_dir=1

    # Get the HTML
    html = get_html(url)
    # Parse the top 20 players' stats from the HTML
    stats = get_top_20_stats(html)
    # Print the stats
    print_stats(stats)

    # Exit the program after the stats are printed
    sys.exit()

if __name__ == '__main__':
    main()
