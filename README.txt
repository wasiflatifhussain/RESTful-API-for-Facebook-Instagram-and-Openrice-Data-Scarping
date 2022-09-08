How to run the system and server:

> install all the dependencies required by using the following command-
    pip install -r requirements.txt

    Special Note- make sure to install the version of chromedriver binary that is compatible with the google
                  chrome version installed on your computer
                  if google chrome version 103.(following) is installed on your computer, than make sure to
                  install chromedriver binary version 103.(following) also
                  please check pypi.org to find the versions of chromedrivers available
> to run the whole system-
    python3 app_execute.py 
    Special Note- please edit the run commands. by default, the command used is, for eg, 'py run.py'. however, if python 
                  installed on your device runs by python/python3, then edit the lines 4,5,6 from 
                  os.system('start cmd /k "py run.py"') to os.system('start cmd /k "python run.py"') or to
                  os.system('start cmd /k "python3 run.py"')

> all the data have can be accessed from the main url
> to visit the main localhost url, use the link-
        http://127.0.0.1:5001/

Note= The program requires use of chromedriver; please check the chrome version on your device and match it with
      the chrome version available on requirements.txt.
      If the versions dont math, install the compatible chromedriver version from pypi.org

