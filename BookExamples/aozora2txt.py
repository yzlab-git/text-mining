import re

input_fn ='text/kageotoko.txt'
output_fn = 'text/kageotoko.stripruby.txt'

with open(input_fn, encoding='shift-jis') as fin, open(output_fn, mode='w') as fout:
   for line in fin:
         fout.write(re.sub(r'《[^》]+》| ［[^］]+］ ','', line))