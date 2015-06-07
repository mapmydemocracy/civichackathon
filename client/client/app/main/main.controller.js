'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, jurisdictions) {
    $scope.awesomeThings = [];
    $scope.jurisdictions = jurisdictions.jurisdictions;

    $scope.addJurisdiction = function() {
      //console.log($scope.newJurisdiction)
      jurisdictions.addJurisdiction($scope.newJurisdiction)
    }
    
  });
