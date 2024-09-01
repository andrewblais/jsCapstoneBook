```bash
# Initialize a new Git repository in the current directory:
git init

# Add all files to the staging area, including respecting the .gitignore file:
git add --all

# Commit the staged files with a descriptive message:
git commit -m "first commit"

# Rename the current branch to `main` (common default branch name):
git branch -M main

# Add a remote repository with the name `origin` pointing to the specified GitHub URL:
git remote add origin https://github.com/andrewblais/jsCapstoneBook.git

# Push the `main` branch to the `origin` remote, and set `origin/main` as the upstream branch:
git push -u origin main
```
