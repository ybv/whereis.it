<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

        <title>Where is it?</title>
               
    </head>
    <body>

        <script src="LAB.min.js" type="text/javascript"></script>        
<?


//PHP fallback to enable graceful degredation


//feel free to substitute with a more secure read-in method
$json = file_get_contents("data/album1.json");
$json_a=json_decode($json,true);
$folderType = $_GET['view'];
$index = $_GET['ind'];
$subalbums = array();
$i =0; $j =0;
error_reporting(0);

//expose convenient access to subalbums
foreach ($json_a as $p => $k){
    foreach($k["subalbum"] as $sub){ 
                 $subalbums[$i][$j] = $sub;
         $j++;
        }
        $i++;
} 

//handle 'view' switching

echo "<ul class='gallery'>";
foreach($subalbums[$index] as $sub){
echo "<li class='item drop-shadow round'><a href='"  . $sub['large_image'] . "'><img src='" . $sub['image'] . "'></img>" .  $sub['title']  . "</a> " . $sub['artist'] ." </li>";
 } 
echo "</ul>";            

        
 



?>
        <script type="text/javascript">
                   $LAB
                   .script("jquery-1.4.4.min.js").wait()
                   .script("jquery.tmpl.min.js")
                   .script("backbone-min.js");      
        </script>
    </body>
</html>