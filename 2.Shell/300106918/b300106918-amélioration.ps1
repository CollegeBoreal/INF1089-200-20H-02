function Stagiaire {
<#
.SYNOPSIS 
#Vérifie l'existence d'un compte dans Active Directory.
.DESCRIPTION 
#Vérifie l'existence d'un compte dans Active Directory. L'objectif est de créer le compte s'il n'existe pas. 
.PARAMETER personneNom 
#c'est l'identifiant de l'utilisateur. Généralement, il s'agit du prénom. Compte est un alias de personneNom. Ce paramètre est obligatoire. 
.EXAMPLE 
#Stagiaire -Compte "Bob"
.LINK 
https://coudr.com/blog 


#>
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
Get-Help stagiaire

