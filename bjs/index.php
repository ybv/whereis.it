<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

        <title>Where is it?</title>
      
               
    </head>
    <body>
        <div id="container">
            <div id="header">
                <h1>
                    <a href="index.php">Multi-Level Backbone Gallery</a>
                </h1>
                <h3>Created by Addy Osmani for 'Building Single-page Apps With jQuery's Best Friends'</h3>
            </div>

            <div id="main">
                 <div class="jstest">This application is running with JavaScript turned off.</div>
            </div>
        </div>
        <script src="LAB.min.js" type="text/javascript"></script>

        
<?


//PHP fallback to enable graceful degredation


//feel free to substitute with a more secure read-in method
$json = file_get_contents("data/album1.json");
$json_a=json_decode($json,true);
$folderType = $_GET['view'];
$index = $_GET['ind'];
$subal = $_GET['subalbum'];
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
switch($folderType){
      
        
        default:
            $ind = 0;
                echo "<ul class='gallery'>";
                foreach($json_a as $p => $k){
                   echo "<li class='item drop-shadow round'><a href='index.php?view=subalbum&ind=$ind'><img src='" . $k['image'] . "'></img>" .  $k['title']  . "</a> " . $k['years'] ." </li>";
                   $ind++;
                }
                echo "</ul>";
        break;
}


?>
        <script type="text/javascript">
                   $LAB
                   .script("jquery-1.4.4.min.js").wait()
                   .script("jquery.tmpl.min.js")
                   .script("backbone-min.js");      
        </script>
    </body>
</html>