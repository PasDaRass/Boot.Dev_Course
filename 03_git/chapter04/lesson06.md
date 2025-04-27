There are several locations where Git can be configured. From more general to more specific, they are:
<ul>
  <li>
    
system: /etc/gitconfig, a file that configures Git for all users on the system
  </li>
  <li>
    
global: ~/.gitconfig, a file that configures Git for all projects of a user
  </li>
  <li>
    
local: .git/config, a file that configures Git for a specific project
  </li>
  <li>
    
worktree: .git/config.worktree, a file that configures Git for part of a project
  </li>
</ul>

<h4>Overriding</h4>
If you set a configuration in a more specific location, it will override the same configuration in a more general location. <br />
For example, if you set user.name in the local configuration, it will override the user.name set in the global configuration.
<br />
<img src="https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/e4S7M9u.png" />
