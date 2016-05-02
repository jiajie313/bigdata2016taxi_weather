#!/usr/bin/python
import sys
	for line in sys.stdin:
		line = line.strip()
		
	if line == '  USAF  WBAN YR--MODAHRMN DIR SPD GUS CLG SKC L M H  VSB MW MW MW MW AW AW AW AW W TEMP DEWP    SLP   ALT    STP MAX MIN PCP01 PCP06 PCP24 PCPXX SD':
		continue
	elif len(line) == 33:
		word = line.split(' ')
		# wordneeded = word[2],word[4],word[10],word[14],word[17],word[18],word[19]
	print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(word[2],word[4],word[10],word[14],word[17],word[18],word[19])