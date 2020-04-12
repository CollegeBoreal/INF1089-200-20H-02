$here = Split-Path -Path ..\..\  -Resolve -NoQualifier
echo $here
echo "$here\.scripts"
Get-ChildItem $here
Get-ChildItem "$here\.scripts"

$there = Split-Path -Path "$here\.scripts" 
echo $there

#. "$here\.scripts\students.ps1"

#echo $ETUDIANTS

