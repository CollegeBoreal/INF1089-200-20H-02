function Stagiaire {

   
    param ([String]$personneNom)

    # test d'existence du compte dans active directory
        try {$existeAD = (Get-ADUser $personneNom)}
        catch {$existeAD = $false}
    #
        if ($existeAD){"le compte du stagiaire {0} existe dans Active Directory."}
        else {"vous devez creer le compte de {0} dans Active Directory." -F $personneNom}
	
	
 }

 Stagiaire "Alice"

 Stagiaire "Chris"

 Stagiaire "Bob"