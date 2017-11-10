import json
import os
import time
import argparse
import sys

current_date = time.strftime("%d.%m.%Y_%H%M%S")
count = 0
script_path = (os.path.dirname(os.path.realpath(__file__)))
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", default = "choose daily | weekly | monthly ", help="configuration file")
args = parser.parse_args()
os.system('tput clear')

# colors
class text_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print text_colors.WARNING + " Sync Server script v 2.0.1" + text_colors.ENDC
print "Use: python syncs.py --type daily"
print('')

print( "Processing type...  {} ".format(
        args.type
        ))

config_file = script_path+'/backups.json'

print "Parser file: "+config_file
print ""
print ""

with open(config_file) as json_file:
    data = json.load(json_file)
    for p in data['sites']:
        count=count+1
        def beep():
                print "\a"
        beep()
        beep()
        beep()
        status =  p['status']
        #print count
        print "Reference: "+p['reference']
        print 'Backup reference: ' + p['reference'] +' / status: '+status
        if status == "1":
                to = p['to'] +'/'+args.type+'/'
                log_file = script_path+'/logs/'+args.type+'/'+p['reference'] + '_' +current_date+'.log'
                os.system('rsync -Cravz --progress --delete-excluded '+p['from']+' '+to+' --log-file='+log_file)
                print('')
                print('')
print "End..."
