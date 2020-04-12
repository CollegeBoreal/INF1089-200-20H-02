#. ..\..\scripts\students.ps1

#$here = Split-Path --path . -Parent $MyInvocation.MyCommand.Path
$here = Split-Path -Path ..\..\.scripts/students.ps1 -Resolve -Parent
echo $here
. "$here\students.ps1"

# $ETUDIANTS = 300104524, 300104541, 300105201, 300106918, 300107361, 300108234, 300110500, 300111671, 300111766, 300112017, 300112917, 300113775

echo "$ETUDIANTS"

#for ($i = 0; $i -le $ETUDIANTS.Count; $i = $i + 1) {
#    $ETUDIANTS[$i]
#}
