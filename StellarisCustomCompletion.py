import sublime, sublime_plugin, os, re
from os.path import isfile, join
import json
#
# Reads all effect and trigger names located in /scripted_effects and /scripted_triggers 
#


def make_completion(key,hint,content):
    return (key+"\t"+hint, content)

class StellarisScriptedCompletion(sublime_plugin.EventListener):
    def __init__(self):
        #Finds baselevel commands
        self.regex = re.compile('^(\w+) = {')
        self.completion_dir = os.path.dirname(__file__)+"/completions"
        #Completions are on tuple form (trigger\tHint, content)
        self.completion_list = []
        self.scope_completion_dict = {}
        self.prefix_completion_dict = {}

    def on_activated(self, view):
        self.load_completions()

    def load_completions(self):
        completion_files = os.listdir(self.completion_dir)
        for completion_file in completion_files:
            with open(os.path.join(self.completion_dir,completion_file)) as f:
                j = json.load(f,strict=False)
                self.scope_completion_dict[j['scope']] = list(map(lambda x: (x['trigger'],x['contents']), j['completions']))

    def on_deactivated(self, view):
        pass

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.stellaris"):
            return []
        scopelist = view.scope_name(locations[0]).split()

        if len(scopelist) >= 2:
            (blocktype,scoeptype) = scopelist[-2:]
            scope = " ".join(scopelist[-2:])
            return self.scope_completion_dict.get(scope,[])# + self.scope_completion_dict[blocktype+" block.Any"]
        else:
            return []

    def get_completions(self, view, prefix, locations):
        if prefix == '':
            completion_list = self.completion_list
        else:
            completion_list = self.prefix_completion_dict.get(prefix[0], [])
        return completion_list