#Powershell Script 

#Afficher a l'ecran pour permettre une entree
echo "Type the year that you want to check(4 digits), then press [ENTER]:"
read year

#Conditions pour que l'annee choisie soit une annee bissextile
if (( ("$year" % 400) == "0" )) || (( ("$year" % 4) == "0" )) && (( ("$year % 100") != "0" ))
   then
      echo "$year is a leap year"
else
     echo "This is not a leap year"
fi 
