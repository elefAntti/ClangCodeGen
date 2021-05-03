#!/usr/bin/env python

import clang.cindex, asciitree, sys

clang.cindex.Config.set_library_path("/usr/lib/llvm-11/lib")
index = clang.cindex.Index(clang.cindex.conf.lib.clang_createIndex(False, True))
translation_unit = index.parse(sys.argv[1], ['-x', 'c++', '--std', 'c++17'])
print(asciitree.draw_tree(translation_unit.cursor,
  lambda n: [ x for x in n.get_children() if x.location.file.name.startswith("/app/data")],
  lambda n: "%s (%s)" % (n.spelling or n.displayname, str(n.kind).split(".")[1])))
