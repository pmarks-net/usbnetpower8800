This is a simple command-line tool for controlling the "USB Net Power 8800"
from Linux (etc.) using Python and PyUSB.  It shows up under lsusb as:

> ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port

But, from what I can tell, none of the serial port features are ever used,
and all you really need is one USB control transfer for reading the current
state, and another for setting it.

The device is basically a box with a USB port and a switchable power outlet.
It has the unfortunate property that disconnecting it from USB immediately
kills the power, which reduces its usefulness.

### Links to similar projects: ###
  * [Plain C port, with faster startup time.](http://emergent.unpythonic.net/01330399156)
  * [Fork containing an install script and a few extra features.](https://github.com/nickodell/usbnetpower)
