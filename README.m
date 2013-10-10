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


As for the project:

I've done a bunch of stuff, but there's still a good bit to do: 

Voting does not happen yet, both the client and server sides need to be done.
Rankings do not have passwords yet.
The algorithm to craete the ranking of a poll is pretty stupid right now.
I haven't written the base test class nor any tests, so just skip tests for now.

You guys can do whatever u want.

TIPS ON GIT:

Lets NOT USE GIT MERGE.

The flow should be the following:

At first time, you guys will clone the repo. That's fine.

To write code, CREATE A NEW FU**** BRANCH.

It's:
- 'git branch' to see the existing branches,
- 'git checkout -b BRANCH_NAME' to create a new branch and go to it (it will create from the branch where you are),
- 'git checkout BRANCH_NAME' to go to another branch,

When you are finished writing code:
- 'git add .' will add everything you wrote.
- 'git commit -m "WRITE A DESCRIPTIVE MESSAGE"' will create your commit
- 'git checkout master' : go back to master
- 'git pull' : update master
- 'git checkout YOUR_BRANCH' : go back to your branch
- 'git rebase master' : this will do the merge 4 you. It's much better than using git merge, but it may still fail. If it does, then you gotta do the manual merge.
- 'git checkout master' go to master
- 'git merge YOUR_BRANCH'
- 'git push origin master' pushes changes to github


Look 4 me if u need help.

Tks a lot for the attention.
