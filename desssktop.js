$('document').ready(function(){
    
    $.getJSON( '/cgi-bin/winslist.py', function(data){
        var dtop = data.shift();
        console.log(dtop);
        var scale = (2*dtop.w)/$(window).width();
        var screenheight = (~~(dtop.h/scale));

        console.log(scale);
        
        for( i in data )
        {
            var win = data[i];
            var w = (~~(win.w/scale));
            var h = (~~(win.h/scale));
            
            $('#wincontainer').append("<div class='win' id='"+win.id+"'><img style='width:100%;height:auto;' src='/"+win.id+".jpg'></div>");
            var style = {'width':w+'px','height':h+'px'};
            console.log(style);
            $('#'+win.id).css(style);
            $('#'+win.id).draggable().resizable().click(function(){ $.ajax('cgi-bin/show.py?w='+$(this).attr('id')); });
        }

        var $container = $('#wincontainer');
        $container.masonry({
          itemSelector: '.win'
        });
    });
    
});
