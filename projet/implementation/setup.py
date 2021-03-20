import os

####################################################################
#
# CONSTANTS
#
####################################################################

#=========================================
# OS Name
# Values LINUX
#        WINDOWS
#=========================================
OS_Name = "LINUX"

#=========================================
# folders
#=========================================
FOLDER_RESULTS   = "results"
FOLDER_ZIPPEDLOG = "gz"
FOLDER_PWA       = "logpwa"


####################################################################
#
# TOOLS
#
#   sepDir  / or \ ?
#   folder  folder f exists ? create it if not. 
# 
####################################################################
def sepDir():
    """
    return "/" if OS_Name = "LINUX
    return "\" else
    """
    linuxPrefix = "/"
    winPrefix   = "\\"

    sep = linuxPrefix
    if OS_Name != "LINUX":
        sep = winPrefix
    # END IF
    return sep
    
def folder(f):
    """
    Verify if folder f exists.
    if not create it
    return the folder prefixed with the relative path. eg ./f (for linux) or .\f (for windows)
    """
    # INIT
    resFolder = "." + sepDir() + f

    # Create folder if not exists
    if not os.path.exists(resFolder):
        os.makedirs(resFolder)
    # END IF
    return resFolder
