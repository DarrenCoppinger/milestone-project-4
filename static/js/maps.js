    function initMap() {
        var map = new google.maps.Map(document.getElementById("map"), {
            zoom: 15,
            center: {
                lat: 53.269750,
                lng: -9.051889
            }
        });
        var location = {
            lat: 53.269750,
            lng: -9.051889
        };
        var markers = new google.maps.Marker({
            position: location,
            map: map
        });
    }