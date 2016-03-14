nosetests -s -v --with-ignore-docstrings --with-xunit --xunit-file=unit_results.xml .\tests\unit
echo "uploading results"
echo $env:APPVEYOR_JOB_ID
$wc = New-Object 'System.Net.WebClient'
$wc.UploadFile("https://ci.appveyor.com/api/testresults/xunit/$($env:APPVEYOR_JOB_ID)", (Resolve-Path .\unit_results.xml))
exit 0