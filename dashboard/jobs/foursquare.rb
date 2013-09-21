require 'httparty'
require 'json'

herenow = 0
users = ''
total_users = 0
user_index = 0
checkins = 0

index = 0

VENUE_ID = '521ed95711d227dca81a6504'
BASE_URL = "https://api.foursquare.com/v2/venues/#{VENUE_ID}/"

cnf = YAML::load_file(File.join(File.dirname(File.expand_path(__FILE__)), '../config.yml'))
CLIENT_ID = cnf['foursquare']['client_id']
CLIENT_SECRET = cnf['foursquare']['client_secret']
ACCESS_TOKEN = cnf['foursquare']['access_token']

SCHEDULER.every '2m', :first_in => 0 do |job|

  options = {:oauth_token => "#{ACCESS_TOKEN}", :v => "20130714"}

  # Get users here now
  response = HTTParty.get("#{BASE_URL}herenow", :query => options)

  if response.code === 200
    result = JSON.parse(response.body)['response']['hereNow']

    herenow = result['count']
    users = result['items'];
    total_users = users.size
  end

  # Get venue stats
  response = HTTParty.get("#{BASE_URL}stats", :query => options)

  if response.code === 200
    result = JSON.parse(response.body)['response']

    checkins = result['stats']['totalCheckins']
  end
end

SCHEDULER.every '5s', :first_in => '5s' do |job|

  if index == 0
    send_event('foursquare', title: 'Here right now', value: herenow, photo: '0')
  elsif index == 1
    send_event('foursquare', title: 'Total Check Ins', value: checkins, photo: '0')
  elsif index == 2

    if(users.size != 0)
      user_index = (user_index + 1)%total_users

      name = users[user_index]['user']['firstName']
      picture = users[user_index]['user']['photo']['prefix'] + "300x300" + users[user_index]['user']['photo']['suffix']
      send_event('foursquare', title: "#{name} is here", value: '', photo: picture)
    end
  end

  index = (index + 1)%3
end
