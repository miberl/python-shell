from application import Application

class Sort(Application):
    
    def run(self, args, out)-> None:
        lines = []
        rev = self.is_reversed(args)
        
        files = [a for a in args if a[0] != "-"]

        for file in files:
            lines.extend(self.read_lines(file))
        
        lines.sort(reverse=rev)
        out.extend(lines)

    def is_reversed(self, args)-> bool:
        if "-r" in args:
            return True
        return False