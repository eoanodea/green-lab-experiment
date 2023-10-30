# Contributing to the Android Runner Framework

Thank you for your interest in using the Android Runner framework. Android Runner has been built up in iterative steps by bachelor's, master's, PhD students and professors. Our goal is to make performance and energy consumption research on Android devices more accessible and robust. The framework provides many tools and plugins to make this possible.

## Table of Contents
- [Requirements](#requirements)
- [Setting Up Environment and Dependencies](#setting-up-environment-and-dependencies)
    - [Linux](#linux)
        - [Ubuntu 22.04 (command-line only)](#ubuntu-2204-command-line-only)
        - [Ubuntu 18.04](#ubuntu-1804)
        - [Other](#other)
    - [macOS](#macos)
- [Before You Begin](#before-you-begin)
- [Environment](#environment)
- [Making Changes to Your Forked Repository](#making-changes-to-your-forked-repository)
    - [Commits](#commits)
    - [Plugins](#plugins)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Communication](#communication)
- [Debugging Tips](#debugging-tips)

## Requirements
- Python 3
- Linux or macOS

Current and former contributors have used Ubuntu 18.04 and Ubuntu 20.04 along with Python 3.6.9 and 3.7.4.

## Setting Up Environment and Dependencies
1. Click on the **Fork** icon in the top right hand corner once you're logged into Github.
2. Once it finishes loading, click on the green **Code** button. Copy `git clone git@github.com:[your_username]/android-runner.git` and then paste that into your terminal after navigating to the desired local development environment.
3. Type `cd android-runner` to enter the framework's main directory.  Now, add a remote tracker to the parent repository with `git remote add upstream https://github.com/S2-group/android-runner`.  This is useful in case any major changes occur to the parent directory that may affect your project.  `git remote -vv` should now show *origin* and *upstream*.
4. Create a virtual environment: `python3 -m venv /path/`.  This can be anywhere on your machine.  Activate it with `source /path/bin/activate`.
5. Install dependencies:
    1. Select your platform below:
        ### Linux
        #### Ubuntu 22.04 (command-line only)
        - Install JDK 11 `sudo apt install openjdk-11-jre`.
        - Download the`sdkmanager` from the latest "command line tools only" package available [here](https://developer.android.com/studio) and unzip the package to your `$HOME` directory.
        - Create a directory called `android-sdk` in your `$HOME` directory and move the unzipped `cmdline-tools` directory there.
        - In the directory `cmdline-tools` create a sub-directory called `latest`.
        - Move all the original contents from `cmdline-tools` into the newly created `latest` directory.
        - cd into `cmdline-tools/latest/bin` and run the following commands to install adb and monkeyrunner:
        ```bash
            ./sdkmanager "platform-tools"
            ./sdkmanager "build-tools;30.0.0"
        ```
        - Add the following to your `.bashrc` or `.zshrc` file:
        ```bash
            export PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$PATH
            export PATH=$HOME/android-sdk/platform-tools:$PATH
            export PATH=$HOME/android-sdk/tools/bin:$PATH
        ```
        - Reload your `.bashrc` or `.zshrc` settings by running `source ~/.bashrc` or `source ~/.zshrc`
        - To verify if everything works correctly run `adb --version`. This should return its version number and install location. To do the same for Monkey Runner run `monkeyrunner --version`. This should return a `Unrecognized argument: --version`. but no other errors.
        - Install lxml using `sudo apt install python3-lxml` (assuming python3 is being used).
        #### Ubuntu 18.04
        - Android Debug Bridge (`sudo apt install android-tools-adb`)
        - Android SDK Tools (`sudo apt install monkeyrunner`)
        - JDK 11 (`sudo apt install openjdk-11-jre`)
            - See [this](https://askubuntu.com/questions/740757/switch-between-multiple-java-versions) for switching between java versions
        - lxml (`sudo apt install python-lxml`)
        #### Other
        - Download Android Studio from [here](https://developer.android.com/studio#downloads).
        - Extract the archive, `cd` into its directory and install Android Studio by running `./bin/studio.sh`
        - During the setup wizard Android Studio will ask you where you want to install the Android SDK. By default it is in `/home/user/Android/Sdk`
        - The Android SDK, including ADB and Monkey Runner, is now installed on your system. To access the Android tools directly via your shell (preferable) add the following to your .bashrc/.zshrc:
            
            ```
            export ANDROID_HOME=$HOME/Android/Sdk
            export PATH=$PATH:$ANDROID_HOME/tools/bin
            export PATH=$PATH:$ANDROID_HOME/platform-tools
            ```
        - Reload your `.bashrc` or `.zshrc` settings by running `source ~/.bashrc` or `source ~/.zshrc`
        - Since MonkeyRunner requires JDK 8 (not JDK 9) we need to install JDK 8: `sudo apt install openjdk-8-jre`.
            - Once JDK 8 is installed we need to actually set it as default. See [here](https://askubuntu.com/questions/740757/switch-between-multiple-java-versions) how to do that.
        - To verify if everything works correctly run `adb --version`. This should return its version number and install location. To do the same for Monkey Runner run `monkeyrunner --version`. This should return a `Unrecognized argument: --version.` but no other errors.
        - Install lxml using `sudo apt install python-lxml`.
        ### macOS
        - Make sure you have <a href="https://brew.sh/">Homebrew</a> installed
        - `brew install --cask homebrew/cask-versions/adoptopenjdk8 android-sdk android-platform-tools`
        - `brew install libxml2`
        - Run `java -version`, if you are running a different version than 1.8/8:
        - `brew install jenv`
            - Run `/usr/libexec/java_home -V` to see the location of your Java environments
            - Copy the location of your AdoptOpenJDK8 environment
            - Run `jenv add <AdoptOpenJDK8_path>`
            - Run `jenv global 1.8`
            - Restart terminal and verify your Java version with `java -version`, it should output `openjdk version "1.8.0_265"`
        - Verify that monkeyrunner works with `monkeyrunner --version`, it should output unrecognized argument and no other errors
    2. Within Android Runner's main directory
        - `pip install -r requirements.txt`  
    3. For creating or editing unit tests to ensure pull request passes TravisCI
        - `pip install pytest mock`

**Note:** It is important that Monkeyrunner shares the same adb the experiment is using. Otherwise, there will be an adb restart and output may be tainted by the notification.  You can specify the path to adb and/or Monkeyrunner in the experiment configuration file.

**Note 2:** The Batterystats, Trepn and Monsoon plugins have additional dependencies.  Refer to the plugin [READMEs](https://github.com/S2-group/android-runner/tree/master/AndroidRunner/Plugins) for more information.

## Before You Begin
It's important for us to make sure that any updates to the framework add value and that the updates adhere to the original goals of the framework.  Before spending a lot of time making substantial changes, please raise an `issue` on Github so we're made aware of the changes you'd like to implement.  We'll provide feedback to inform you whether we think it's viable.

## Environment
- Your forked repository will come with one branch, called `master`.
- Create additional branches for experiments and/or development with `git branch branch_name`.
- To update your forked repo with parent repo, `git checkout master` and type `git fetch upstream` followed by `git rebase upstream/master` so your local work is put on top of any changes made to the parent repo. 
    - Note, this may mean you'll have to stash whatever you were working on.  In this case, `git stash save "message"` before `git checkout master`.
- Once `master` has been updated, checkout the other branches to update with `git merge master`.
- Then, `git stash pop stash@{#}` to continue working on changes.

## Making Changes to Your Forked Repository
### Commits
Any commits should contain logically similar changes.  Commit messages (`git commit -m "[text]"`) should be informative but also concise.  Good commits make changes easier to review later.  To limit the number of commits, use `git rebase` to squash the commits down to a more reasonable number.

### Plugins
If you're editing an existing plugin or adding a new one, there's an automated test called **plugintest** in `examples` that will ensure the plugin adheres to the requirements of the framework.  To execute it, type: `python3 android-runner android-runner/examples/plugintest/config.json`.

## Submitting a Pull Request
Pull requests should be made from secondary branches (ie, not `master`).  Also make sure the branch is not behind in commits compared to master.  Any changes that need to be made while a pull request is still pending review should be made on a third branch to prevent polluting the pull request with other changes if they're not relevant.  

When a pull request is submitted, a number of automated tests are performed on the **TravisCI** platform and with **SonarCloud**.  TravisCI runs coverage analysis to confirm that all major components in the framework have associated unit tests in tests/unit/.  In other words, **you'll need to add unit tests for new methods, plugins or other functionality improvements**.  For an expedited review process, run **pytest** in your local environment before submitting a pull request.  You can execute these tests in the android-runner directory with: `py.test [options] tests/unit`. It's also possible to run py.test with a specific module in tests/unit/.   Don't forget to **remove debugging statements** before submitting.

To execute the test suite make sure you have installed `coverage`, `pytest` and `mock` either globally or in your virtual environment. You can then run (assuming Python3):
```sh
python -m coverage run -m py.test tests/unit/
```
To then check the code coverage and report missing lines run:
```sh
python -m coverage report -m
```
## Communication
The best way to communicate with the Android Runner team is through:
- Opening a GitHub issue
- Slack
- Canvas

## Debugging Tips
[pdb](https://docs.python.org/3/library/pdb.html) is a good library to import if you experience issues that may be hard to resolve with print statements.  