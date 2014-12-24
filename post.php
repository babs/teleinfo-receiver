<?
ini_set("precision", 16);
$json = json_decode($GLOBALS["HTTP_RAW_POST_DATA"], true);
if (file_put_contents('dumps/'.$json["tramets"], $GLOBALS["HTTP_RAW_POST_DATA"]) === false) {
   header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error', true, 500);
}
