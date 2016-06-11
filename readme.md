StellarisSublime adds syntax highlighting and autocompletions to the stellaris script language.
Most autocompletes are grabbed from stellariswiki.com

To use, simply clone this repo into your sublime user folder, (should also work with the Packages folder).
If you are on windows you will most likely find this folder in %appdata%/Sublime Text 3/Packages

Then you open a .txt file, click View -> Syntax -> User -> Stellaris   or   View -> Syntax -> Stellaris depending on where you put the files.
Then you want to click Preferences -> Settings - More -> Syntax Specific (User)
A file named 'Stellaris.sublime-settings' should pop up, in that file write
(if you put in Packages/User/Stellaris)
{
	"color_scheme": "Packages/User/Stellaris/StellarisTheme.tmTheme",
	"extensions":
	[
		"txt"
	]
}
(if you put in Packages/Stellaris)
{
	"color_scheme": "Packages/Stellaris/StellarisTheme.tmTheme",
	"extensions":
	[
		"txt"
	]
}

and then save it to your Packages/User folder.
Due to the complexity of the ordinary syntax files it was easier to just make one from scratch.
To change the colors you want to edit the .tmTheme file, it contains innstructions on how to edit it.