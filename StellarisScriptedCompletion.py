import sublime, sublime_plugin, os, re
from os.path import isfile, join

#
# Reads all effect and trigger names located in /scripted_effects and /scripted_triggers 
#


def make_completion(key,hint,content):
    return (key+"\t"+hint, content)

class StellarisScriptedCompletion(sublime_plugin.EventListener):
    def __init__(self):
        #Finds baselevel commands
        self.regex = re.compile('^(\w+) = {')

        #Completions are on tuple form (trigger\tHint, content)
        self.completion_list = []
        self.prefix_completion_dict = {}

        # construct a dictionary from (tag, attribute[0]) -> [attribute]
        # self.tag_to_attributes = get_tag_to_attributes()
    def on_activated(self, view):
        self.update_scripted_completions(view)

    def on_deactivated(self, view):
        pass
        #print(view.file_name())

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.stellaris"):
            return []
        
        
        #if prefix == '':
        #    return []
        # Only trigger within Stellaris
        # If it lags remove this, then it'll only update completions when switching tabs/tabbing then selecting
        # rather than everytime when you run the autocomplete
        self.update_scripted_completions(view)

        return self.get_completions(view, prefix, locations)

    def get_completions(self, view, prefix, locations):
        if prefix == '':
            completion_list = self.completion_list
        else:
            completion_list = self.prefix_completion_dict.get(prefix[0], [])
        return completion_list

    #Scans through all scripted triggers and effects and appends them to the autocomplete list.
    def update_scripted_completions(self, view):
        self.completion_list = []
        for base in view.window().folders():
            triggers_path = base+"/common/scripted_triggers/"
            effects_path  = base+"/common/scripted_effects/"
            if os.path.isdir(triggers_path):
                #print("Has triggers")
                self.scan_files(triggers_path)


            if os.path.isdir(effects_path):
                #print("Has effects")
                self.scan_files(effects_path, False)
        self.prefix_completion_dict = {}

        # construct a dictionary where the key is first character of
        # the completion list to the completion
        for s in self.completion_list:
            prefix = s[0][0]
            self.prefix_completion_dict.setdefault(prefix, []).append(s)


    def scan_files(self, dirpath,isTrigger=True):
        for filename in [f for f in os.listdir(dirpath) if isfile(join(dirpath,f))]:
            self.scan_file(join(dirpath,filename), isTrigger)

    def scan_file(self, filepath,isTrigger=True):
        #Walks through the file
        #If it finds a new keyword, it uses the previous comment as hint (if any)
        with open(filepath,'r') as f:
            hint = ""
            for line in f:
                if line.startswith("#"):
                    hint = line[1:]
                else:
                    match = self.regex.match(line)
                    if match and hint:
                        key = match.groups()[0]
                        self.completion_list.append(make_completion(key,hint,key))
                    elif match:
                        key = match.groups()[0]
                        self.completion_list.append(make_completion(key,("Scripted Trigger" if isTrigger else "Scripted Effect"),key))
                    else:
                        pass
                    #Throw away the hint makes us only match comments directly above the line with the effect/trigger name
                    hint = ""




