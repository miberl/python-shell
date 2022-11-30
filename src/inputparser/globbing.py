from application import Application


class Globbing:
    """
    NAME
        Globbing
    DESCRIPTION
        Encapsulates logic to return value(s) for a globbed argument
    """
    def __init__(self):
        self.poss_tops = []

    def glob(self, pattern: str) -> [str]:
        """
        Returns a list of files/directories matching the pattern from pwd.

        :param pattern: String, including *, to be matched
        :return: String list of matches
        """
        loc_patt, file_patt = self._get_file_and_location_pattern(pattern)

        loc_patt, top = self._set_start_top(loc_patt)

        self._set_poss_tops(loc_patt, top)

        return self._get_matches(file_patt)

    @staticmethod
    def _get_file_and_location_pattern(pattern) -> ([str], str):
        pattern_split = pattern.split('/')
        if len(pattern_split) == 1:
            return [], pattern_split[0]

        location_pattern = pattern_split[:-1]
        file_pattern = pattern_split[-1]
        if location_pattern[0] == '.':
            location_pattern = location_pattern[1:]
        return location_pattern, file_pattern

    def _set_poss_tops(self, loc_pattern: [str], top: str) -> None:
        if not loc_pattern:
            self.poss_tops.append(top)
            return

        poss_dirs = Application.get_dir_contents(top)[1]
        for dir_ in poss_dirs:
            if self._match(loc_pattern[0], dir_):
                self._set_poss_tops(loc_pattern[1:], top + dir_ + '/')

    def _match(self, pattern: str, string: str, i=0):
        if pattern == '' and len(string) == i:
            return True
        elif pattern == '' or i >= len(string):
            return False

        if pattern[0] == '*':
            return self._match(pattern[1:], string, i) or \
                   self._match(pattern, string, i + 1) or \
                   self._match(pattern[1:], string, i + 1)
        else:
            return string[i] == pattern[0] and \
                   self._match(pattern[1:], string, i + 1)

    @staticmethod
    def _set_start_top(loc_patt: [str]) -> (str, str):
        if len(loc_patt) > 0 and loc_patt[0] == '':
            return loc_patt[1:], '/'
        return loc_patt, './'

    def _get_matches(self, file_patt: str) -> [str]:
        if file_patt == '':
            return self.poss_tops

        matches = []

        for top in self.poss_tops:
            files1 = Application.get_dir_contents(top)[1]
            files2 = Application.get_dir_contents(top)[2]
            for file in files1+files2:
                if self._match(file_patt, file) and file[0] != '.':
                    if top[0:2] == './':
                        matches.append(top[2:] + file)
                    else:
                        matches.append(top + file)

        return sorted(matches)
