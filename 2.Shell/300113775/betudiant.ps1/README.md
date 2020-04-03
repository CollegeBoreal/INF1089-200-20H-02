<#
.SYNOPSIS
    Ce script est un laboratoire Powershell

.DESCRIPTION
    Ce script est utilisé pour le laboratoire de programmation en Powershell.

.NOTES
    Author: 8dbe
    Derniere mise à jour: yyyy-mm-dd

#>

function Stagiaire {

    
    param (
        [String]$personneNom,
        [Int]$personneId
    )
    # message de bienvenue 
    
    "Hello {0} ! Your Student ID is : 300{1} ." -F $personneNom, $personnId
    
 }

# Appel de la fonction
etudiants "widby" 113775
