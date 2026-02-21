<#
run_math.ps1 - Basic math operations

Usage (examples):
  .\run_math.ps1 add 4 5
  .\run_math.ps1 mul 3 2
  .\run_math.ps1 all 7 2     # prints results for all operations
  .\run_math.ps1            # interactive mode
  .\run_math.ps1 help       # show this help
#>

Param(
    [Parameter(Position=0, Mandatory=$false)]
    [ValidateSet('add','sub','mul','div','pow','mod','all','help')]
    [string]$Op = $null,

    [Parameter(Position=1, Mandatory=$false)]
    [double]$A = $null,

    [Parameter(Position=2, Mandatory=$false)]
    [double]$B = $null
)

function Show-Help {
    Write-Output "run_math.ps1 - perform basic math operations"
    Write-Output "Usage: run_math.ps1 <operation> <a> <b>"
    Write-Output "Operations: add, sub, mul, div, pow, mod, all, help"
    Write-Output "Examples:"
    Write-Output "  .\\run_math.ps1 add 4 5"
    Write-Output "  .\\run_math.ps1 all 7 2"
    Write-Output "If no arguments are provided the script enters interactive mode."
}

function Prompt-For-Args {
    while ($true) {
        $aRaw = Read-Host "Enter first number (or 'q' to quit)"
        if ($aRaw -eq 'q') { exit 0 }
        if ([double]::TryParse($aRaw, [ref]$null)) { $A = [double]$aRaw; break }
        Write-Output "Invalid number, try again."
    }
    while ($true) {
        $bRaw = Read-Host "Enter second number (or 'q' to quit)"
        if ($bRaw -eq 'q') { exit 0 }
        if ([double]::TryParse($bRaw, [ref]$null)) { $B = [double]$bRaw; break }
        Write-Output "Invalid number, try again."
    }
}

# If help explicitly requested
if ($Op -eq 'help') {
    Show-Help
    exit 0
}

# If no op provided, enter interactive mode
if (-not $Op) {
    Write-Output 'Interactive mode - choose operation: add, sub, mul, div, pow, mod, all, help'
    $Op = Read-Host 'Operation'
    if ($Op -eq 'help') { Show-Help; exit 0 }
}

# If numbers missing, prompt for them (except when Op is 'help')
# Simplify the condition to avoid operator precedence/parsing issues
if ($Op -ne 'help' -and ($A -eq $null -or $B -eq $null)) {
    Prompt-For-Args
}

# Ensure operation string is lowercase
$opLower = $Op.ToLower()

function Safe-Divide($x,$y) {
    if ($y -eq 0) { return $null }
    return ($x / $y)
}

switch ($opLower) {
    'add' {
        $res = $A + $B
        Write-Output "Result: $A + $B = $res"
    }
    'sub' {
        $res = $A - $B
        Write-Output "Result: $A - $B = $res"
    }
    'mul' {
        $res = $A * $B
        Write-Output "Result: $A * $B = $res"
    }
    'div' {
        $res = Safe-Divide $A $B
        if ($res -eq $null) { Write-Output "Error: division by zero" } else { Write-Output "Result: $A / $B = $res" }
    }
    'pow' {
        $res = [math]::Pow($A, $B)
        Write-Output "Result: $A ^ $B = $res"
    }
    'mod' {
        if ($B -eq 0) { Write-Output "Error: modulus by zero" } else { $res = $A % $B; Write-Output "Result: $A % $B = $res" }
    }
    'all' {
        Write-Output "Add:    $A + $B = $($A+$B)"
        Write-Output "Sub:    $A - $B = $($A-$B)"
        Write-Output "Mul:    $A * $B = $($A*$B)"
        if ($B -eq 0) { Write-Output "Div:    Error (division by zero)" } else { Write-Output "Div:    $A / $B = $([math]::Round(($A/$B),6))" }
        Write-Output "Pow:    $A ^ $B = $([math]::Pow($A,$B))"
        if ($B -eq 0) { Write-Output "Mod:    Error (modulus by zero)" } else { Write-Output "Mod:    $A % $B = $($A % $B)" }
    }
    Default {
        Write-Output "Unknown operation: $Op"
        Show-Help
        exit 2
    }
}
