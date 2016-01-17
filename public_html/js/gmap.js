function init_map() {
    var map_canvas = document.getElementById("background");
    var map_options = {
        disableDefaultUI: true,
        center: new google.maps.LatLng(53.935894, 48.802024),
        zoom: 12,
        zoomControl: false,
        scrollwheel: false,
        disableDoubleClickZoom: true,
        draggable : false,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    var map = new google.maps.Map(map_canvas, map_options);
};