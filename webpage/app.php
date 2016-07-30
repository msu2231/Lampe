<?php
if (!file_exists("light.txt"))
{
	$datei = fopen ("light.txt", "w");
	fwrite($datei, "0");
	fclose($datei);
}

$file_content = file_get_contents ("light.txt");

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
?>
