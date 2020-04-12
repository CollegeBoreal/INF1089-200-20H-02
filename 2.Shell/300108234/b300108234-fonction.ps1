<#
.SYNOPSIS
    Ce script est un laboratoire Powershell
.DESCRIPTION
    Ce script est utilisé pour le laboratoire de programmation en Powershell.
.NOTES
    Author: halimabzn
    Derniere mise à jour: yyyy-mm-dd
#>

# Definition de la fonction
function Stagiaire
 {
<#
.SYNOPSIS
    Ce script est un laboratoire Powershell qui presente la Promo2018
.DESCRIPTION
    Ce script est utilisé pour presenter les noms et les numéros d'identification des eleves de la promotion 2018... 

.PARAMETER personneNom, personneId
personneNom est l'identifiant de l'etudiant. Generalement, il s'agit du prénom.
personneId est l'ID de l'etudiant.
promo18 est un alias de personneNom.
Ces parametres sont obligatoire.

.EXAMPLE
Stagiaire Halima 300108234

.LINK
https://github.com/orgs/CollegeBoreal/teams/promo2018
#>

 [CmdletBinding()]
 param (
        [String]$personneNom,
        [Alias("promo18")]
        [Int]$personneId
        
    )

 # message de bienvenue 
    BEGIN {Write-Verbose "Debut du script"}
    PROCESS { "Bonjour {0} ! Votre ID est {1} et Vous faites partie de Promo18." -F $personneNom, $personneId }
    END {Write-Verbose "Fin du script"}
}

# Appel de la fonction
Stagiaire Echnaider 300104524 -verbose 
Stagiaire Romeo 300104541 -verbose
Stagiaire Abdel 300106918 -verbose 
Stagiaire Etienne 300106918 -verbose
Stagiaire Halima 300108234 -verbose
Stagiaire Dedier 300110500 -verbose 
Stagiaire Fabrice 300110529 -verbose
Stagiaire Abass 300111671 -verbose 
Stagiaire Cheikh 300111766 -verbose
Stagiaire Olaiton 300112017 -verbose 
Stagiaire Djuma 300112917 -verbose
Stagiaire Armand 300113775 -verbose


Get-Help Stagiaire
