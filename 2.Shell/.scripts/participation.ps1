$here = Split-Path -Parent $MyInvocation.MyCommand.Path
echo $here
. "$here\Add-Numbers.ps1"
