# Debugging Python running in a Docker Container running in WSL

Example project, showing how to debug Python,
running in a Docker Container using VSCode.

## Prerequisites

- VSCode "Python" plugin
- Docker

## Commands

```shell
make build  # build the container
make debug  # run the container with the debugpy command in the background
make run    # run the container in the background
make logs   # print the logs from the container to stdout
```

## Debugging Manually with Docker

Attaching the debugger (linux):

1. In a terminal, in the workspace folder, run `make debug` .
   - use `make logs` to see that the container is waiting for the debugger
     to attach.
1. In VSCode, navigate to "Run and Debug" in the leftside menu
   (`ctrl + shift + D`.)
1. In the top-left, in the dropdown with configurations,
   choose "Python Remote Docker,"
1. Start debugging by clicking the green "play"-icon (shortcut: `F5`)

At this point you should see in the logs that the debugger has attached,
and VSCode should pause at different break points in the code.

## Debugging Automagically with Docker

1. In VSCode, navigate to "Run and Debug" in the leftside menu
   (`ctrl + shift + D`.)
1. In the top-left, in the dropdown with configurations,
   choose "Docker: Python - Flask."
1. Start debugging by clicking the green "play"-icon (shortcut: `F5`.)

VS Code should build and launch a container,
and attach the debugger.

It also opens the app in the browser.

> NB: It does this by invoking the `Docker: Python - Flask`-launch configuration,
> from the `./vscode/launch.json`,
> which in turn runs the `docker-run: debug`-task, from `./vscode/tasks.json`,
> (which also depends on the `docker-build`-task.)
>
> You should check out these files, and play around with their configuration.

We've enabled "hot-reload," by adding the configurations listed on,
<https://code.visualstudio.com/docs/containers/debug-python#_for-flask-apps>,
and also added the `--debug`-flag, so Flask listens for changes.

### Generating the files

The base `launch.json` and `tasks.json` were generated,
using the `Docker: Initialize for Docker debugging`-command in VS Code.
This is available after installing the "Docker"-extension.

We chose "Initialize" and not `Docker: Add Docker Files to Workspace`,
because we already had a Dockerfile.

The "debug-common"- and "debug-python"-links below,
were used to customize the files, and forward ports accordingly.

By default it forwards ports on the container IP,
(some random ip on the container network,)
and localhost (inside the container!)

In the `tasks.json` we've set a `containerPort` and `hostPort`,
so the ports are forwarded to `localhost`.

> NB: We could also do some regex magic,
> from the log, and use the dynamically selected IP,
> this is left as an exercise to the reader, for now.
>
> See:
> <https://code.visualstudio.com/docs/containers/debug-python#_automatically-launching-the-browser-to-the-entry-page-of-the-application>)
>
> But instead of reading the port, you should read out the IP.

## More Resources

Configuring Debugging in general:
<https://code.visualstudio.com/docs/containers/debug-common>

Debug Python within a container:
<https://code.visualstudio.com/docs/containers/debug-python>
