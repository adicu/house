angular.module('app.controllers')
.controller 'HomeCtrl', ($scope) ->
	$scope.actionCalled = false

	$scope.message = "Please be quiet"

	$scope.sendText = () -> 
		data = message : $scope.message
		$http.post('/be_quiet', data)
			.sucess (data) ->
				console.log data
			.error (err) ->
				console.log err

