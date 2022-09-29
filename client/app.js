function getBathroomValue() {
    var bathrooms = document.getElementsByName("bathrooms");
    for(var i in bathrooms) {
        if(bathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function getBedroomValue() {
    var bedrooms = document.getElementsByName("bedrooms");
    for(var i in bedrooms) {
        if(bedrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
return -1;
}

function onClickedEstimatedPrice() {
    console.log("Estimate price button clicked");
    var total_sqft = document.getElementById("area_sqft");
    var bedrooms = getBedroomValue();
    var bathrooms = getBathroomValue();
    var location = document.getElementById("locations");
    var est_price = document.getElementById("price");
    var url = "http://127.0.0.1:5000/house_pricing";
    // var url = "/api/predict_home_price";
    $.post(url, {
        location: location.value,
        total_sqft: parseFloat(total_sqft.value),
        bathrooms: bathrooms,
        bedrooms: bedrooms
    },function(data, status) {
        console.log(data.estimated_price);
        est_price.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log( "locations loaded" );

    // Use a url of your choice by uncommenting as you please.
    var url = "http://127.0.0.1:5000/locations";
    // var url = "/api/get_location_names";
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("locations");
            $("#locations").empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#locations').append(opt);
            }
        }
    })
}

window.onload = onPageLoad;

//ifunanyaScript