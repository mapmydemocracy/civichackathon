'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, jurisdictions) {
    $scope.awesomeThings = [];
    $scope.jurisdictions = jurisdictions.jurisdictions;

    $scope.addJurisdiction = function() {
      //console.log($scope.newJurisdiction)
      jurisdictions.addJurisdiction($scope.newJurisdiction)
    }
    
    $scope.add = {

      jurisdiction: function(jurisdiction){
        jurisdictions.addJurisdiction($scope.newJurisdiction)
      },

      district: function(district){
        jurisdictions.addDistrict($scope.newDistrict)
      },

      contest: function(contest){
        jurisdictions.addContest($scope.newContest)
      },

      candidate:function(candidate){
        jurisdictions.addCandidate($scope.newCandidate)
      }
    }

  });
