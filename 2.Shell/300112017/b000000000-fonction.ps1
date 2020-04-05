

# Definition de la fonction
  function Stagiaire {

   <#
   .SYNOPSIS
    Ce script est un laboratoire Powershell

   .DESCRIPTION
    Ce script est utilisé pour le laboratoire de programmation en Powershell.

    .NOTES
    Author: Olaitan
    Derniere mise à jour: 2020-04-02

     .Exemple
     Stagiaire -Compte "Ador"

      .Link
      https://github.com/ordenrosae
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

