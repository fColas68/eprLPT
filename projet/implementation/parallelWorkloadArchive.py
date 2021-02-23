import urllib.request
import os
import pathlib

def pwaFileManage(webRetrieve=False, unzipfiles=True):
    tabFiles = []
    
    #-------------------------------
    # script's directory
    # Create requested directories
    #curDir = os.path.abspath(os.curdir) 
    #-------------------------------
    zipDir = "./gz"  # curDir+"/gz"
    logDir = "./log" # curDir+"/log"
    if not os.path.exists(zipDir):
        os.makedirs(zipDir)
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    
    #-------------------------------
    # Web resource web --> zipDir
    #-------------------------------
    if webRetrieve:
        # read distant file
        fichierNom = "https://www.cs.huji.ac.il/labs/parallel/workload/logs-list"
        req = urllib.request.Request(url=fichierNom) 
        fichierId = urllib.request.urlopen(req)

        # put the list on a tab tabFiles
        contentsLine = fichierId.readline().decode('utf-8')
        while contentsLine:
            tabFiles.append(contentsLine)
            contentsLine = fichierId.readline().decode('utf-8')

        # close the file
        fichierId.close()

        # now i have my list pf logs
        #print (tabFiles)


        for file in tabFiles:
            fileInfo = pathlib.Path(file)
            # destFile = os.path.join(zipDir, fileInfo.name)
            destFile = zipDir+"/"+fileInfo.name
            urllib.request.urlretrieve(file, destFile)
            print("file "+destFile+" retrieved.")

    #-------------------------------
    # Files unzip (zipDir --> logDir
    #-------------------------------
    if unzipfiles:
        zipFiles = os.listdir(zipDir)
        print(zipFiles)
        for file in zipFiles:
            print(file)

pwaFileManage(True, False)
