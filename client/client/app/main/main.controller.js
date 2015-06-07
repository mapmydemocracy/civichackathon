'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, jurisdictions) {

    $scope.jurisdictions = jurisdictions.jurisdictions;





    $scope.jurisdiction_name = "jurisdiction_one"
    $scope.office_name = "Supervisor"







    $scope.addJurisdiction = function() {
      //console.log($scope.newJurisdiction)
      jurisdictions.addJurisdiction($scope.newJurisdiction)
    }

    




    $scope.jurisdiction = jurisdictions.parseObjArray($scope.jurisdictions, $scope.jurisdiction_name) 
    
    $scope.office = jurisdictions.parseObjArray($scope.jurisdiction.offices, $scope.office_name)

    console.log($scope.office)







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
        console.log($scope.jurisdiction_name , $scope.office_name, $scope.newDistrict)
        jurisdictions.addDistrict($scope.jurisdiction_name , $scope.office_name, $scope.newDistrict)
      },

      contest: function(contest){
        jurisdictions.addContest($scope.newContest)
      },

      candidate:function(candidate){
        jurisdictions.addCandidate($scope.newCandidate)
      }
    }

  });
