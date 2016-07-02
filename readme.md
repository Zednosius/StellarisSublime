# StellarisSublime 
Adds syntax highlighting and auto-completions to the stellaris script language.  
Most autocompletes are grabbed from stellariswiki.com

To use, simply clone this repo into your sublime Packages folder.  
If you are on windows you will most likely find this folder in %appdata%/Sublime Text 3/Packages
The final path should look like /Sublime Text 3/Packages/Stellaris/<files>

### Associate with .txt files
Then you open a .txt file, click  `View -> Syntax -> Stellaris` to have sublime use that syntax file when opening text files.

### Associate theme with Stellaris Syntax
Then you want to click `Preferences -> Settings - More -> Syntax Specific (User)`  
A file named 'Stellaris.sublime-settings' should pop up, in that file write  
(if you put files in Packages/Stellaris)

```
{
	"color_scheme": "Packages/Stellaris/StellarisTheme.tmTheme",
	"extensions":
	[
		"txt"
	]
}
```
and then save it to your Packages/User folder.


Due to the complexity of the ordinary syntax files it was easier to just make one from scratch, this also means the usual themes won't work with it.
I have however made a custom theme file, which should be easy to edit to your liking.