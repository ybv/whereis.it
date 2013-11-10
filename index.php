
<!DOCTYPE html><head>
<title>Justified Gallery Example</title>

<link href="http://www.jqueryscript.net/css/top.css" rel="stylesheet" type="text/css">

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<link rel='stylesheet' href='jquery-colorbox/colorbox.css' type='text/css' media='screen' />
<script type='text/javascript' src='jquery-colorbox/jquery.colorbox-min.js'></script>
<link rel='stylesheet' href='../css/jquery.justifiedgallery.min.css' type='text/css' media='all' />
<script type='text/javascript' src='../js/jquery.justifiedgallery.min.js'></script>
</head>

</script>


<style type="text/css">
  .example-description { margin: 20px 0 20px 0;}
  #myExample3 {

      line-height: 0;
      z-index: 0;
   -webkit-column-count: 6;
   -webkit-column-gap:   1px;
   -moz-column-count:    6;
   -moz-column-gap:      1px;
   column-count:         6;
   column-gap:           1px;
  }
  #imgs{
   width: 100%;
  height: auto;
  }
  @media (max-width: 1200px) {
  #myExample3 {
  -moz-column-count:    5;
  -webkit-column-count: 7;
  column-count:         5;
  }
}

#myExample3 img:hover:after{
content: attr(title);
}
#where{
    position: absolute;
    z-index: 90;
    width:350px;
    height:11%;
    bottom:50px;
    right: 20px;
    padding:0px 20px;
    background: rgba(255, 255, 255, 0.9);
}
</style>
<script type="text/javascript">

  var data2="";
 function onld(){
  $.getJSON('template_c.js', function(data) {


          for (var i in data.pages) {
            var curr = data.pages[i];
            var id1 = curr.id;
            var pagel = id1+".html";
            var location1 = curr.location;
            var img_link = curr.image_link;
            data2+= "<a href=\""+ pagel+"\" title=\""+location1+"\"> <img id =\"imgs\" src=\""+img_link+"\"  /></a>";
            //document.getElementById("myExample3").innerHTML+=data2;

   }
    document.getElementById("myExample3").innerHTML =data2;
    //document.getElementById("myExample3").innerHTML=data;
  });

  };

 
</script>



<body onload="onld();">
<a href="#" >
    <img src="img/WHEREISIT.png" id="where" onload="this.width/=2;"/>
  </a>
<div id="myExample3" >

  </div>




<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-36251023-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>




</body>
</html>