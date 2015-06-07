'use strict';

angular.module('clientApp')
  .directive('chForm', function () {
    return {
      templateUrl : 'components/chForm/chForm.html',
      restrict    : 'EA',
      scope       : {
        	title        : '@',
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
		
	}]);