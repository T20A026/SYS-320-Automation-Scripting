# List files in a dir

#Lists all items, and prints full path
#Get-ChildItem -Recurse -Include *.pdf, *.docx -Path .\Documents | Select FullName

#Get-ChildItem -Recurse -Include *.pdf, *.docx -Path .\Documents | Export-Csv -Path files.csv

#Import the csv
$filelist = Import-Csv -path .\files.csv -header FullName

#Loop Through the results
foreach ($f in $filelist) {
    Get-ChildItem -Path $f.FullName
}