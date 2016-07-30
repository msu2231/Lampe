<?php
if (!file_exists("light.txt"))
{
	$datei = fopen ("light.txt", "w");
	fwrite($datei, "0");
	fclose($datei);
}

echo "<html>";
echo "<head>";
echo "<meta charset=\"ISO-8859-1\">";
echo "<title>Steuerungsseite Warnleuchte<title>";
echo "</head>";
echo "<body>";
echo "<form action=\"index.php\" method=\"post\">";
echo "	<input type=\"submit\" name=\"active\" value=\"Lampe aktivieren / <br />deaktivieren\">"
echo "</form>"
echo "</body>";
echo "</html>";

if (isset($_POST['active']))
{
  if ($file_content === 1)
  {
    $datei = fopen("light.txt", "w");
    fwrite($datei, "0");
    fclose($datei);
  }
  else {
    $datei = fopen("light.txt", "w");
    fwrite($datei, "1");
    fclose($datei);
  }
}
?>
