# Copyright (C) 2022 - Scott Smart <scott967@kodi.tv>
# This program is Free Software see LICENSE file for details

"""Kodi script runs JSON VideoLibrary.Refresh* method for a video library
list item.  The list item to uppdate must be focused in Kodi GUI and the
script is started using the RunScript(script.refreshvideo) builtin command.
The script will raise a Kodi notification dialog showing either "success" if
the refresh completed, or "fail" if it didn't.
"""

try:
    import simplejson as json
except ImportError:
    import json

import xbmc
import xbmcgui

def main():
    """Wraps the code within a function
    """
    dialog = xbmcgui.Dialog()
    if xbmc.getInfoLabel('ListItem.DBType') in ['movie', 'episode', 'musicvideo', 'tvshow']:
        refreshtype = xbmc.getInfoLabel('ListItem.DBType')
        dbid = int(xbmc.getInfoLabel('ListItem.DBID'))
        json_call = ('{{"jsonrpc": "2.0", '
                        '"method": "VideoLibrary.Refresh{0}", '
                        '"params" : {{"{0}id": {1}, "ignorenfo": false}}, '
                        '"id": 1}}'.format(refreshtype, dbid))
        json_result = xbmc.executeJSONRPC(json_call)
        json_result = json.loads(json_result)
        if  ('result', 'OK') in json_result.items():
            dialog.notification('{} refresh'.format(refreshtype), 'success',
            xbmcgui.NOTIFICATION_INFO, 2000)
        else:
            dialog.notification('{} refresh'.format(refreshtype), 'fail',
            xbmcgui.NOTIFICATION_WARNING, 2000)
    else:
        dialog.notification('refresh', 'fail -- must use on a video list item',
        xbmcgui.NOTIFICATION_WARNING, 2000)

if __name__ == '__main__':
    main()
