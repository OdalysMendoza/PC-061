$Python = "python.exe"


$Script = "C:\Users\odaly\Downloads\BasicOne.py"


function Ver-StatusPerfil{  
    param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil)  
    $status = Get-NetFirewallProfile -Name $perfil  
    Write-Host "Perfil:" $perfil  
    if($status.enabled){  
        Write-Host "Status: Activado"  
    } else{  
        Write-Host "Status: Desactivado"  
    }  
}  


Ver-StatusPerfil | & $Python $Script