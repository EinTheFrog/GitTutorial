# Git Cheat Sheet
  
## List of Basic Commands
Parts of the commands that are put in square brackets you need to change yourself. For example, instead of "[Commit description]" you put "New algorithm for customer detection". You should NOT use square brackets in real commands.

## Navigation Commands
`cd [directory name]` - go to directory (folder)  
`cd ..` - go one level up  
`ls` - show structure (files and folders) of the current directory  

### Status Commands  
`git status` - check the status of the project (current branch, changes)  
`git branch` - check branches of the project  
`git log --oneline` - show history of commits  

### Branch Commands
Branch names CANNOT have spaces. Use underscores instead. For example, branch can be called _new_feature_ but cannot be called _new feature_.  

`git checkout [branch_name]` - go to an existing branch  
`git checkout -b [branch_name]` - go to a new branch  
`git branch -d [branch_name] ` - delete branch  

### Commit Commands

`git add [file names]` - select changes to commit  
`git add *` - select all changes to commit  
`git commit -m "[Commit description]"` - make a commit  

### Cancel Commands
`git restore --staged [file names]` - unselect changes to commit  
`git restore --staged .` - unselect all changes to commit  
`git restore [file names]` - cancel all changes done to mentioned file names after the last commit  
`git restore .` - cancel all changes and roll back to the last commit (all changes done after last commit will be lost)  

### Remote Commands
Commands below are used to communicate with remote repository (GitHub)  

`git clone [repository ssh]` - clone project from GitHub to your computer  
`git push --set-upstream origin [branch_name]` - upload your commits to GitHub for the first time  
`git push origin` - upload your commits to GitHub  
`git pull origin` - download commits from GitHub to your computer

## Feature Development Flow
1) `git checkout -b [branch_name]`
2) Do some code
3) `git commit -m "[Describe what you did]"`
4) `git push --set-upstream origin [branch_name]`
5) Do some code
6) `git commit -m "Describe what you did"`
7) `git push origin`
8) Repeat steps 5-6-7 as long as you need
9) When you finish implementing your feature - go to GitHub and create Pull Request  


## After Pull Request
1) `git checkout master` - go to master branch
2) `git pull origin` - update master branch
3) `git checkout -b [branch_name]` - go to new a branch to develop next feature
