# Git

## The Ultimate Resource
[Pro Git](https://git-scm.com/book/en/v2)

If you want to dive deep into Git, use **the Ultimate Resource**.

This note provides an introduction to Git.

---

## What is `git`?

Git is a version control system that keeps track of snapshots..
We call all the files that git keeps track of, a **repository**.

We need to explicitly tell git which files to add to the **repository**.

Again, git keeps track of **snapshots**. Anytime we make a change, git keeps track of these changes.

Every change made to the repository needs to be "**owned**" by a person. We first need to set up our identities so that git can help keep track of them.
## Identity
` config --global gituser.name "<username>"`
`git config --global user.email "<email address>"`

Git only needs two pieces of information to identify the ones making changes, the username and the user's email address. We use the commands above to set it for our accounts.

The next step is to create a repository for a directory/folder.

## Creating a repository
`git init`

This creates a **git repository** in the current folder.

## Checking Status
`git status`

You can see all changes that are **not yet committed** to the snapshot using this command.

## All previous commits
`git log`

We can see all of the previous snapshots using git log.
## Adding files to the stage
`git add <path>`

When we're finally ready to add files and their changes to the git repository, we use this.

If we want to add **all** changes to the git repository, we can do this:

```bash
git add .
```
## Commit
`git commit -m "<commit message>"`

Commits take all the staged changes and create a new **snapshot**.

---

## Github

We can store our repositories in the cloud.

For this class, we'll create a public repository for all of our programming source files.

### Create a Github Account

Go to **https://github.com** and create a new account if you don't have one.
Your username is the name you'll be referred to as on Github. 

### Create a new repository

Click the green  **New** button. 
Give the repository a descriptive name.
We're going to make the repository profile to the public 

### Create a key to link your local repository to your remote repository

1. Click on your profile picture
2. Find the **Settings** option and click it .
3. In the left sdebar, find **Developer Options** and click it.
4. In the left sidebar, find "**Personal Access Tokens**".
   1. Click **Fine Grained Tokens**. 