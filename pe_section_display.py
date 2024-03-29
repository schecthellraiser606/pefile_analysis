import pefile
import sys

malw_file = sys.argv[1]
pe = pefile.PE(malw_file)

for section in pe.sections:
  print(" %s %s %s %s %s" % (section.Name,
                          hex(section.VirtualAddress),
                          section.Misc_VirtualSize,
                          section.SizeOfRawData,
                          section.get_entropy()))
print("\n")
