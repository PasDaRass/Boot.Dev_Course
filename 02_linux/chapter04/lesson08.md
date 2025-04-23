<p>
  pwd and realpath both reveal the absolute path of your current directory
</p>

<p>
  To add a directory to your PATH without overwriting all of the existing directories, use the export command and reference the existing PATH variable:

</p>

```
export PATH="$PATH:/path/to/new"

```

<em>
Restarting your shell will reset your env variables to default values
</em>
