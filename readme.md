
# Disclaimer
First of, I suck at writing these kinds of things, so hopefully it all makes sense.

This tool is provided 'as-is'. While it has been tested to work there is no guarantee that will be true in the future, or that nothing may go wrong. **Always back up your original file before modifying**. This tool has been tested against a save from **Build 41**. While it may work with newer version of the game, there are not guarantees.

* **This mod is not made to be compatible with mods that add their own configuration items to the game's sandbox options screen.**
* **Back up your map_sand.bin file before applying one created by this tool. There is no guanratee that it won't break your save.**

# Requirements
* Python 3.9.16 or later
* A map_sand.bin file from Project Zomboid Build 41

# Known Supported Versions
* Project Zomboid Build 41 (41.78.16)

# PZSandboxOptionsEditor

This command line tool allows players of Project Zomboid to modify their save's sandbox settings (map_sand.bin) after they have started their game without the need to create a new save from scratch and copy the new files over.

# Usage

First, make sure you have Python 3.9.16 or later installed.

Next, you'll need the tools files, you can get them by either downloading the source from github, or by cloning the repository locally. If you downloaded them, extract them somewhere you can find them.

Once you have the files, you'll need tp open your favourite command line interface, for windows, you can press WindowsKey + R and enter "cmd" (without quotes), and hit enter.

Next, make sure the command line is poiting towards where you saved the script files, let's say we downloaded and extracted them to `C:\PZEditor\`. In your command line interface, enter the following: `cd C:\PZEditor\` (**note**: if the drive which you saved the files to differs from your OS drive, you may need to use the `/D` switch in the command, ie. `cd /D C:\PZEditor\`) and press enter, and make sure the beginning of the line matches the directory you entered.

Now that you're command line is ready, you'll need to find the map_sand.bin file you want to modify, Zomboid saves your game by default to `%userprofile%\Zomboid\Saves` on Windows (you can type this into the address bar in explorer, or in the run dialog (how we opened the command line)). In the `Sandbox` folder you'll see your save files. It's recommended you give them a proper name in-game so you can tell which is which, this can be done by selecting "Load" from the main menu. Once you find it, copy it to somewhere easy to access - this is the file we'll be using to make our edits.

Once you have copied it somewhere, it's time to make it easily modifiable. In your command line interface, you can enter the following to have the tool dump the contents of the file into a json file for easy editing. To do that we can run the following command:
`python main.py --dump --file C:\Path\To\map_sand.bin` making sure to put the correct path. This will create an `output` directory in the same location as the python files, and inside it will be `map_sand.json` - this is the file we'll be editing.

Open `map_sand.json` in your favourite text editor, and make your edits. **The values here will have many potential values and some will also have upper and lower limits, there are far too many to list the limits here, so you may have to resort to trail and error**. See [this page](settings.md) for a list of settings found within map_sand.bin. Make sure you keep the data types the same, ie. an integer (whole number) remains and integer, a float (decimal number) remains a float, etc. Once you've completed your edits, it's time to build it so the game can use it.

To make the file usable by the game we need to run another command with the tool again:
`python main.py --save --file ./output/map_sand.json` this will now create a `map_sand.bin` file inside the `output` directory. You may change the name of the file if you wish by adding `--output some_name.bin` to the command.

**Now is the time to back up your existing `map_sand.bin` file if you have not done so already.**

Once the process is complete, copy the `map_sand.bin` file from the `output` directory into your save directory that we found earlier. Note that some settings may take some in-game time to take effect and/or be noticable, and options that modify spawns may not take effect if an area has already been visited, and some changes may never take effect at all.

# Past/Future game versions
As mentioned above, while this tool may be able to create files for older or newer versions of the game, there is no guarantee that it can (unles the version is specified in the "Known Supported Versions" section) If you wish to create files for older or newer game versions, please run `python main.py --help` and look into the `--checkversion`, `--worldversion`, and `--sandboxversion` switches.

