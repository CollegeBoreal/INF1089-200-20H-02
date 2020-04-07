# Definition de la fonction
function Stagiaire {

    <#
    .SYNOPSIS
     Verifie l'existence d'un compte dans Active Directory
    .DESCRIPTION
     Verifie l'existence d'un compte dans Active Directory. L'objectif est de creer le compte s'il n'existe pas 
    .PARAMETER personneNom
     C'est l'identifiant de l'utilisateur generalement , il s'agit d'un prenom
     compte est un alias de personneNom
     Ce parametre est obligatoire 
     .EXAMPLE 
      Stagiaire -Compte "Bob"
     .Link
       https://github.com/8dbe
       #> 
       
       [CmdletBinding()]
       param (
          [Parameter(Mandatory=$true)]
          [Alias("Compte")]
          [String]$personneNom
          )
       
       # Text d'existence du compte dans Active directory
       Try {$existAD = (Get-ADUser $personneNom)}
       catch {$existAD = $false}
     
       # Affichage du message d'existence ou de création du compte
       if ($existAD) {"le compte su stagiaire {0} existe dans Active Directory." -F $personneNom}
       else {"vous devez créer le compte de {0} dans Active Directory." -F $personneNom}
    }
  
   Get-Help Stagiaire