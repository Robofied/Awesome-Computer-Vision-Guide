#!/bin/sh
# Run the file inside terminal 
# $ bash automate.sh "Commit message"

echo "Git Automation Starts ....."

message=$1 # First parameter will be the commit message
currentBranch=$(git symbolic-ref --short -q HEAD) # Getting the current branch

if [ ! -z "$1" ] # checking if the commit message is present. If not then aborting.
then
  git status
  read -p "Do you want to push the changes ? [Y/N] : " user_var
  
  if [[ "$user_var" == "y" || "$user_var" == "Y" || "$user_var" == "yes" ]] 
  then 
    git add .
    git commit -m "$message"
    git push origin $currentBranch
  else
    echo "Pushing changes is incomplete"
  fi 

else
  echo "Commit message is not provided"
fi               # closes the if statement