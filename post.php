<?
ini_set("precision", 16);
$json = json_decode($GLOBALS["HTTP_RAW_POST_DATA"], true);
file_put_contents('dumps/'.$json["tramets"], $GLOBALS["HTTP_RAW_POST_DATA"]);

