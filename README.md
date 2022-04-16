# script.refreshvideo
 
Kodi script runs JSON VideoLibrary.Refresh* method for a video library
list item.  The list item to uppdate must be focused in Kodi GUI and the
script is started using the RunScript(script.refreshvideo) builtin command.
The script will raise a Kodi notification dialog showing either "success" if
the refresh completed, or "fail" if it didn't.