# Python 3.5
# HexChat >2.9.6

import hexchat
import re

__module_name__ = "Autogreeter"
__module_version__ = "1.0"
__module_description__ = "Automatically responds to join events with a time-specific greeting."

greeting = "{} {} - {}".format(__module_name__, __module_version__, __module_description__)
hexchat.emit_print("Generic Message", "Loading", greeting)

def daytime(hour):
    hour = int(hour)
    
    if hour < 12:
        return 'morning'
    elif hour < 17:
        return 'afternoon'
    else:
        return 'evening'

def greeter(word, word_eol, userdata):
    nick = word[0]
    chan = word[1]
    
    reply_hook = None
    send_hook = None
    
    def on_reply(word, word_eol, userdata):
        match = re.search('(\d\d):\d\d:\d\d', word_eol[3])
        if match:
            msg = 'Good {}'.format(daytime(match.group(1)))
        else:
            msg = 'Hello'
        
        hexchat.command('msg {} {}!'.format(chan, msg))
        
        hexchat.unhook(reply_hook)
        return hexchat.EAT_ALL
    
    def on_send(word, word_eol, userdata):
        hexchat.unhook(send_hook)
        return hexchat.EAT_ALL
    
    reply_hook = hexchat.hook_server('NOTICE', on_reply, priority=hexchat.PRI_HIGHEST)
    send_hook = hexchat.hook_print('CTCP Send', on_send, priority=hexchat.PRI_HIGHEST)
    
    hexchat.command('ctcp {} TIME'.format(nick))
    return hexchat.EAT_NONE

hexchat.hook_print('Join', greeter, priority=hexchat.PRI_HIGHEST)