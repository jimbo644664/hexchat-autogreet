# hexchat-autogreet
Time-specific greeter plugin for HexChat

## What is it?
Basically, whenever someone enters the channel, this module greets them according to what time it is in their timezone.

To do this, it traps the Join event of HexChat, uses CTCP to get their current time, and then sends the greeting to the channel that the event was generated from.

## Why?
First of all, because I'm lazy, and wanted to work on a quick project using HexChat's Python API.

Moreover, often someone will come into a channel and then leave (presumably due to inactivity) before I have a chance to say hello. To be perfectly honest, the timezone-specfic part came in because I wanted to see if I could get the event trapping and callbacks to work.

## Extra
I'm releasing this under the 'do whatever the hell you want with it' license. That said, if you have any ideas for new features, don't hesitate to start a pull request or an issue.
