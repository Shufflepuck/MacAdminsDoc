# Basic Configuration

This tutorial goes over how to add some basic configuration to your Puppetserver for managing your macs.

Originally Posted at: [www.mholt.tech/blog/2015/12/07/basic-puppet-configuration/](http://www.mholt.tech/blog/2015/12/07/basic-puppet-configuration/)

## Configuration Overview

So this is the second post about Puppet.  I'm going to go through a brief overview  deploying some configuration to your computer using Puppet.

If you don't already have Puppetserver running, please go back to my previous post [Here](/blog/2015/12/04/getting-started-with-puppet/) to get up and running with Puppet. If you aren't following from my previous post some of this will be different depending on your Environment but I will be continuing with the setup on the Docker Image that I've created. We're going to start with some basic configuration so you can understand how the basics work.  Next year I'll be providing a repository with more detailed configuration options that won't necessarily be covered here.

There are multiple parts to applying configurations to your computer.  Inside of the Core Repo folder that you cloned previously you'll see a folder named **Hiera**.

First off, you have Hiera.  These files are used to apply configuration to your machine.

  - ``machine/c02n5heug3qj.yaml`` (You may have renamed this in the previous post)
  - ``role/test.yaml``
  - ``common.yaml``

The files inside of ``machine`` are optional and used if you want to apply a special configuration option to a specific machine. These files should be named after the serial number of the machine, always in lower case.

The files in ``role`` are used to create a configuration file that is applied to multiple machines and is defined as a custom fact as done in the previous post.

The final file, ``common.yaml `` is a master configuration that is applied to all machines.

When defining specific configuration data, you can have the same variable in multiple files and the one that is seen first in the order of files above is what is applied.

Lets start with opening ``common.yaml``.  In this file you'll see a few lines of code.  Classes are configuration functions defined in manifests either from Modules that are included in Puppetfile, or additional custom manifests defined in site/(profiles or roles)/manifests.

The first line you see under classes is "puppet_run".  This is calling a function inside of a Puppet Module by [Graham Gilbert](http://www.grahamgilbert.com) called [Puppet Run](https://github.com/grahamgilbert/puppet-puppet_run).  This module configures puppet agent on the machine and configures puppet to automatically run every 30 minutes along with a random delay of anywhere between 0 and 20 minutes to prevent all of your machines from checking in at the same time.

The next line you'll see under Classes is ``roles::default``.  This calls a custom configuration file inside of ``site/roles/manifests/default.pp`` and simply run an echo command outputting "Default Role" when running ``puppet agent -t``

The final line is a variable, ``puppet_run::server_name``.  This variable is what tells the Puppet Run module what your puppet servers name is.  When it comes to variables you can override them on a per role or per machine basis by also including the variable along with the corresponding class inside of the respective role or machine yaml file.

## Lets add some custom configuration

Your needs and environment are going to vary from mine but i'm going to go over some basic configuration options using [ManagedMac](https://github.com/dayglojesus/managedmac) by [dayglojesus](https://github.com/dayglojesus).

### Add some text to Login Window.

We're going to start off with configuring puppet to display a message on the login window.

We'll start off with adding a message that will be applied to everyone.  To do this, lets open up common.yaml and add these lines.

Under ``classes`` add:
````
  - managedmac::loginwindow
````

now at the bottom of the file lets add the variable to define the message.

````
managedmac::loginwindow::loginwindow_text: "This is a global message"

````

Once this is done go ahead and save, commit, and push the file to your git repository.  Once this is done you need to log into your Docker server and run

````
docker exec -it puppetserver r10k deploy environment -pv
````

Once your puppetserver has been updated lets manually run Puppet on your test machine

````
puppet agent -t
````

Now go ahead and log out and you should see a message on the login window saying "This is a global message".

Now lets go ahead and define a machine specific message on the login window.

Create a file inside of hiera/machine/<serial-number>.yaml (Ensure that you use all lower case).  Inside of this file go ahead and populate with:

````
---
classes:
  - managedmac::loginwindow
managedmac::loginwindow::loginwindow_text: "This is a machine message"

````

Go ahead and commit and push this to your git repository, then once again run this on the server:

````
docker exec -it puppetserver r10k deploy environment -pv
````

Afterwards, run on your machine

````
puppet agent -t
````

Log out and you will now see your login window saying "This is a machine message" instead of "This is a global message".

There are a lot more configuration options for ManagedMac and they can all be found [Here](http://dayglojesus.github.io/managedmac/).


## Hide Puppet User

Lets go ahead and do one more thing before we wrap up this session.  We're going to hide the annoying "Puppet" user that shows up on the login window.

Go ahead and navigate to ``site/profiles/manifests`` and create a file called ``hidepuppetuser.pp``.

Inside of this file, insert

````
class profiles::hidepuppetuser {
  exec {
    'Hide Puppet User':
    command => "/usr/bin/defaults write /Library/Preferences/com.apple.loginwindow HiddenUsersList -array-add puppet",
  }
}
````

Now go ahead and save this file and close it.  The next step is to tell the machines to go ahead and run this manifest.  We want to apply this to ALL machines, so go ahead and edit ``hiera/common.yaml`` and under classes insert

````
  - profiles::hidepuppetuser

````

Save this file, then commit and push both files to your git repository.  After that, run r10k to update your Puppetserver and then run puppet on your test machine.  After this is done, you should no longer see the user "Puppet" when you are at the login window.

This concludes this blog post and gives you an idea of how to use Puppet to configure your machines.  As I mentioned previously, i'll be posting a number of my configurations up on Github when I get back from Christmas Vacation.

**UPDATE**: An Example Core Repository can be found [**HERE**](https://github.com/MichaelHoltTech/example-core_repo)
