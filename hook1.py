"""
requirement

pythoncom
  conda install -c anaconda comtypes 

pyHoook
  download ke
    https://www.lfd.uci.edu/~gohlke/pythonlibs/
  ambil:
    python_hdf4‑0.9‑cp27‑cp27m‑win_amd64.whl
  install:
    pip.exe install python_hdf4‑0.9‑cp27‑cp27m‑win_amd64.whl

selenium
  conda install -c conda-forge selenium 
"""

import pythoncom, pyHook
import ctypes

def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'

    if event.Key == 'F12':
       MessageBox = ctypes.windll.user32.MessageBoxA
       MessageBox(None, 'The Chippy Program exited...', 'alert', 0)
       print "Exiting..."
       exit(0)
  
    if event.Alt == 'F11':
       MessageBox = ctypes.windll.user32.MessageBoxA
       MessageBox(None, 'The Chippy Program exited...FFFFF', 'alert', 0)
       print "Exiting..."
       exit(0)


# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

