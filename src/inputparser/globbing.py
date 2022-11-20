import os

from application import Application


class Globbing:
    def __init__(self):
        self.poss_tops = []

    def glob(self, pattern: str) -> [str]:
        loc_patt, file_patt = self.get_file_and_location_pattern(pattern)

        top = self.set_start_top(loc_patt)

        self.set_poss_tops(loc_patt, top)

        return self.get_matches(file_patt)

    def get_file_and_location_pattern(self, pattern) -> ([str], str):
        pattern_split = pattern.split('/')
        if len(pattern_split) == 1:
            return [], pattern_split[0]

        location_pattern = pattern_split[:-1]
        file_pattern = pattern_split[-1]
        if location_pattern[0] == '.' or location_pattern[0] == '':
            location_pattern = location_pattern[1:]
        return location_pattern, file_pattern[0]

    def set_poss_tops(self, loc_pattern: [str], top: str) -> None:
        if not loc_pattern:
            self.poss_tops.append(top)
            return

        poss_dirs = Application.get_dir_contents(top)[1]
        for dir_ in poss_dirs:
            if self.match(loc_pattern[0], dir_):
                self.set_poss_tops(loc_pattern[1:], top + dir_ + '/')

    def match(self, pattern: str, string: str, i=0):
        if pattern == '' and len(string) == i:
            return True
        elif pattern == '' or i >= len(string):
            return False

        if pattern[0] == '*':
            return self.match(pattern[1:], string, i) or self.match(pattern, string, i + 1) \
                   or self.match(pattern[1:], string, i + 1)
        else:
            return string[i] == pattern[0] and self.match(pattern[1:], string, i + 1)

    @staticmethod
    def set_start_top(loc_patt: [str]) -> str:
        if len(loc_patt) > 0 and loc_patt[0] == '':
            return '/'
        return './'

    def get_matches(self, file_patt: str) -> [str]:
        if file_patt == '':
            return self.poss_tops

        matches = []

        for top in self.poss_tops:
            for file in Application.get_dir_contents(top)[1] + Application.get_dir_contents(top)[2]:
                if self.match(file_patt, file) and file[0] != '.':
                    if top[0:2] == './':
                        matches.append(top[2:] + file)
                    else:
                        matches.append(top + file)

        return sorted(matches)
