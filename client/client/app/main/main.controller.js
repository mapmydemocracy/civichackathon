'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, jurisdictions) {

    $scope.jurisdictions = jurisdictions.jurisdictions;


   $scope.candidates = jurisdictions.candidates


    $scope.jurisdiction_name = "San Francisco";
    $scope.office_name = "Supervisor";
    $scope.district_name = "District 3";
    $scope.contest_date = new Date('2015', '11', '05').toString();

    $scope.step = 1


    $scope.addJurisdiction = function() {
      //console.log($scope.newJurisdiction)
      jurisdictions.addJurisdiction($scope.newJurisdiction)
    }

    




    $scope.jurisdiction = jurisdictions.parseObjArray($scope.jurisdictions, $scope.jurisdiction_name) 
    
    $scope.office = jurisdictions.parseObjArray($scope.jurisdiction.offices, $scope.office_name)

    $scope.district = jurisdictions.parseObjArray($scope.office.districts, $scope.district_name)    

    $scope.contest = jurisdictions.parseObjArray($scope.district.contests, $scope.contest_date)

    console.log($scope.district.contests)
    console.log($scope.contest)



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
        console.log($scope.jurisdiction_name , $scope.office_name, district)
        jurisdictions.addDistrict($scope.jurisdiction_name , $scope.office_name, district)
      },

      contest: function(contest){
        console.log(contest)
        console.log($scope.jurisdiction_name , $scope.office_name, $scope.district_name, contest)
        jurisdictions.addContest($scope.jurisdiction_name , $scope.office_name, $scope.district_name, contest)
      },

      candidate:function(candidate){
        jurisdictions.addCandidate(candidate)
      }
    }

  });
