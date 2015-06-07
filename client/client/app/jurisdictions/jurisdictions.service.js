'use strict';

angular.module('clientApp')
  .factory('jurisdictions', function () {
    var o = 
    {
      jurisdictions: [
        {
          name: 'San Francisco City and County',
          offices : [
            {
              name: "Mayor",
              districts: []
            },
            {
              name: "Supervisor",
              districts: [
                {name: "District 1"},
                {name: "District 2"}
              ]
            }
          ]
        }
      ]
        
    }
    

    o.addJurisdiction = function(jurisdiction) {
        o.jurisdictions.push({name:jurisdiction, districts:[]})
        console.log('Adding jurisdiction ', jurisdiction)
      }

    o.addOffice = function(jurisdiction, office) {
      o.jurisdictions[jurisdiction]['offices'].push(office)
      contests.log('Adding office ', office)
    }

    o.addDistrict = function(jurisdiction, office, district){
      o.jurisdictions[jurisdiction][office]['districts'].push({name: district, contests:[]})
      contests.log('Adding district ', district)
    }

    o.addContest = function(jurisdiction, office, district, contest){
      o.jurisdictions[jurisdiction][office][district]['contests'].push({date: contest, candidates:[]})
      contests.log('Adding contest ', district)
    }

    o.addCandidate = function(jurisdiction, office, district, contest, candidates){
      o.jurisdictions.jurisdiction.office.district.contest['candidates'].push({name: contest, candidates:[]})
      contests.log('Adding contest ', district)
    }


    return o

  });
