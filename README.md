This was a project to some computer class I took. It is a website in which you can create a different kind of poll, in which two images of the options appear side by side and you choose the 'winner'. Many votes are collected to create a ranking.

- What do you need to run this?

You need at least Flask and Flask-PyMongo (python packages, both can be installed with pip) and mongo (search for mongodb).
You may need something else that I do not remember.

To run, run python runserver.py at the root of the repo.


- Some info about the organization of files:

The file 'views' contains the methods regarding requests. The urls of our application are declared there.
If you want to check out the models (they're already pretty complete), look at poll_models.
The file repository.py has the methods that you'll use to access the DB.
'poll_service' is where the logic that the views use should be. DO NOT WRITE A BUNCH OF CODE IN A VIEW METHOD. This should be done here.

The folder 'templates' contains the html files. 'rankings' is the main page, and 'new-poll' and 'edit-poll' are the pages to 1)create a new poll (duh) and 
2) add a new option to a poll.

The folder 'static' contains a lot of stuff, mostly files regarding bootstrap and knockout, which we don't have to deal with. The interesting file in this folder are 
the .js and .css files that I created (ranking, edit-poll and new-poll). If you look these .js files, you'll see how knockoutjs patterns should be used. If you never used 
any model-view-model framework, please take a look at http://learn.knockoutjs.com/ . Also, do not hesitate to look for me, I'll be glad to show you guys how to get started.
