app = angular.module('app', ['app.controllers'])
app.config ($routeProvider) ->
  $routeProvider.when('/',
    templateUrl: 'static/partials/home.html'
    controller: 'HomeCtrl'
  ).otherwise redirectTo: '/'
