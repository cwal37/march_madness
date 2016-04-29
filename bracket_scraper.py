# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""


"""
Everything within the 3 quotes should appear green in spyder, easiest way to 
think about this section is a super comment, it's a way to write things out
that don't get executed as code, but also aren't comments, which start with # and
everything to their right on the line will also not be executed. My notes within
the code will be that kind of comment. Personally, I like to change their color
from the default grey to a bright purple/pink, but you could change it to 
whatever you want by going to Tools->Preferences->Syntax Coloring->Spyder Tab->
scroll down to Comment-> click on color box to change to whatever.

Other useful tips, highlight a word to have that word be highlighted everywhere 
in your script, right click to carry out some common actions, like commenting out 
everything you currently have highlighted. You'll also notice certain other things,
like if you type (, [, or { it will automatically generate the closing partner
at the same time. These are IDE behaviors to make coding generally more stream
lined and pleasant. 

This is a super simple way to webscrape and it has a pretty short "critical path"

1. Actually open a web browser
2. Navigate to desired page
3. Perform action
4. Close


Now obviously there's more to it than that, but this is really a pretty 
chill thing. I'll go through the steps in detail in the code below.
"""
# So Python can do a lot of things on its own, but the really amazing value
# comes from the packages that other people have built to do all sorts of neat
# things. These aren't inherently in a script you're writing, so you have to call
# them right off the bat in order to be able to use their functions. Winpython
# comes packaged with a boatload of common (and more niche) python packages, 
# so you typically don't have to worry about installation, but can just call 
# the once i'm showing you here. I can show you the quickest way to install a
# new pacakge when you need, the vagaries of pip confused me at first (like where
# I was even supposed to be using it).

# So, from the package (or library, another name) selenium we're importing the
# specific function webdriver you could also do, from selenium import *
# * is a wildcard that typically means everything, but here we're only using
# webdriver, so we'll just grab that.
from selenium import webdriver

# in this line, I'm importing the entire pandas package as pd. Specifying an "as"
# is helpful, because you can use that shorthand in the rest of your script 
# instead of writing out pandas every time you want to use a function. We're 
# not actually using pandas in this script, but it is an excellent data 
# management package that I use constantly and would use to package and manipulate
# the actual scraped data from the jeopardy page.I wanted to get you something
# asap, but I'll write a little thing to show some pandas basics as well
# (of course you can always google guides from people more competent than myself)
import pandas as pd

# here, we're using webdriver to say that our webdriver (browser, literally "driving"
# our web experience) is goign to be firefox, and we're assigning it to the
# variable driver. This is step 1, a single line of code.
driver = webdriver.Chrome()

# .get is a specific function of a webdriver once you've declared it. get takes
# you to a specific webpage, here' we're going to espn's NCAAM bracket page
# This is step 2, also a single line of code
driver.get('http://espn.go.com/mens-college-basketball/tournament/bracket')

# in Python, things inside of [] are generally lists. I'm declaring an empty list
# here under teh variable name teams. It will hold the teams we're gonna grab
# from the ESPN site. This is prep for Step 3. Step 3 is by far the msot variable,
# and will be the vast bulk of any project. You could break it out into an action
# and analysis if you wanted to, but I was trying to prevent as condensed a 
# version as possible in order to facilitate understanding.
teams = []

# this is the main (and only) loop here this first line, initializing the loop
# is saying that it's going to go through all the elements on the webpage that
# have the HTML tag of 'a' the team is because I know that these are ultimately
# going to be teams, but team could be x or y or z or flagrgardl. I'm declaring
# in that moment of writing team that there are n number of elements in the
# second, conditional piece of the loop intitialization statement, and the loop 
# will go through n iterations until there are no more of team in the HTML elements
# on the page that have the tag of 'a'. find_elements_by_tag_name is another 
# function of the webdriver class (which we initialized using firefox under the
# variable name of "driver").
for team in driver.find_elements_by_tag_name('a'): # select the url in href for all a tags(links) look, comments can go anywhere(ish)

    # I know within those 'a' tagged elements that the team name is futher 
    # delineated by the HTML attribute of 'title', so I'm getting that section
    # and making sure it's a string (a datatype), by wrapping the call in str
    team_name = str(team.get_attribute('title'))
    
    # but crap, there are still things that aren't team names, little bits and
    # pieces of random junk because HTML is hot bullshit. Here, I'm using an if
    # statement in conjunction with the built-into-python len function to determine
    # if the length of the team_name I just grabbed is greater than 2. If it is greater 
    # than 2 it's an actual team name (note: this was something I just had to parse
    # out for myself, always trial and error when working with HTML in this way
    # there are other ways, automatic parses that strip out the crap, but I find
    # it easier to just reach into HTML's guts and pull out what I need while
    # scraping off the random detritus I brought back with it)
    if len(team_name)>2:
        # I'm printing each team name because I like to see it sometimes if
        # I'm just eyeballing for errors
        print team_name
        # remember when I declared that empty list of teams? Here I'm appending
        # every genuine team in the webpage to that list
        teams.append(team_name)


# closing and quitting the webdriver. ACtually really important because it will
# fill up your harddrive with random junk if not closed properly.
driver.close()
driver.quit()

""" 
The neat thing about Spyder is you can now look at teh list of teams by clicking
on teams in the variable explorer pane. It's oriented towards sceientists and
data stuff where you're not exactly hardcore coding, but it provides an excellent
quick check for someone like me who started in Matlab is is mostly dealing with
data issues and other similar things anyways.
"""
    
    

        
    
