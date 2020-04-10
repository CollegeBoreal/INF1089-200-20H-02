<#
.SYNOPSIS
    Ce script est un laboratoire Powershell

.DESCRIPTION
   Ce script est utilisé pour le laboratoire de programmation en Powershell.

.NOTES
     Author: toch90
    Derniere mise à jour: yyyy-mm-dd
#>


# Definition de la fonction
function Stagiaire 
{ 
        [CmdletBinding()]
        param (
# On ajoute a la fonction des parametres mandataires pour exiger le nom et l'age
	    [Parameter(Mandatory=$true)]
            [String]$personneNom,

            [Parameter(Mandatory=$true)]
# On ajoute a la fonction une tranche d'age a laquelle la presonne doit se trouver
            [ValidateRange(7,77)]
	    [Int]$personneAge
    )
    # message de bienvenue 
    BEGIN {Write-Verbose "Début du script"}
    PROCESS { "Bonjour {0} ! Tu as {1} ans." -F $personneNom, $personneAge }
    END {Write-Verbose "Fin du script"}

}

# Appel de la fonction
Stagiaire "Pascal Siakam" 26  -verbose
# 4 Tests pour verifier nos conditions
# sans aucun parametres 
Stagiaire
# Sans le parametre age
Stagiaire "Alice"
# Avec l'age en dehors de la tranche d'age exigee
Stagiaire "Alice" 79
# Respectant tous les conditions
Stagiaire "Ben" 35
