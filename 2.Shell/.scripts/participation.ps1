$here = Split-Path -Path ..\..\  -Resolve -NoQualifier
echo $here
echo "$here\.scripts"
$there = Split-Path -Path "$here\.scripts\*" 
echo $there

Get-Content "$there\students.ps1"

#echo $ETUDIANTS

