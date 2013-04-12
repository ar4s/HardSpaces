import sublime
import sublime_plugin


class HardCommand(sublime_plugin.TextCommand):

    """
    Usuwanie "sierot" na końcach linii w plikach HTML.
    """

    def run(self, edit):
        pattern = r"\s(a|i|u|o|w|z|oraz|lub|albo|do|przy|nad|pod|na)\s"
        sel_regions = self.view.sel()
        for r in sel_regions:
            region = self.view.find(pattern, r.begin())
            while region:
                print region
                glue = self.view.substr(region)[1:-1]
                self.view.replace(edit, region, " "+glue+"&nbsp;")
                region = self.view.find(pattern, region.end())
