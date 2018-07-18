# Using Direnv with Python

## Introduction to Direnv

Direnv is a powerful tool that lets you automate some of the setup of your
environment. Its slogan is "Unclutter your .profile" so it's pretty good at
helping you take your per-project configuration and localizing it to the project
you're working on. What does that mean exactly? Let's dig into that briefly.

Suppose you're working on a project that requires you to modify your path to
include a particular command or change an environment variable, say `API_KEY` to
a value for your app. A way to do that would be to add something like the
following to your `.profile` (some people add it to their `.bashrc`).

    PATH="$PATH:$HOME/path/to/commands/"
    export PATH
    export API_KEY="1234567890"

This way, your environment can access these variables. 

The value proposition for Direnv is that it lets you configure this on a
project-by-project basis. The [README](https://github.com/direnv/direnv) goes
into that a bit more but the gist is that in your project folder, you edit a
file called `.envrc` and add your variables do it. To replicate what we did
above with the `PATH` and key, you'd have the following `.envrc`:

    PATH_add $HOME/path/to/commands
    export API_KEY="1234567890"
    
    
The magic is that once you have Direnv set up, when you entire the directory, it
automatically changes your shell to include these variables.

## Setting up Direnv

To install Direnv, you'll want to follow the instructions for your platform. On
MacOS, it should be available via Homebrew. On Linux, it should be available via
`apt-get`. If you use Go and prefer to install it that way, you can even use `go
get -u github.com/direnv/direnv` to install it.

Once it's installed, you need to add the initialization hook to your shell's
configuration script. For Bash, that means adding this line:

    eval "$(direnv hook bash)"

to your `.bashrc`.

When that is set up, you can proceed to add `.envrc` files to your individual
projects. (You may need to run the command `direnv allow` to allow it to run
properly. You usually need to do this any time you change you `.envrc`.)

## Working with Python projects

Direnv has a lot of rich standard library that can help you with different
environments. To take a look, you can either use `direnv stdlib | less` to look
through them, or else take a look a look at them on [GitHub
here](https://github.com/direnv/direnv/blob/master/man/direnv-stdlib.1.md). 

One that I really like is the ability to automatically create and activate a
Python virtualenv for your project. In a nutshell, a virtualenv is a way to
install all of your Python dependencies into an environment that you can
activate and deactivate at will. You might be noticing a trend here that it's
really useful to keep your setup and configuration separate. The reason why is
that it would allow you to install one version of a package in one project while
being able to use a different version in another.

To use Direnv to help manage your virtualenv in a project, you want to add the
following line to your `.envrc` in the project directory:

    layout python
    
This does one of two things:

* If a folder doesn't exist in `$PWD/.direnv/python-$version`, it creates it
* If the folder above already exists (or it just created it), it activates your
  virtualenv

Once you've done that, you can navigate to the project directory and it should
create your virtualenv. When you do `which python`, it'll point to the one
within your project.

## Further refinements

One thing you might want to do is add some code to your `.bashrc` to enable
showing your Python virtualenv in your prompt. There's an issue with some
versions of Bash with modifying the prompt, so by default, [Direnv won't mess
with](https://github.com/direnv/direnv/issues/331#issuecomment-367015404) it.
You can add the behavior of changing your prompt using the [snippet
here](https://github.com/direnv/direnv/wiki/Python#restoring-the-ps1). At this
to your `.bashrc`:

    show_virtual_env() {
      if [ -n "$VIRTUAL_ENV" ]; then
        echo "($(basename $VIRTUAL_ENV))"
      fi
    }
    export -f show_virtual_env
    PS1='$(show_virtual_env)'$PS1
    
## Concluding remarks

That's sums up some ways you can get started with using Direnv as well as use it
to help you manage your Python projects more automatically.
