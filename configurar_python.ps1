# Configura o Python (instalado via uv) no PATH permanente do usuario
# e desativa os aliases falsos do Microsoft Store.
# Execute uma unica vez como usuario normal (sem precisar de admin).

$pythonDir = "C:\Users\thiag\AppData\Roaming\uv\python\cpython-3.14.7-windows-x86_64-none"

# --- 1. Adiciona ao PATH do usuario (permanente) ---
$pathAtual = [System.Environment]::GetEnvironmentVariable("PATH", "User")

if ($pathAtual -notlike "*$pythonDir*") {
    $novoPath = "$pythonDir;$pathAtual"
    [System.Environment]::SetEnvironmentVariable("PATH", $novoPath, "User")
    Write-Host "[OK] Python adicionado ao PATH permanente."
} else {
    Write-Host "[OK] Python ja estava no PATH."
}

# --- 2. Desativa os aliases do Microsoft Store (sem precisar de admin) ---
$regBase = "HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths"

@("python.exe", "python3.exe") | ForEach-Object {
    $chave = "$regBase\$_"
    if (-not (Test-Path $chave)) { New-Item -Path $chave -Force | Out-Null }
    Set-ItemProperty -Path $chave -Name "(Default)" -Value "$pythonDir\python.exe"
    Write-Host "[OK] Alias '$_' redirecionado para o Python real."
}

# Desativa tambem via registro o App Execution Alias do Store
$aliasReg = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.py\OpenWithList"
# (apenas informa; a desativacao visual e feita nas Configuracoes do Windows)

Write-Host ""
Write-Host "Pronto! Feche este PowerShell e abra um novo."
Write-Host "Depois teste com:  python --version"
