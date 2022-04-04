

## [fields](https://facebook.github.io/watchman/docs/cmd/query.html#available-fields)

## [watch-project](https://facebook.github.io/watchman/docs/cmd/watch-project.html)

```bash
$ watch-project ~/www/some/child/dir
{
  "version": "3.0.1",
  "watch": "/Users/wez/www",
  "relative_path": "some/child/dir"
}
```

## [query](https://facebook.github.io/watchman/docs/cmd/query.html)

```bash
$ watchman -j <<-EOT
["query", "/path/to/root", {
  "suffix": "php",
  "expression": ["allof",
    ["type", "f"],
    ["not", "empty"],
    ["ipcre", "test", "basename"]
  ],
  "fields": ["name"]
}]
EOT
{
    "version": "2.9",
    "clock": "c:80616:59",
    "is_fresh_instance": false,
    "files": [
        {
            "exists": true,
            "mode": 33188,
            "new": false,
            "name": "argv.c",
            "size": 1340,
        }
    ]
}
```
Expresions: 
*   ["exists"] 
*   ["allof", ...]
*   ["match", "foo*.c", "basename"],
*   ["allof",
        ["not", ["match", "*.c", "wholename"]],
        ["match", "*main*", "wholename"]
    ]
* ["type", "f"]

[relative_root](https://facebook.github.io/watchman/docs/file-query.html#relative-roots)

## [subscribe](https://facebook.github.io/watchman/docs/cmd/subscribe.html)
```bash
$ watchman -j --server-encoding=json -p <<-EOT
["subscribe", "/path/to/root", "mysubscriptionname", {
  "expression": ["allof",
    ["type", "f"],
    ["not", "empty"],
    ["suffix", "php"]
  ],
  "fields": ["name"]
}]
EOT
{
  "version":   "1.6",
  "subscribe": "mysubscriptionname"
}
{
  "version": "1.6",
  "clock": "c:1234:123",
  "files": ["one.php"],
  "root":  "/path/being/watched",
  "subscription": "mysubscriptionname"
}
```

### subscribe with clock (token)

Only include files that changed since the specified [clockspec](https://facebook.github.io/watchman/docs/cmd/clock.html).

Equivalent to to using the `query command` with the `since` generator.

```bash
["subscribe", "/path/to/root", "myname", {
  "since": "c:1234:123",
  "expression": ["not", "empty"],
  "fields": ["name"]
}]
```

### subscribe and check the lock if undergoing git operations.
 If the root appears to be a version control directory, subscription notifications will be **held until an outstanding version control operation is complete** (at the time of writing, this is based on the presence of either `.hg/wlock` or `.git/index.lock`).

 To **observe the creation of the control files at the start** of a version control operation. You may specify that you want this behavior by passing the `defer_vcs` flag to your subscription command invocation.
 ```bash
 $ watchman -j -p <<-EOT
["subscribe", "/path/to/root", "mysubscriptionname", {
  "expression": ["allof",
    ["type", "f"],
    ["not", "empty"],
    ["suffix", "php"]
  ],
  "defer_vcs": false,
  "fields": ["name"]
}]
EOT
 ```

 TODO: pasar el log file
 git-lock
 template de exclude files .watchman.json de ese
 como meto las exclusiones tambien en la query
 helpers de quer de commands... si hay relative path... si se esta monitorizando ya el root... etc. es
 creo que no hace falta comprobar que no se esta pero...
 el git-lock seria para lo de sincronizar ... pero no para el fsmonitor.
 y tendria que ser async...cccc o que haya uno solo ...


 Util run as root y rsync ... 
 mover el fg  classmethod 
 