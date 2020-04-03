
<#
 .SYNOPSIS
     Verifie d’un port tcp distant
 .DESCRIPTION
     La fonction TEST-Port retourne $true si le port est ouvert sinon $false
 .PARAMETER Host
        Nom du volume ex: c:
 .PARAMETER Port
        Numéro de port TCP (inférieure  à 65535)
 .PARAMETER Timeout
        Durée du timeout en ms (par défaut 300ms)
 .NOTES
     Author : Abbasdelux
     Requires : PowerShell V2
 .EXAMPLE
     [ps] c:\foo> Test-Port « 10.13.5.50 »  8080
     true
  #>
  
function Test-Port{
param(
[Parameter(Mandatory=$true,Position=0)][String[]]$Host ,
[Parameter(Mandatory=$true,Position=1)][ValidateRange(0,65535)] [Long]$Port,
[Parameter(Mandatory=$false,Position=2)][Long]$Timeout=300
)
$tcpclient = new-Object system.Net.Sockets.TcpClient
$iar = $tcpclient.BeginConnect($Host,$Port,$null,$null)

# Set the wait time
$wait = $iar.AsyncWaitHandle.WaitOne($Timeout,$false)

# Check to see if the connection is done
if(!$wait)
{
# Close the connection and report timeout
$tcpclient.Close()
Return $false
}
else
{
# Close the connection and report the error if there is one
$error.Clear()
$tcpclient.EndConnect($iar) | out-Null
if(!$?){$failed = $true}
$tcpclient.Close()
}

# Return $true if connection Establish else $False
if($failed){return $false}else{return $true}
}
