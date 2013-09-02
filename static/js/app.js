
var app = angular.module('app', []);

app.config( ['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/',  {templateUrl: 'static/partials/home.html',  controller: 'Home'})

        .otherwise({redirectTo: '/'});

}]);

