function Item(context, x, y, height, text) {   
    this._main_color = "black";
    this._background_color = "white";
    this._accent_color = "red";
    
    var text_width = function () {
        return context.measureText(text).width;  
    };
    
    this.setColorScheme = function (main_color, background_color, accent_color) {
        this._main_color = main_color;
        this._background_color = background_color;
        this._accent_color = accent_color;
    };
    
    this.paint = function () {
        context.save();

        context.font = "30px Libre Baskerville, serif";

        context.translate(x + height, y);
        context.rotate(Math.PI / 2);
        var offset = 15;
        var textSize = 30;
        
        var gradient = context.createLinearGradient(0,0,170,0);
        gradient.addColorStop(1, this._main_color);
        gradient.addColorStop(0, this._background_color);
        context.fillStyle = gradient;        
        context.fillRect(0, 0, text_width() + 2 * offset, height);

        context.fillStyle = this._background_color;
        context.fillText(text, offset, height / 2 + textSize / 4);
        
        context.restore();
    };
}