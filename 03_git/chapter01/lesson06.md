Let's set your identity. Check if your user.name and user.email are already set:
```
git config --get user.name
```
```
git config --get user.email
```
If they aren't, set them. It is recommended using your GitHub username and email.
```
git config --add --global user.name "github_username_here"
```
```
git config --add --global user.email "email@example.com"
```
Finally, let's set a default branch (we'll talk more about configs and branches later) so that we're all on the same page. Run:
```
git config --global init.defaultBranch master
or
git config --global init.defaultBranch main

```
