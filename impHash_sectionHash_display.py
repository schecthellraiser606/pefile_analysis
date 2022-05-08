import pefile
import sys

malw_file = sys.argv[1]
pe = pefile.PE(malw_file)

print("-----Import_Hash-----")
print(pe.get_imphash())
print("\n")

print("-----Section_Hash-----")
for section in pe.sections:
  print("%s:\t%s" % (section.Name, section.get_hash_md5()))  
print("\n")