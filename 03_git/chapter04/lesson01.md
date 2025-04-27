# Anatomy of the git config command
<ul>
  <li>
    
git config: The command to interact with your Git configuration.
  </li>
  <li>
    
--add: Flag stating you want to add a configuration.
  </li>
  <li>
    
--global: Flag stating you want this configuration to be stored globally in your ~/.gitconfig. <br />
The opposite is "local", which stores the configuration in the current repository only.
  </li>
  <li>
    
user: The section.
  </li>
  <li>
    
name / email: The key within the section. (preprended with dot notation for objects)
  </li>
  <li>
    
"ThePrimeagen": The value you want to set for the key.
  </li>
</ul>

Without the global flag, `git config` defaults to local <br />
Git has a command to view the contents of your config:

```
git config --list --local
```
You can also just view the contents of your local config file directly:
```
cat .git/config
```
