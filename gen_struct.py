import sys
import clang.cindex
from dataclasses import dataclass, field
from mako.template import Template

@dataclass
class Struct:
		namespace:list = field(default_factory=list)
		name:str = ""
		fields:list = field(default_factory=list)

def collectStructs( node, namespace = [] ):
	structs =[]
	for child in node.get_children():
		if child.kind == clang.cindex.CursorKind.STRUCT_DECL\
		  and child.location.file.name.startswith("/app/data"):
			struct = Struct()
			struct.name = child.spelling

			struct.fields = [ (field.type.spelling, field.spelling) for field in child.get_children()\
			  if field.kind == clang.cindex.CursorKind.FIELD_DECL ]
			struct.namespace = list( namespace )
			structs.append(struct)
		elif node.kind == clang.cindex.CursorKind.NAMESPACE:
				namespace = namespace + [ node.spelling ]
				structs += collectStructs( child, namespace )
		elif node.kind == clang.cindex.CursorKind.TRANSLATION_UNIT:
			structs += collectStructs( child, namespace )
	return structs

clang.cindex.Config.set_library_path("/usr/lib/llvm-11/lib")
index = clang.cindex.Index(clang.cindex.conf.lib.clang_createIndex(False, True))
translation_unit = index.parse(sys.argv[1], ['-x', 'c++', '--std', 'c++17'])
structs = collectStructs( translation_unit.cursor )

tpl = Template(filename='/app/templates/struct.mako')
string = tpl.render( structs=structs )

if len(sys.argv) > 2:
	open(sys.argv[2], 'w').write(string)
else:
	print(string)
