from application import Application

class Sort(Application):
    
    def run(self, args, out)-> None:
        lines = []
        for a in args:
            lines.extend(self.read_lines(a))
        lines.sort()
        out.extend(lines)