# Projet_Data_Innovant-
Open data project related to low mobilities in Grenoble city area 
Problems of adding files : 

- error related to ' .git/index.lock ' something like that created =>  rm -f .git/index.lock in the terminal (not needed git in front of )
- error type 'zsh not found' after 'add .' or 'add file' command , means you need to push your work , so ' git push '
-If you want to modify this README file , you need to save changes before commit , otherwise changes won't be take into consideration. 


- Creating new branch : 'git branch -c branch_named' 
- Deleting branch : you need to be on an other branch then : 'git branch -d branch_named' 

- ISSUE : When someone has edited file between the moment you pulled and the moment you changed something => save changes 

('git add .' and 'git commit -m'message' ') then go to local main branch, pull it then do : 'git config pull.rebase false' (fusion)

