class Dashing.Foursquare extends Dashing.Widget

  onData: (data) ->
    if(data.photo == '0')
      $('#foursquare_photo').hide();
    else
      $('#foursquare_photo').show();
