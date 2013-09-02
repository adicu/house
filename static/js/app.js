var app;

app = angular.module('app', ['app.controllers']);

app.config(function($routeProvider) {
  return $routeProvider.when('/', {
    templateUrl: 'static/partials/home.html',
    controller: 'HomeCtrl'
  }).otherwise({
    redirectTo: '/'
  });
});

angular.module('app.controllers', []);

angular.module('app.controllers').controller('HomeCtrl', function($scope) {});

/*
//@ sourceMappingURL=app.js.map
*/