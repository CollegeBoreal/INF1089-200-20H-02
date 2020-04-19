function Stagiaire {
<#

.SYNOPSIS

    #Ce script est un laboratoire Powershell

    #Vérifie l'existence d'un compte dans Active Directory.
.DESCRIPTION

    #Ce script est utiliser pour le laboratoire de programmation en Powershell.
    
    #Vérifie l'existence d'un compte dans Active Directory. L'objectif est de créer le compte s'il n'existe pas. 

.PARAMETER personneNom 
    #c'est l'identifiant de l'utilisateur. Généralement, il s'agit du prénom. Compte est un alias de personneNom. Ce paramètre est obligatoire. 

.EXAMPLE 
    #Stagiaire -Compte "Bob"

.LINK 
    #https://coudr.com/blog 

.NOTES

    Author: AEKchaouche
    Derniere mise à jour: yyyy-mm-dd
#>

# Definition de la fonction

    [CmdletBinding()]
    param (
           [String]$personneNom,
           [Int]$personneAge

       )
   
    # message de bienvenue 
    BEGIN {Write-Verbose "Début du script"}
    PROCESS { "Bonjour {0} ! Tu as {1} ans." -F $personneNom, $personneAge }
    END {Write-Verbose "Fin du script"}



{
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [Alias("Compte")]
        [string]$personneNom
        )
#Test d'existence du compte dans Active Directory 
try {SexistAD = (Get-ADUser $personneNom)} 
catch {SexistAD $false} 

#Affichage du message d'existence ou de création du compte 
if ($existAD) {"Le compte du stagiaire (e} existe dans Active Directory." -F $personneNom }
else {"vous devez creer le compte de {0} DANS Active Directory." -F $personneNom}

}

   
   # Appel de la fonction
   Stagiaire Toronto 35 
   Stagiaire "Pascal Siakam" 26  -verbose
  
   Get-Help stagiaire
