$here = Split-Path -Path ..\..\  -Resolve -NoQualifier
echo $here
echo "$here\.scripts"
Get-ChildItem $here

#. "$here\.scripts\students.ps1"

#echo $ETUDIANTS

