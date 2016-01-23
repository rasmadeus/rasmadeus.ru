function MenuItems(canvas) {
    var context = canvas.getContext("2d");
    var items = [];
    
    this._main_color = "black";
    this._background_color = "white";
    this._accent_color = "red";
    
    this.append_items = function (text_items) {
        items = [];
        var height = 45;
        var offset = 20;
        var x = canvas.width/2 - text_items.length*height/2 - (text_items.length - 1)*offset/2;
        var y = 0;
        for(var i = 0; i < text_items.length; ++i) {
            var item = new Item(context, x, y, height, text_items[i]);
            item.setColorScheme(this._main_color, this._background_color, this._accent_color);
            x += offset;
            x += height;
            items.push(item);
        }
    };
    
    this.setColorScheme = function (main_color, background_color, accent_color) {
        this._main_color = main_color;
        this._background_color = background_color;
        this._accent_color = accent_color;
    };
    
    this.paint = function() {
        context.fillStyle = this._background_color;
        context.fillRect(0, 0, canvas.width, canvas.height);
        
        for(var i = 0; i < items.length; ++i) {
            items[i].paint();
        }
    };
}