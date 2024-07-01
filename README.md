# Debugging Python running in a Docker Container running in WSL

.. in a [Multi Root Workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces).

This can be used to

- easily work with multiple different repositories at the same time, or
- make VS Code think that subfolders of a single (monolithic) repository
  are in fact individual projects;
  allowing them to have individual `.vscode`-configuration folders.

Is this a good idea?

- It scopes projects, which is nice,
  since we can defer config to the individual projects.
- It may lead to a lot of copy-pasted config,
  but hopefully they'll be fairly identical,
  (since they can use relative references to their folders,)
  and if we had this in different repositories,
  we'd have copy-pasted config anyways;
  but we'd have to update it in every repository.

## Getting Started

1. Open VS Code
1. Choose "File -> Open Workspace from File"
1. Choose the `myproject.code-workspace`

This will..

- Open a new workspace in VS Code
- The workspace will have 4 "folders"
- The `root` folder is added, so we have access to manipulate the
  root of the project.
  This also automagically enables our git source control,
  and tracks changes in any folders.

Folders are defined in the `myproject.code-workspace`-file,
each of the folders have been given a shorter name,
along with their path.

## Projects

> NB: When you're debugging any of the projects, you _must_
> select the relevant debugging configuration.
> The project-name will be appended.

### super-long

- A python app with two launch configurations.
- Its `README.md` explains in great detail how it's configured.

It's a basic project which demos
"Debugging Python running in a Docker Container running in WSL."

### another-long

- Similar to super-long, but the launch configurations have their order reversed;
  notice how this changes the debug configuration menu in VS Code.

### the-third-even-longer-wow-this-is-a-name-folder-project-name-3

- Similar to the others, it just has a really long name and no alias.
- Only has one launch configuration.

Notice:

- How the launch-configuration dropdown shows it all.
- How its nice to give folders short-names.

### team-red (here be dragons)

A client/server workspace which uses a common root.

- They can both include the same `global-version-file-example`-file,
  in their built containers.
- This is not a good practice; use a "library, module, etc." for shared things.
- This is how things get complicated real _fast_.

Notice:

- How the `launch.json` and `tasks.json` are bloated,
  and specifically have to reference the `/client` and `/server`-folders,
  whereas the other projects can simply use `{workspaceFolder}`.
- Sending "the entire root" as context for docker is often overkill,
  unless its needed.
  - If it's needed consider if you can restructure your code;
    shared code should be a module!
- How we need to use `team-red` as our workspace root,
  otherwise we can't reference it as the context for Docker.

## The .code-workspace File

The `.code-workspace`-file has a list of folders that it opens as individual workspaces.
Notice how some of these is in the `root`,
and some of these are in the `team-blue` folder.

The `.code-workspace`-file could also hold configuration
for the individual projects, and compound configurations.

Imagine that we're working on a "client" and "server,"
and we want to run both.

However, in our case, all the folders hold separate, individual projects,
and we have no interest in "debugging multiple at the same time."
So we keep the configurations separated in their respective `.vscode`-folders.
