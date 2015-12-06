import sublime
import sublime_plugin

class SelectMultiLinesCommand(sublime_plugin.TextCommand): 
    def run(self, edit):
        sel_regions = []
        for sel_region in self.view.sel():
            sel_regions.append(sel_region)
        for sel_region in sel_regions:
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                sel_text = sel_text.replace("$","\$")
                sel_text = sel_text.replace("(","\(")
                sel_text = sel_text.replace(")","\)")
                if len(sel_text) > 0:
                    if sel_text == "\n":
                        find_regions = self.view.find_all("^\n", sublime.IGNORECASE)
                    else:
                        find_regions = self.view.find_all(".*" + sel_text + ".*\n", sublime.IGNORECASE)
                    for find_region in find_regions:
                        self.view.sel().add(find_region)
