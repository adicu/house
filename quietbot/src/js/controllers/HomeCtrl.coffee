angular.module('app.controllers')
.controller 'HomeCtrl', ($scope, $http) ->
	$scope.actionCalled = false

	$scope.message = "Please be quiet."

	$scope.sendText = () ->
		data = message : $scope.message
		$http.post('/be_quiet', data)
			.success (data) ->
				$scope.successMessage = data.message
			.error (err) ->
				$scope.errorMessage = err.message

