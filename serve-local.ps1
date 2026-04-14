param(
    [int]$Port = 4000
)

$ErrorActionPreference = "Stop"

Write-Host "Building Jekyll site..."
bundle exec jekyll build

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$pyLauncher = Get-Command py -ErrorAction SilentlyContinue

if ($pythonCommand) {
    Write-Host "Serving _site at http://127.0.0.1:$Port"
    python -m http.server $Port --directory _site
    exit $LASTEXITCODE
}

if ($pyLauncher) {
    Write-Host "Serving _site at http://127.0.0.1:$Port"
    py -m http.server $Port --directory _site
    exit $LASTEXITCODE
}

throw "Python was not found. Install Python or run any static server against the _site directory."
