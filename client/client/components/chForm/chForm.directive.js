'use strict';

angular.module('clientApp')
  .directive('chForm', function () {
    return {
      templateUrl : 'components/chForm/chForm.html',
      restrict    : 'EA',
      scope       : {
        	items     : '=',
        	title     : '@',
          type      : '@'
      },
      controller: 'chFormCtrl'
    };
  })

.controller("chFormCtrl", ['$scope', '$state', '$http', 
	function($scope, $state, $http){
		
	}]);