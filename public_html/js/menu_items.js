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
            item.set_color_scheme(this._main_color, this._background_color, this._accent_color);
            x += offset;
            x += height;
            items.push(item);
        }
    };
    
    this.set_color_scheme = function (main_color, background_color, accent_color) {
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
    
    this.process_mouse_move = function (ev) {
        var rect = canvas.getBoundingClientRect();
        var mouse_x = ev.clientX - rect.left;
        var mouse_y = ev.clientY - rect.top;

        for(var i = 0; i < items.length; ++i) {
            var item_contains_mouse = items[i].contains(mouse_x, mouse_y);
            items[i].set_hover(item_contains_mouse);
        }
    };
}