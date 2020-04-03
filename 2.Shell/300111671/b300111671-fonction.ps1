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
     Author : AbbasSadissou
     Requires : PowerShell V2
 .EXAMPLE
     [ps] c:\foo> Test-Port « 10.13.5.55 »  8080
     true
  #>

# Definition de la fonction
function Stagiaire
 {
 [CmdletBinding()]
 param (
	[Parameter(Mandatory=$true)]
        [String]$personneNom,

	[Parameter(Mandatory=$true)]
	[ValidateRange(9,99)]
        [Int]$personneAge
	
	
    )
	
	#Test d'existance du compte dans Active directory
	try {$existeAD =(Get-ADUser $personneNom)}
	catch {$existeAD =$false}
	
	#Affichage du message d'existence ou de creation de compte
	if ($existeAD) {"le compte du stagiaire{0} existe dans Active Directory." -F $personneNom}
	else {"Vous devez creer le compte de {0} dans Active Directory." -F $personneNom}

	



	 # message de bienvenue 
    	BEGIN {Write-Verbose "Début du script"}
   	 PROCESS { "Bonjour {0} ! Tu as {1} ans." -F $personneNom, $personneAge }
    	END {Write-Verbose "Fin du script"}
}

# Appel de la fonction
Stagiaire Toronto 35
Stagiaire "Pascal Siakam" 26  -verbose
stagiaire "Alice" 7777
stagiaire "Alice" 35

stagiaire "Administrator"
stagiaire "delux" 
stagiaire "brice" 

Get-Help Stagiaire





