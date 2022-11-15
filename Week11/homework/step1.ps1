#Copy Powershell to home directory
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\abija"

# Rename the file

Rename-Item -Path "C:\Users\abija\powershell.exe" -NewName "EnNoB-1216.exe"
"If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."| Out-File -FilePath "C:\Users\abija\Desktop\Readyou.READ"

# Test for Powershell
if (Test-Path -Path "C:\Users\abija\EnNoB-1214.exe") {
    Write-Output "Powershell Moved and Concealed!"
} else{
     Write-Output "Powershell  Task Failed!"
}

# Testing For Note
if (Test-Path -Path "C:\Users\abija\Desktop\Readme.READ") {
    Write-Output "Ransome Note Created!"
} else{
     Write-Output "Ransome Note Failed!"
}
