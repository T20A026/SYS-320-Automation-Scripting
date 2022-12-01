#Create commandline parameters to copy a file and place it in an evidence dir
param(

    [Parameter(Mandatory = $true)]
    [int]$reportNo,

    [Parameter(Mandatory = $true)]
    [String]$filePath

)

#Create a dir with the report number
$reportDir = "rpt$reportNo"

mkdir $reportDir

Copy-Item $filePath $reportDir