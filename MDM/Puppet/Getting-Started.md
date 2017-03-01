# Getting Started

This tutorial goes over how to get started with running Puppet in a Docker Container to manage your mac configuration.

Originally Posted at: [www.mholt.tech/blog/2015/12/04/getting-started-with-puppet/](http://www.mholt.tech/blog/2015/12/04/getting-started-with-puppet/)

## Installing Docker

I'm going to assume you already have a working Ubuntu 14.04 Server.  If not, I Highly recommend using Linode, which is what we use to run our Management Platform.  You can sign up [Here](https://www.linode.com/?r=eb7892d4b2b5528c799c9bab969491ae8b02970a).

Our first job after SSH'ing into the server is to get Docker installed.  This is a very easy process.  

First lets makes sure we have `` wget `` installed:

````
which wget
````


If nothing is returned, we need to install `` wget ``:

````
sudo apt-get update
sudo apt-get install wget
````

And now we can install Docker.

````
wget -qO- https://get.docker.com/ | sh
````

Enter your password when asked and then you're done.

If you aren't running as root (which isn't secure anyways so I hope you aren't), you can give a user access to Docker without having to grant sudo and preface all docker commands with sudo.  This can be done by running

````
sudo usermod -aG docker <username>
````

## Clone the Core Repo
Now before we continue with docker we need to clone the base configuration that our Puppetserver will be using.  I'm going to go with the assumption that you are familiar with git.  If this is you're first time there are a lot of tutorials on the internet, personally I like to use a GUI and recommend [SourceTree](https://www.sourcetreeapp.com/).

This is also going to be based on using Bitbucket for storing your configurations privately.  Bitbucket gives you unlimited *PRIVATE* repositories for free which I highly recommend doing to keep your configuration data private.  This is also compatible with GitHub as well.  You can get a BitBucket account [here](https://bitbucket.org/).

Here's how to get started with your own copy of the Core Repository:

1. To start off, go to Bitbucket's website and log in.
2. Go to Repositories -> Import Repository
3. For **URL**, enter: https://github.com/MichaelHoltTech/puppet-core_repo.git
4. For **Name**, you may keep the name of the imported repository or change this to anything you want.
5. For **Access Level**, make sure to check "This is a private repository"
6. Click **Import Repository** to import the base repository into your Bitbucket account.  It'll take a moment for the code to import and then you can continue.

## Start setting up Puppetserver

Now we're ready to go back to Docker and start setting up Puppetserver.  This is a very simple process.

We'll start off with creating what is called a Volume Container.  This will store the SSL Certificates used by Puppet so that the container can be updated as needed without worrying about losing some important configuration.

On your Ubuntu server, start by running this command. *Note: If you are not logged in with root then preface all commands from here on out with sudo*

````
docker pull busybox
docker run -d --name data_puppet \
  -v /root/.ssh \
  -v /var/lib/puppet/ssl \
  busybox
````

Now we have to create a file in order for the Puppetserver to know how to get your Core Repository.  If you skip this step you'll run into some issues when we get to restarting the container.  I prefer nano, but you use whatever editor you prefer on the Linux Server.

To begin, lets create some directories and grant all users inside of the Docker user group access.

````
sudo mkdir -p /usr/local/docker/puppetserver
sudo chgrp -R docker /usr/local/docker
sudo chmod -R 770 /usr/local/docker
cd /usr/local/docker/puppetserver
nano custom.yaml
````

Inside of custom.yaml insert the following contents, replacing the repo url in single quotes with repo's SSH URL found by clicking: ... -> Clone -> Change HTTPS to SSH.

````
---
repo_url: 'git@github.com:MichaelHoltTech/puppet-core_repo.git'
````

Now lets go ahead and close and save this file

Now that we have that out of the way we can get started with the Puppetserver.  Make sure you replace `` puppet.example.com `` with the url/hostname you intend to use for your puppet server.

````
docker pull michaelholttech/puppetserver
docker run -d --name=puppetserver \
  --volumes-from data_puppet \
  -v /root/.ssh \
  -v /var/lib/puppet/ssl \
  -v /usr/local/docker/puppetserver/custom.yaml:/root/bootstrap/hiera/data/custom.yaml \
  -e PUPPETSERVER_JAVA_ARGS="-Xms384m -Xmx384m -XX:MaxPermSize=256m" \
  -p 8140:8140 \
  -h puppet.example.com \
  --restart="always" \
  michaelholttech/puppetserver
````

After you have run those commands we need to monitor the logs for some important information that will be provided.  This can be done by running:

````
docker logs -f puppetserver
````

Once the initial scripts have run you'll see Public Key displayed in the logs.  You need to take this and enter it as a Deployment Key for your Repository.  This can be done by browsing to your repository on the Bitbucket Website, and then going to Setttings -> Deployment Keys -> Add Key.  Copy/Paste the Publickey starting with `` ssh-rsa `` and ending with `` R10K Deployment Key ``

Now that we've gotten that done we're ready to let Puppet finish bootstraping itself.  This can be done by copy/pasting the commands after the Publickey in the  logs that were looking at in the last step.  You can also run:

````
docker stop puppetserver
docker start puppetserver
````

Now if you watch the logs again you can see puppet preparing itself

````
docker logs -f puppetserver
````

This will take several minutes to complete.  When it is done you will see a line saying `` [p.s.m.master-service] Puppet Server has successfully started and is now ready to handle requests ``

Now that your puppetserver is running there's only one last command to run.  This command is only needed if there isn't already data existing inside of `` data_puppet ``.  This command is also set up to automatically run ever 30 minutes inside of the container.

````
docker exec -it puppetserver puppet agent -t
````

## Set up you're first client!

Whew we're almost there.  Not much longer until you will have your first client checking into your brand new Puppetserver.  

Let's start with a fresh Mac OS environment, be it a VM or spare computer.  We're going to have to start off by installing two packages on the machine... Puppet & Facter.

Puppet v3.8.4 can be downloaded [**HERE**](https://downloads.puppetlabs.com/mac/puppet-3.8.4.dmg).

Facter v2.4.4 can be downloaded [**HERE**](https://downloads.puppetlabs.com/mac/facter-2.4.4.dmg).

Once downloaded go ahead and install these onto your test machine.

At this point all that's left is to get your machine configured.  This is extremly simple and can be done with running one command in terminal, replacing `` puppet.example.com `` with your puppetserver's URL.  *If you don't have a DNS record for it, make sure you add a manual entry inside of `` /etc/hosts `` on your test machine!*

````
sudo puppet agent -t --certname $(ioreg -l | awk '/IOPlatformSerialNumber/ { split($0, line, "\""); printf("%s\n", line[4]); }' | tr '[:upper:]' '[:lower:]') --waitforcert 20 --server puppet.example.com
````

You now have your first machine up and running on Puppet! Congratulations!

There's plenty of information online if you want to begin playing with some configuration settings inside of the Core Repository.  

We'll go over this more in a future post, but to configure a role we need to create a fact on the local machine.  This can be done by running:

````
sudo mkdir -p /etc/facter/facts.d
sudo nano /etc/facter/facts.d/computer_role.yaml
````

Paste the following inside of `` computer_role.yaml ``

````
---
computer_role: "test"
````

Since the machine is now configured with puppet, you can trigger puppet by running a much simpler command:

````
sudo puppet agent -t
````

If you have added the computer_role fact, you should get an output similar to the following when you run `` puppet agent -t ``:

````
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Loading facts
Info: Caching catalog for c02n5heug3qj
Info: Applying configuration version '1449305286'
Notice: Test Role
Notice: /Stage[main]/Roles::Test/Notify[Test Role]/message: defined 'message' as 'Test Role'
Notice: Default Role
Notice: /Stage[main]/Roles::Default/Notify[Default Role]/message: defined 'message' as 'Default Role'
Notice: Common Profile
Notice: /Stage[main]/Profiles::Common/Notify[Common Profile]/message: defined 'message' as 'Common Profile'
Notice: Test Profile
Notice: /Stage[main]/Profiles::Test/Notify[Test Profile]/message: defined 'message' as 'Test Profile'
Notice: Finished catalog run in 13.84 seconds
````

## Additional Notes

Whenever you make a change to your Core Repo, you also need to manually tell your Puppetserver to pull in the changes.  This can be done by running this on the server:

````
docker exec -it puppetserver r10k deploy environment -pv
````

Yay! We've made it to the end and we now have a functional Puppetserver! If you've made it this far give yourself a pat on the back, it took me much longer to get up and running with Puppet when I first started.  

Here's a few quick notes:

1. This is a new Docker image and could have some bugs and issues.  I'm relying on the community to help identify these issues.
2. I'm not an expert at this, I just started using puppet a few months ago myself.  If you see areas that could be improved feel free to submit a pull request.
    1. The Puppetserver code can be found [**here**](https://github.com/MichaelHoltTech/puppetserver).
    2. The Core Repo code can be found [**here**](https://github.com/MichaelHoltTech/puppet-core_repo/).
    3. An Example Repository with more code can be found [**here**](https://github.com/MichaelHoltTech/example-core_repo).
    4. The Base Image code can be found [**here**](https://github.com/MichaelHoltTech/baseimage).  It is based off of work done by phusion, located [**here**](https://github.com/phusion/baseimage-docker).
3. I'm currently not running this Image in Production.  I plan on moving over to it after the Christmas Holidays as I continue to document our Management Platform.

Stay Tuned for the next post! No promises but i'll see if I can at least get one more post up documenting how to begin programming some configuration options.  If I don't get to it, I'll definitely have time in January! (I'll do my best not to keep you waiting 2 months this time)
