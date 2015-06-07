'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, jurisdictions) {
    $scope.awesomeThings = [];
    $scope.jurisdictions = jurisdictions.jurisdictions;


    $scope.jurisdiction_name = "jurisdiction_one"


    $scope.addJurisdiction = function() {
      //console.log($scope.newJurisdiction)
      jurisdictions.addJurisdiction($scope.newJurisdiction)
    }

    $scope.jurisdiction = jurisdictions.parseObjArray($scope.jurisdictions, $scope.jurisdiction_name) 
    


    $scope.add = {

      jurisdiction: function(jurisdiction){
        console.log('adding jurisd', jurisdiction)
        // jurisdictions.addJurisdiction($scope.newJurisdiction)
      },

      office: function(office){
        // console.log($scope.jurisdiction_name , office)
        jurisdictions.addOffice($scope.jurisdiction_name , office)
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
