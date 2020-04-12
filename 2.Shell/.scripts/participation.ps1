$here = Split-Path -Path ..\..\  -Resolve -NoQualifier
echo $here
echo "$here\.scripts"
$there = Split-Path -Path "$here\.scripts\*" 
echo $there

Write-Host "$there\students.ps1"

#echo $ETUDIANTS

