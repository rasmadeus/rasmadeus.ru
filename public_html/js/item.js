function Item(context, x, y, height, text) {
    var width = 0;
    
    this._is_hover = false;
    
    this._main_color = "black";
    this._background_color = "white";
    this._accent_color = "red";
    
    var text_width = function () {
        return context.measureText(text["text"]).width;  
    };
    
    this._item_background = function () {
        var gradient = context.createLinearGradient(0, 0, 100, 0);
        gradient.addColorStop(1, this._main_color);
        gradient.addColorStop(0, this._background_color);
        return gradient;
    };
    
    this.set_color_scheme = function (main_color, background_color, accent_color) {
        this._main_color = main_color;
        this._background_color = background_color;
        this._accent_color = accent_color;
    };
    
    this.set_hover = function (is_hover) {
        this._is_hover = is_hover;
    };

    this.contains = function(mouse_x, mouse_y) {
        return mouse_x >= x && mouse_x <= x + height && mouse_y >= y && mouse_y <= y + width;
    };

    this.paint = function () {
        context.save();

        context.font = "30px Serif";

        context.translate(x + height, y);
        context.rotate(Math.PI / 2);
        
        var offset = 15;
        var textSize = 30;      
        var hover_offset = this._is_hover ? 20 : 0;
        
        context.fillStyle = this._item_background();
        width = text_width() + 2 * offset;
        context.fillRect(0 + hover_offset, 0, width, height);

        context.fillStyle = this._background_color;
        context.fillText(text["text"], offset + hover_offset, height / 2 + textSize / 4);
        
        context.restore();
    };
    
    this.go = function () {
        if (text["url"]) {
            window.location.href = text["url"];
        }
    };
}