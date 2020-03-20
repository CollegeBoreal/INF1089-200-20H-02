Clear-Host

$villes =  "Nantes","Lyon"

"test" -F ${ville}.Count

foreach ($ville in $villes)
{
    "${0} est une tres belle ville" -F $ville
} 