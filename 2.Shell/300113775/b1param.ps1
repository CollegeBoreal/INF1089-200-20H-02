<#
.SYNOPSIS
    Ce script est un laboratoire Powershell

.DESCRIPTION
    Ce script est utilisé pour le laboratoire de programmation en Powershell.

.NOTES
    Author: CollegeBoreal
    Derniere mise à jour: yyyy-mm-dd

#>

function Stagiaire {

    [CmdletBinding()]
    param (
	[Parameter(Mandatory=$true)]
        [String]$personneNom,
	
	[Parameter(Mandatory=$true)]
	[ValidateRange(7,77)]
        [Int]$personneAge
    )
    # message de bienvenue 
    BEGIN {Write-Verbose "Début du script"}
    PROCESS { "Bonjour {0} ! Tu as {1} ans." -F $personneNom, $personneAge }
    END {Write-Verbose "Fin du script"}
 }


 Stagiaire "Alice" 35