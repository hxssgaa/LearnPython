# coding=utf-8
import os
import re
from collections import OrderedDict

SEARCH_PATH = '/Users/hxssg/Downloads/shopping-home-trunk/WebRoot/WEB-INF/templates/zh_cn'


def get_html_feature(html_file):
    for l in html_file:
        res = re.search(b'<title>(.+)</title>', l)
        if res:
            return {"title:": res.group(1)}
    return {}


def get_html_feature_map(html_dir):
    m = OrderedDict()
    for f_name in os.listdir(html_dir):
        f_path = os.path.join(html_dir, f_name)
        if os.path.isdir(f_path):
            m[f_name] = get_html_feature_map(f_path)
        else:
            with open(f_path) as f:
                m[f_name] = get_html_feature(f)

    return m


def output_html_feature_map(output_file, feature_map, prev_keys):
    for k, v in feature_map.items():
        if isinstance(v, dict):
            output_html_feature_map(output_file, v, prev_keys + [k])
        else:
            prev_key_str = "/".join(prev_keys)
            prev_key_str = prev_key_str.ljust(70, ' ')
            output_file.write("%s-->%s\n" % (prev_key_str, v))


def main():
    m = get_html_feature_map(SEARCH_PATH)
    with open("extracted.txt", "w") as f:
        output_html_feature_map(f, m, [])


if __name__ == '__main__':
    main()
