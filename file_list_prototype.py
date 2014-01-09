import os
import mimetypes

def path_get(dictionary, path):
    for item in path.split("/"):
        if item != '':
            if not item in dictionary:
                dictionary[item] = {}
                return dictionary[item]
            else:
                dictionary = dictionary[item]
    return dictionary

def path_set(dictionary, path, item):
    path_tuple = path.split("/")
    key = path_tuple[-1]

    dictionary = path_get(dictionary, "/".join(path_tuple[:-1]))
    dictionary[key] = item

def find_dirs(content_dict, dirname, names):
    for leaf in names:
        abspath = os.path.join(dirname, leaf)
        if os.path.isfile(abspath) and \
           mimetypes.guess_type(abspath)[0] is not None and \
           "text" in mimetypes.guess_type(abspath)[0]:
            try:
                with open(abspath) as handle:
                    path_set(content_dict, abspath, handle.readlines())
            except:
                raise
                pass

def file_list(directory):
    content_dict = {}
    os.path.walk(directory, find_dirs, content_dict)
    print content_dict.keys()

file_list("/etc/")
