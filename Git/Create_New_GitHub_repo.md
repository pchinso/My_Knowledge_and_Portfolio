
# New empty repositorie

- Create remote

Go to <https://github.com>, log in and create a new account then press the **"New_Repository"**

<https://github.com/pchinso/New_Repository.git>

- Create locally on the command line,

```sh
echo "# New_Repository" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pchinso/xxxx.git
git push -u origin main
```

# Some cheatsheet

## Undo last commit

`git reset` command with the `--soft` option to reset the HEAD pointer to the previous commit. This command will not delete the commit from your repository history, but it will undo the changes made in that commit.

You can also use the `git reset --hard` option if you want to delete the commit from your history. Be aware, however, that this will also delete any changes made in the commit, so it should be used with caution.

```git
git reset --soft
git reset --hard
```
