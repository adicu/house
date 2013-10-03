class Dashing.Clock extends Dashing.Widget

  ready: ->
    setInterval(@startTime, 500)

  startTime: =>
    today = new Date()

    h = today.getHours()
    ampm = 'AM'

    if(h > 12)
      h -= 12;
      ampm = 'PM'
    else
      ampm = 'AM'

    m = today.getMinutes()
    s = today.getSeconds()
    m = @formatTime(m)
    s = @formatTime(s)
    @set('time', h + ":" + m + ":" + s + " " + ampm)
    @set('date', today.toDateString())

  formatTime: (i) ->
    if i < 10 then "0" + i else i
