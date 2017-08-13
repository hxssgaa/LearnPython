import os


class CodeAnalyser(object):
    CODE_TYPE_PYTHON, CODE_TYPE_CPLUSPLUS, CODE_TYPE_C = range(1, 4)
    SUFFIX_MAP = {
        CODE_TYPE_PYTHON: '.py',
        CODE_TYPE_CPLUSPLUS: '.cpp',
        CODE_TYPE_C: '.c',
    }

    def __init__(self, code_dir, code_type=CODE_TYPE_PYTHON):
        """
        :type code_dir: str
        :type code_type: int
        """
        self.code_dir = code_dir
        self.code_type = code_type

    def count_line(self, f):
        """
        :type f: file
        :rtype: int
        """
        cnt = 0
        flag = True
        for l in f:
            if not l or not l.strip():  # check for empty line
                continue
            if '#' in l and not l[0: l.index('#')].strip():  # check for comment
                continue
            if '"""' in l and not l[0: l.index('"""')].strip():
                flag = not flag
                continue
            if not flag:
                continue
            cnt += 1
        return cnt

    def count_code_line_helper(self, code_dir=None):
        code_info = []
        code_dir = self.code_dir if not code_dir else code_dir
        for f_name in os.listdir(code_dir):
            f_path = os.path.join(code_dir, f_name)
            if os.path.isdir(f_path):
                code_info.extend(self.count_code_line_helper(f_path))
            if not f_name.endswith(self.SUFFIX_MAP[self.code_type]):
                continue
            if self.code_type == self.CODE_TYPE_PYTHON and f_name == "__init__.py":
                continue
            with open(f_path) as f:
                cl = self.count_line(f)
                code_info.append((f.name, cl))
        return code_info

    def count_code_line(self, code_dir=None, only_show_one=True, show_least=False):
        code_info = self.count_code_line_helper(code_dir)
        if only_show_one:
            code_line, code_file = max((e[1], e[0]) for e in code_info) \
                if not show_least else min((e[1], e[0]) for e in code_info)
            return "%s lines of code: %d" % (code_file, code_line)
        else:
            return "\n".join(map(lambda x: "%s lines of code: %d" % (x[0], x[1]), code_info))


def main():
    c = CodeAnalyser("/Users/hxssg/Documents/OpenStack Temp/neutron/neutron")
    print c.count_code_line(only_show_one=False, show_least=False)


if __name__ == '__main__':
    main()
