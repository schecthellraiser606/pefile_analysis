import pefile
import sys

malw_file = sys.argv[1]
pe = pefile.PE(malw_file)

print("-----Import_APIfunctions-----")

if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
  for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print("%s" % entry.dll)
    for imp in entry.imports:
      if imp.name != None:
        print ("\t%s" % (imp.name))
      else:
        print ("\tord(%s)" % (str(imp.ordinal)))
    print ("\n")
    
print ("\n")
    
print("-----export_APIfunctions-----")
if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
  for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    print("%s" % exp.name)
  print ("\n")