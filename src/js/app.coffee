app = angular.module('app', [])
app.config ($routeProvider) ->
  $routeProvider.when('/',
    templateUrl: 'static/partials/home.html'
    controller: 'HomeCtrl'
  ).otherwise redirectTo: '/'
