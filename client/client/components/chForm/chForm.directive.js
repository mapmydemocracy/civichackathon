'use strict';

angular.module('clientApp')
  .directive('chForm', function () {
    return {
      templateUrl : 'components/chForm/chForm.html',
      restrict    : 'EA',
      scope       : {
        	title        : '@',
          step         : '=',
          items        : '=',
          type         : '@',
          add          : "=",
          jurisdiction : '=?',
          office       : '=?',
          district     : '=?',
          contest      : '=?',
          candidate    : '=?',

      },
      controller: 'chFormCtrl'
    };
  })

.controller("chFormCtrl", ['$scope', '$state', '$http', 
	function($scope, $state, $http){

    // console.log(step)
		$scope.stepForward = function() {
      $scope.step = $scope.step + 1
    }
	}]);